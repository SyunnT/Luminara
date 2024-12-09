import platform
import socket

class SystemInfo:
    def __init__(self):
        self.host_name = socket.gethostname()
        self.os = {'system':platform.system(), 
                   'version':platform.version()}
        # TODO: 获取 cpu 信息：型号、架构、核心与线程、主频、
        self.cpu = platform.processor()