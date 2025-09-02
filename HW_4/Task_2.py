## Напишите класс Calculator со следующими методами:

# add(a,b)
# subtract(a,b)
# multiply(a,b)
# divide(a,b) (проверка деления на ноль)

# Решила задачу двумя способами, с "return" и с "print"

class Calculator1:

    def add (a, b):
        return a + b

    def subtract (a, b):
        return a - b

    def multiply (a, b):
        return a * b

    def divide (a, b):
        if b == 0:
            return "can not divide a number to 0, please, enter another number"
        else:
            return a / b

a = int(input("a = "))
b = int(input("b = "))

print(f'a + b = {Calculator1.add( a, b)}')
print(f'a - b = {Calculator1.subtract( a, b)}')
print(f'a * b = {Calculator1.multiply( a, b)}')
print(f'a / b = {Calculator1.divide( a, b)}')



class Calculator2:

     def add(a, b):
       print(f'a + b = { a + b }' )

     def subtract(a, b):
        print(f'a - b = { a - b }' )

     def multiply (a, b):
        print(f'a * b = { a * b }' )

     def divide (a, b):
        if b == 0:
            print("can not divide a number to 0, please, enter another number")
        else:
            print(f'a / b = { a / b }' )

a = int(input("a = "))
b = int(input("b = "))

Calculator2.add(a, b)
Calculator2.subtract(a, b)
Calculator2.multiply(a, b)
Calculator2.divide(a, b)

