#write a program of factorial number in agiven range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

fact = 1
i = 1

print("Factorial numbers in the range", start, "to", end, "are:")

while fact <= end:
    if fact >= start:
        print(fact)
    i += 1
    fact *= i
