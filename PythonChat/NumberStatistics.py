def is_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def square(number):
    return number * number 
   
def average(numbers):
    return sum(numbers) / len(numbers)

numbers = []
while True:
    user_input = input ("Enter a number(or type q to quite): ")
    
    
    if user_input.lower() == "q":
        break
    number = int(user_input)
    numbers.append(number)

result1 = average(numbers) 

print ("Average:", result1)

for number in numbers:
    even_or_odd = is_even(number)
    squared = square(number)
    print(number, "->", even_or_odd, "-> Square:", squared)

#f-string can be use to make that last print more professional.print(f"{number} -> {even_or_odd} -> Square: {squared}")