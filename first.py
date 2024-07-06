def add(a, b, c, d,):
    return a + b+ c+ d

def subtract(a, b, c, d):
    return a - b - c - d

def multiply(a, b, c, d,):
    return a * b * c * d



C = int(input('''Enter your choice:
1: add
2: subtract
3: multiply

'''))

no1 = int(input("no1: "))
no2 = int(input("no2: "))
no3 = int(input("no3: "))
no4 = int(input("no4: "))
if C == 1:
    print(add(no1, no2,no3,no4))

elif C == 2:
    print(subtract(no1, no2,no3,no4))

elif C == 3:
    print(multiply(no1,no2,no3,no4))


else:
    print("Invalid choice")