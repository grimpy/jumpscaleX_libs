import time
import email
import email.utils
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from collections import namedtuple
from dateutil.parser import parse
from Jumpscale import j


Attachment = namedtuple(
    "Attachment", ["hashedfilename", "hashedfilepath", "hashedfileurl", "originalfilename", "binarycontent", "type"]
)


def parse_email_body(body):
    """
    Parses email body and searches for the attachements
    :return: (body, attachments)
    :rtype: tuple
    """

    message = email.message_from_string(body)
    return parse_email(message)


def parse_email(message):
    to_mail = message.get("To")
    from_mail = message.get("From")
    subject = message.get("Subject") if message.get("Subject") is not None else ""
    headers = get_headers(message.items())
    # Get the date from the headers
    val = [item["value"] for item in headers if item["key"].lower() == "date"]
    date = val[0] if len(val) != 0 else ""
    body = ""
    html_body = ""
    attachments = []
    g = message.walk()
    if message.is_multipart():
        next(g)  # SKIP THE ROOT ONE.

    for part in g:
        part_content_type = part.get_content_type()
        part_body = part.get_payload()
        part_filename = part.get_param("filename", None, "content-disposition")

        # get the body of the mail
        if part_content_type == "text/plain" and part_filename is None:
            body += part_body

        elif part_content_type == "text/html" and part_filename is None:
            html_body += part_body

        elif part_content_type is not None and part_filename is not None:
            attachments.append({"name": part_filename, "content": part_body, "contentType": part_content_type})

    return {
        "body": body,
        "attachments": attachments,
        "to": to_mail,
        "from": from_mail,
        "subject": subject,
        "htmlbody": html_body,
        "headers": headers,
        "date": date,
    }


def store_message(model, message, folder="inbox", unseen=True, recent=True):
    if isinstance(message, str):
        data = parse_email_body(message)
    elif isinstance(message, dict):
        message = dict_to_message(message)
        data = parse_email(message)
    else:
        data = parse_email(message)
    mail = model.new()
    mail.from_email = data["from"]
    mail.to_email = data["to"]
    mail.subject = data["subject"]
    mail.body = data["body"]
    mail.htmlbody = data["htmlbody"]
    mail.headers = data["headers"]
    new_format = "%d/%m/%Y %H:%M"
    if data.get("date"):
        old_date_format = parse(data.get("date"))
        mail.date = old_date_format.strftime(new_format)
    mail.attachments = data["attachments"]
    mail.folder = folder
    mail.unseen = unseen
    mail.recent = recent
    mail.uid = 0
    mail.uid_vv = 0
    mail.mtime = int(time.time())
    mail.save()
    return mail


def object_to_message(mail):
    textmessage = None
    plaintextmessage = None
    htmlmessage = None

    attachments = []
    if mail.body:
        plaintextmessage = MIMEText(mail.body, "plain")
        textmessage = plaintextmessage
    if mail.htmlbody:
        htmlmessage = MIMEText(mail.htmlbody, "html")
        if textmessage:
            textmessage = MIMEMultipart("alternative")
            textmessage.attach(plaintextmessage)
            textmessage.attach(htmlmessage)
        else:
            textmessage = htmlmessage

    for attachment in mail.attachments:
        if attachment.contenttype:
            part = MIMEBase(*attachment.contenttype.split("/"))
        else:
            part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.content)
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f'attachment; filename="{attachment.name}"')
        attachments.append(part)

    mainmessage = None
    if attachments:
        mainmessage = MIMEMultipart("mixed")
        mainmessage.attach(textmessage)
    else:
        mainmessage = textmessage

    mainmessage["from"] = mail.from_email
    mainmessage["to"] = mail.to_email
    mainmessage["subject"] = mail.subject
    for header in mail.headers:
        if header.key.lower() in ["content-type", "mime-version"]:
            continue
        mainmessage[header.key] = header.value

    for attachment in attachments:
        mainmessage.attach(attachment)
    return mainmessage


