try:
    print("Don't enter fractions. ")

    a = float(input("Type a number and press enter: "))
    b = input("Type either +, -, *, /, or ^: ")
    c = float(input("Type another number and press enter: "))
    result = str(0)

    def calculator(first, sign, second):
        if "+" == sign:
            result = first + second
        elif "-" == sign:
            result = first - second
        elif "*" == sign:
            result = first - second
        elif "/" == sign:
            result = first / second
        elif "^" == sign:
            result = first ** second
        else:
            result = str("Not a valid mathematical equation. Try again.")
        return result


    if isinstance(result, str):
        print(calculator(a, b, c))
    else:
        print("Your answer is:", calculator(a, b, c))


except ValueError:
    print("The calculator has been stopped; please enter a valid input.")
except ZeroDivisionError:
    print("Undefined")