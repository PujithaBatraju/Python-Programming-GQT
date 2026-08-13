#Calculate the factorial of a number
num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)

OUTPUT:Enter a number: 6
       Factorial = 720