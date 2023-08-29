class Interval:
    def __init__(self, hours=0, minutes=0, seconds=0):
        if not (hours >= 0 and 59 >= minutes >=0 and 59 >= seconds >= 0):
            raise ValueError('There must be hours >= 0, 59 >= minutes >= 0, and 59 >= seconds >= 0')
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add__(self, other):
        other = self.__verify_parameter(other)
        hours = self.hours + other.hours
        minutes = self.minutes + other.minutes
        seconds = self.seconds + other.seconds
        hours, minutes, seconds = self.correct_positive(hours, minutes, seconds)
        return Interval(hours, minutes, seconds)

    def __sub__(self, other):
        other = self.__verify_parameter(other)
        hours = self.hours - other.hours
        minutes = self.minutes - other.minutes
        seconds = self.seconds - other.seconds
        if seconds < 0:
            seconds += 60
            minutes -= 1
        if minutes < 0:
            minutes += 60
            hours -= 1
        return Interval(hours, minutes, seconds)

    def __mul__(self, value):
        if value < 0:
            raise ValueError("The multiplier must be positive")
        hours = self.hours * value
        minutes = self.minutes * value
        seconds = self.seconds * value
        hours, minutes, seconds = self.correct_positive(hours, minutes, seconds)
        return Interval(hours, minutes, seconds)

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'

    @staticmethod
    def correct_positive(hours, minutes, seconds):
        if seconds > 59:
            seconds %= 60
            minutes += 1
        if minutes > 59:
            minutes %= 60
            hours += 1
        return hours, minutes, seconds

    @staticmethod
    def __verify_parameter(other):
        if isinstance(other, Interval):
            return other
        elif isinstance(other, int):
            hours, minutes, seconds = Interval.correct_positive(0, 0, other)
            return Interval(hours, minutes, seconds)
        else:
            raise TypeError('Only Interval classes can be added')


fti = Interval(21, 58, 50)
sti = Interval(1, 45, 22)
print(fti + sti)
print(fti - sti)
print(fti * 2)

tti = Interval(21, 58, 50)
print(tti + 62)
print(tti - 62)