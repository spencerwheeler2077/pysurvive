class Time():
    def __init__(self):
        self.day = 0
        self.morning = True
        self.hour = 8

    def sleep(self):
        """Function to make it morning after sleep action is used"""
        self.day += 1
        self.morning = True
        self.hour = 8

    def action(self):
        """Function to add an hour after an action is used"""
        if self.hour == 12:
            if not self.morning:
                self.day += 1
                self.morning = True
            else:
                self.morning = False
            self.hour = 1
        else:
            self.hour += 1
            