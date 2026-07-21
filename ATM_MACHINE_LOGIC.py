## making an atm card insert and giving the card back code by the exception handling

try:
    print("YOUR CARD IS INSERTED :)")
    CARD = int(input("ENTER YOUR CARD PIN:"))

    if CARD != 1234:
        raise ValueError("wrong pin buddy")
    else:
        print("your pin is correct buddy :)")
    
    cash = int(input("Enter the amount you want to withdraw:"))

    amount = 5000
    
    if cash > amount:
        raise ValueError("insufficient balance buddy")
    
    else:
        print(f"your cash is {cash} and your remaining balance is {amount - cash}")
    
except Exception as e:
    print(f"error: {e}")

finally:
    print("your card is ejected buddy :)")
    print("THANK YOU FOR USING OUR ATM SERVICE")