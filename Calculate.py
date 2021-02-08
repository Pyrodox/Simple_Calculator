class SetNums:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def adding(self):
        result = self.first + self.second
        return result

    def subtracting(self):
        result = self.first - self.second
        return result

    def multiplying(self):
        result = self.first * self.second
        return result

    def dividing(self):
        try:
            result = self.first / self.second
            return result
        except ZeroDivisionError:
            print("Please try again.")

    def exponent(self):
        result = self.first ** self.second
        return result
