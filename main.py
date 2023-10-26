
def Balance():
    balance = 845.70

    while True:
        try:
            num = float(input("Deposit: "))
            break
        except ValueError:
            return ("Must be a valid quantity.")

    balance += num
    return (f"Balance: {balance}")


print(Balance())
