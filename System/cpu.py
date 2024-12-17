class cpu:
    def __init__(self):
        self.cpu_brand = None
        self.cpu_model = None
        self.cpu_core = 0
        self.cpu_thread = 0
        self.cpu_max_freq = 0
        self.cpu_base_freq = 0
        self.cpu_cache = {0, 0, 0}
        self.cpu_maxbit = 0

    def cpu_now_temprature(self):
        pass

    def cpu_now_usage(self):
        pass
    
    def cpu_now_freq(self):
        pass