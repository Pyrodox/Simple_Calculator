def firstnum():
    while True:
        try:
            first_num = float(input("Type a number and press enter: "))
            break
        except ValueError:
            print("Please try again.")
    return first_num


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


def secondnum():
    while True:
        try:
            second_num = float(input("Type another number and press enter: "))
            break
        except ValueError:
            print("Please try again.")
    return second_num
