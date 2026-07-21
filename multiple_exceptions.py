try:
   num = int(input())
   print(10 / num)

except ValueError:
    print("Enter only numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")