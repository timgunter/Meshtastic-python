from SX127x.LoRa import *

from . import MeshInterface

class PyLoRaInterface(MeshInterface):
    def __init__(self, debugOut=None, noProto=False):
        MeshInterface.__init__(self, debugOut=debugOut, noProto=noProto)

    def _sendToRadio(self, toRadio):
        pass

    def connect(self):
        pass

    def close(self):
        pass

    def _readFromRadio(self):
        pass

class Router:
    def __init__(self):
        pass
