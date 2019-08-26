from Jumpscale import j
from .SendGridClient import SendGridClient


JSConfigs = j.baseclasses.object_config_collection


class SendgridFactory(JSConfigs):

    __jslocation__ = "j.clients.sendgrid"
    _CHILDFACTORY_CLASS = SendGridClient

    def test(self):
        """

        :return:
        """

        SENDER = "test@threefold.tech"
        RECIPENT = "test@threefold.tech"
        SUBJECT = "Sending with SendGrid is Fun"
        MESSAGE_TYPE = "text/plain"
        MESSAGE = "and easy to do anywhere, even with Python"

        statCode, body = self.send(SENDER, SUBJECT, MESSAGE, [RECIPENT], MESSAGE_TYPE, attachments=[])

        j.shell()

        self._log_info(statCode)
