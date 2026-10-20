numbers = []

while True:
    user_input = input ("Enter a number (or type q to quit): ")

    if user_input.lower() == 'q':
        break
    number = int(user_input)
    numbers.append(number)

    

print ("List of numbers : ", numbers)
print ("Total numbers : " ,len(numbers))

even_count = 0
odd_count = 0

for number in numbers :
    if number % 2 == 0:
       even_count +=1
    else :
       odd_count += 1

print ("Even numbers : ", even_count)
print ("Odd Numbers : ", odd_count)