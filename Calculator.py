from Calculate.DefiningParts import usernums, sign
from Calculate.Calculate import SetNums
from Shift15.Restart_Function import confirm_restart

print("Don't enter fractions. ")

while True:
    a = usernums()
    b = sign()
    c = usernums()
    calculate_by = SetNums(a, c)
    operations = {"+": calculate_by.adding, "-": calculate_by.subtracting, "*": calculate_by.multiplying,
                  "/": calculate_by.dividing, "^": calculate_by.exponent}
    print(operations.get(b)())
    if confirm_restart() == "yes":
        continue
    else:
        break
