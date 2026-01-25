a = 50
while (a > 0):
    print(f"Amount Due: {a}")
    x = int(input("Insert Coin: "))
    if x in [25, 10, 5]:
        a -= x
    else:
        pass
a *= -1
print(f"Change Owed: {a}")
