a = int(input())
b = int(input())
c = int(input())
if c < 0:
    print("NO SOLUTION")
elif a == 0:
    if c ** 2 == b and b >= 0:
        print("MANY SOLUTIONS")
    else:
        print("NO SOLUTION")
else:
    sol = ((c ** 2) - b) / a
    if sol % 1 != 0:
        print("NO SOLUTION")
    else:
        print(round(sol))