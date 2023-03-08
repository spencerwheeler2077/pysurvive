class Time():
    def __init__(self):
        self.__day = 0
        self.__morning = True
        self.__hour = 8

    def getDay(self):return self.__day
    def getHour(self): return self.__hour
    def getMorning(self): return self.__morning

    def sleep(self):
        """Function to make it morning after sleep action is used"""
        self.__day += 1
        self.__morning = True
        self.__hour = 8

    def action(self):
        """Function to add an hour after an action is used"""
        if self.__hour == 12:
            if not self.__morning:
                self.__day += 1
                self.__morning = True
            else:
                self.__morning = False
            self.__hour = 1
        else:
            self.__hour += 1

    def travel(self):
        """Function that runs after the travel function is called runs the action function a few times"""
        for i in range(2):
            self.action()
            