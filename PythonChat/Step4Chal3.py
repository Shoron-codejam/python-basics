numbers = []

while True :
    user_input = input ("Enter a number or (Type q for quit): ")
    if user_input.lower() == 'q':
        break
    number = int(user_input)
    numbers.append (number)
     
print ("List of numbers : ", numbers)

 

average = sum(numbers) / len(numbers)
print ("Total Average : ", average)

above_count = 0 
below_count = 0
equal_count = 0

for number in numbers:
    if number > average:
        above_count += 1
    elif number < average:
        below_count += 1
    else :  
        equal_count +=1        

print ("Total avobe average numbers : ", above_count)  
print ("Total below average numbers : ", below_count)      
print ("Total number that equal to average : ", equal_count)
