def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact

number=int(input(" enter any Number to find factorial :"))

factof= factorial(number)
print("factorial is:" ,factof)