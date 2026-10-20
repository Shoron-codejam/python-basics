numbers = []

while True:
    user_input = input ("Enter a number(or type q to quite): ")
    
    
    if user_input.lower() == "q":
        break
    number = int(user_input)
    numbers.append(number)

print ("Number entered by you:", numbers)  
print ("The largrst number:", max (numbers)) 
print ("The smallest number:", min (numbers))