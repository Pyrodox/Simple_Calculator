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
