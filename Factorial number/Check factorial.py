#write a program to check given is factorial number or not
n = int(input("Enter a number: "))

fact = 1
i = 1

while fact < n:
    i += 1
    fact *= i

if fact == n:
    print(n, "is a factorial number (", i, "!)")
else:
    print(n, "is not a factorial number")
