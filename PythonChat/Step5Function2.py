def analyze_number(number):
    if number == 0:
        return "Zero"
    elif number > 0:
            if number % 2 == 0:
                return "Positive Even"
            else:
                return "Positive Odd"
    else: 
           if number % 2 == 0:
                return "Negative Even"
           else:
                return "Negative Odd"
                             
number = int(input("Enter your number : "))
result = analyze_number(number)
print (result)