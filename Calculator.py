from Calculate.DefiningParts import firstnum, sign, secondnum
from Calculate.Calculate import Adding, Subtracting, Multiplying, Dividing, Exponent
from Shift15.Restart_Function import confirm_restart

print("Don't enter fractions. ")

while True:
    def result_of(first, operator, second):
        if operator == "+":
            calculate_by = Adding(first, second)
            return calculate_by.adding()

        elif operator == "-":
            calculate_by = Subtracting(first, second)
            return calculate_by.subtracting()

        elif operator == "*":
            calculate_by = Multiplying(first, second)
            return calculate_by.multiplying()

        elif operator == "/":
            calculate_by = Dividing(first, second)
            return calculate_by.dividing()

        elif operator == "^":
            calculate_by = Exponent(first, second)
            return calculate_by.exponent()

    print(result_of(firstnum(), sign(), secondnum()))

    if confirm_restart() == "yes":
        continue
    else:
        break
