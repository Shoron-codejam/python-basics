def square(number):
    return number * number
def cube(number):
    return number * number * number

number = int(input("Enter a number : "))
result1 = square(number)
result2 = cube(number) 
print ("Square:", result1)
print ("cube:",result2)