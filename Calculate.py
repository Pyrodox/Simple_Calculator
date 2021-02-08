class SetNums:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def adding(self):
        result = self.first + self.second
        if result.is_integer():
            result1 = int(result)
            return result1
        else:
            return result

    def subtracting(self):
        result = self.first - self.second
        if result.is_integer():
            result1 = int(result)
            return result1
        else:
            return result

    def multiplying(self):
        result = self.first * self.second
        if result.is_integer():
            result1 = int(result)
            return result1
        else:
            return result

    def dividing(self):
        result = self.first / self.second
        if result.is_integer():
            result1 = int(result)
            return result1
        else:
            return result

    def exponent(self):
        result = self.first ** self.second
        if result.is_integer():
            result1 = int(result)
            return result1
        else:
            return result
