from Shift15.Restart_Function import confirm_restart

print("Don't enter fractions. ")


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


def usernums():
    while True:
        try:
            user_num = float(input("Enter a number: "))
            break
        except ValueError:
            print("Please try again.")
    return user_num


def sign():
    while True:
        signs = ["+", "-", "*", "/", "^"]
        operator_sign = input("Type either +, -, *, /, or ^: ")
        operator_sign1 = operator_sign.strip()
        if operator_sign1 not in signs:
            print("Please try again.")
        else:
            break
    return operator_sign1


while True:
    while True:
        num1 = usernums()
        users_sign = sign()
        num2 = usernums()
        calculate_by = SetNums(num1, num2)
        operations = {"+": calculate_by.adding, "-": calculate_by.subtracting, "*": calculate_by.multiplying,
                      "/": calculate_by.dividing, "^": calculate_by.exponent}
        try:
            print(operations.get(users_sign)())
            break
        except ZeroDivisionError:
            print("Please try again.")

    if confirm_restart() == "yes":
        continue
    else:
        break
