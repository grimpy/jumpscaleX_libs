from Jumpscale import j

JSBASE = j.baseclasses.object


class Coordinator(j.baseclasses.object):
    __jslocation__.replace("j.world.", "")

    def _init(self, **kwargs):
        self.services = {}
        self._name = None

    def _service_register(self, klass):
        self.__dict__[klass.__name__] = klass
        self.__dict__[klass.__name__].coordinator = self

    # def _service_action_ask(self,instance,name):
    #     cmd = [name,arg]
    #     self.q_in.put(cmd)
    #     rc,res = self.q_out.get()
    #     return rc,res

    # @property
    # def name(self):
    #     return self.data.name
    #
    # @property
    # def key(self):
    #     if self._key == None:
    #         self._key = "%s"%(j.core.text.strip_to_ascii_dense(self.name))
    #     return self._key

    def __str__(self):
        return "coordinator:%s" % self._name
