print("Decimal to Binary, Octal, and Hexadecimal".center(100, "."))
print()
while True:
    try:
        decimal = int(input("Enter a number with base 10: "))
        print()
        print(f"\tDEC   {decimal:,}")
        print(f"\tBIN   {bin(decimal).lstrip('0b')}")
        print(f"\tOCT   {oct(decimal).lstrip('0o')}")
        print(f"\tHEX   {hex(decimal).lstrip('0x').upper()}")
        break

    except ValueError:
        print("Invalid Input!")
        continue
