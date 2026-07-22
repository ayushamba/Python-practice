age = int(input("enter your age:-"))
try:
    if age < 18 or age > 10:
        raise ValueError("age should be between 10 to 18")
    else:
        print("your age is valid")
except ValueError as err:
    print(f"Error: {err}")

print("welcome to the club")