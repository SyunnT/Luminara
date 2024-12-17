class portion:
    def __init__(self):
        self.portion_id = None
        self.portion_name = None
        self.portion_capacity = 0
        self.portion_fs = None

    def portion_now_usage(self):
        pass

class driver:
    def __init__(self):
        self.driver_brand = None
        self.driver_model = None
        self.driver_capacity = 0
        self.dirver_portions = portion()

    def driver_now_usage(self):
        pass

class disk:
    def __init__(self):
        self.disk_drivers = driver()
        self.disk_raid = None

    def disk_update(self):
        pass