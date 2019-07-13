class Clock:
    def __init__(self, hour=1, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._seconds = second

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        self._hour = value

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        self._minute = value

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, value):
        self._seconds = value

    def parse_clock(self, hour, minutes):
        self.hour = int(hour) * 60
        self.minute = int(minutes)
        self.seconds = 0

    def time_to_seconds(self):
        hour = int(self.hour) * 60
        minute = int(self.minute) * 60
        return hour + minute

    def clock_to_str(self):
        if int(self.hour) >= 60:
            hour = '0' + str(int(self.hour / 60))
        else:
            hour = '00'

        if int(self.minute) < 10:
            minute = '0' + str(int(self.minute))
        else:
            minute = str(int(self.minute))

        time = f"{hour}:{minute}:00"

        return time

    @staticmethod
    def get_minute_list():
        min_list = [str(i) for i in range(0, 60)]
        return min_list