def dict_to_message(mail):
    textmessage = None
    plaintextmessage = None
    htmlmessage = None

    attachments = []
    if mail.get("body"):
        plaintextmessage = MIMEText(mail.get("body"), "plain")
        textmessage = plaintextmessage
    if mail.get("htmlbody"):
        htmlmessage = MIMEText(mail.get("htmlbody"), "html")
        if textmessage:
            textmessage = MIMEMultipart("alternative")
            textmessage.attach(plaintextmessage)
            textmessage.attach(htmlmessage)
        else:
            textmessage = htmlmessage

    for attachment in mail.get("attachments"):
        if attachment.contenttype:
            part = MIMEBase(*attachment.contenttype.split("/"))
        else:
            part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.content)
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f'attachment; filename="{attachment.name}"')
        attachments.append(part)

    mainmessage = None
    if attachments:
        mainmessage = MIMEMultipart("mixed")
        mainmessage.attach(textmessage)
    else:
        mainmessage = textmessage

    mainmessage["from"] = mail.get("From")
    mainmessage["to"] = mail.get("To")
    mainmessage["subject"] = mail.get("subject")
    mainmessage["date"] = mail.get("date")
    for header in mail.get("headers"):
        if header.key.lower() in ["content-type", "mime-version"]:
            continue
        mainmessage[header.key] = header.value

    for attachment in attachments:
        mainmessage.attach(attachment)
    return mainmessage


def get_headers(headers):
    rest_headers = []
    reserved_headers = ["To", "From", "Subject"]
    for key, val in headers:
        if key not in reserved_headers:
            rest_headers.append({"key": key, "value": val})
    return rest_headers


if __name__ == "__main__":
    data = 'To: rafy@gmail.com\nFrom: Rafy <rafy@incubaid.com>\nSubject: testing subject\nMessage-ID: <ace3555b-1715-3177-d707-ad8a982f0aeb@incubaid.com>\nDate: Thu, 19 Sep 2019 12:29:06 +0200\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101\n Thunderbird/60.8.0\nMIME-Version: 1.0\nContent-Type: multipart/mixed;\n boundary="------------54B39785043A597FAEBBBA3E"\nContent-Language: en-US\n\nThis is a multi-part message in MIME format.\n--------------54B39785043A597FAEBBBA3E\nContent-Type: multipart/alternative;\n boundary="------------7235A5D86007E410F6A6660D"\n\n\n--------------7235A5D86007E410F6A6660D\nContent-Type: text/plain; charset=utf-8; format=flowed\nContent-Transfer-Encoding: 7bit\n\ntesting body\n\n\n  Testing html\n\n\n\n--------------7235A5D86007E410F6A6660D\nContent-Type: text/html; charset=utf-8\nContent-Transfer-Encoding: 7bit\n\n<html>\n  <head>\n\n    <meta http-equiv="content-type" content="text/html; charset=UTF-8">\n  </head>\n  <body text="#000000" bgcolor="#FFFFFF">\n    <p>testing body <br>\n    </p>\n    <h1>Testing html </h1>\n    <p><br>\n    </p>\n  </body>\n</html>\n\n--------------7235A5D86007E410F6A6660D--\n\n--------------54B39785043A597FAEBBBA3E\nContent-Type: text/plain; charset=UTF-8;\n name="how to scedule a job"\nContent-Transfer-Encoding: base64\nContent-Disposition: attachment;\n filename="how to scedule a job"\n\nZnJvbSBKdW1wc2NhbGUuc2VydmVycy5teWpvYnMuTXlKb2JzRmFjdG9yeSBpbXBvcnQgYWRk\nCmouc2VydmVycy5teWpvYnMud29ya2VycwpqLnNlcnZlcnMubXlqb2JzLnNjaGVkdWxlKGFk\nZCw1NDU0NTMpCgo=\n--------------54B39785043A597FAEBBBA3E--'
    # data = "To: testing@dd.com\nFrom: Rafy <rafy@incubaid.com>\nSubject: trial 2\nMessage-ID: <34cefd88-2af6-906d-0ce1-889ba50ea117@incubaid.com>\nDate: Sun, 22 Sep 2019 16:23:31 +0200\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101\n Thunderbird/60.8.0\nMIME-Version: 1.0\nContent-Type: text/plain; charset=utf-8; format=flowed\nContent-Transfer-Encoding: 7bit\nContent-Language: en-US\n\ntesting the second trial\n"
    result = parse_email_body(data)
    print("done")

# https://github.com/incubaid/crm/blob/master/crm/mailer.py
