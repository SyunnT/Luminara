from PySide6.QtCore import QSysInfo

class os:
    def __init__(self):
        os = QSysInfo()
        self.name = os.productType()
        self.version = os.productVersion()
        self.architecture = os.currentCpuArchitecture()