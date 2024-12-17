from system.os import os
from system.cpu import cpu
from system.memory import memory
from system.gpu import gpu
from system.disk import disk

class system:
    def __init__(self):
        self.os = os()
        self.cpu = cpu()
        self.memory = memory()
        self.gpu = gpu()
        self.disk = disk()