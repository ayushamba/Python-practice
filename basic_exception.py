a = input("tell your number:")

try:
    print(10/a)
except Exception as err:
    print(f"sorry {err}")
else:
    print("there is no error")

print("hi")