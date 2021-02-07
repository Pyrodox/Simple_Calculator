class Def:
    def __init__(self, first, second):
        self.first = first
        self.second = second


class Adding(Def):
    def adding(self):
        result = self.first + self.second
        return result


class Subtracting(Def):
    def subtracting(self):
        result = self.first - self.second
        return result


class Multiplying(Def):
    def multiplying(self):
        result = self.first * self.second
        return result


class Dividing(Def):
    def dividing(self):
        try:
            result = self.first / self.second
        except ZeroDivisionError:
            result = "Undefined"
        return result


class Exponent(Def):
    def exponent(self):
        result = self.first ** self.second
        return result
