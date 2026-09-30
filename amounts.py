"""Amount input and exact splitting."""

def get_amount():
    while True:
        text = input("Total bill amount in rupees: ").strip()
        parts = text.split(".")
        if len(parts) > 2 or not parts[0].isascii() or not parts[0].isdigit():
            print("Enter an amount such as 500 or 500.50.")
            continue
        fraction = ""
        if len(parts) == 2:
            fraction = parts[1]
            if not fraction.isascii() or not fraction.isdigit() or len(fraction) > 2:
                print("Use one or two digits after the decimal point.")
                continue
        fraction = fraction.ljust(2, "0")
        amount = int(parts[0]) * 100 + int(fraction)
        if amount < 1:
            print("The amount must be greater than zero.")
            continue
        return amount


def money(paise):
    return str(paise // 100) + "." + str(paise % 100).zfill(2)


def split_amount(amount, people):
    shares = []
    for i in range(people):
        share = amount // people
        if i < amount % people:
            share = share + 1
        shares.append(share)
    return shares


