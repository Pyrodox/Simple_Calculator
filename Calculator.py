from Calculate.DefiningParts import usernums, sign
from Calculate.Calculate import SetNums
from Shift15.Restart_Function import confirm_restart

print("Don't enter fractions. ")

while True:
    calculate_by = SetNums(usernums(), usernums())
    operations = {"+": calculate_by.adding(), "-": calculate_by.subtracting(), "*": calculate_by.multiplying(),
                  "/": calculate_by.dividing(), "^": calculate_by.exponent()}
    print(operations.get(sign()))
    if confirm_restart() == "yes":
        continue
    else:
        break
