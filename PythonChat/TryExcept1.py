try:
    age = int(input("What is your age? : "))
    print(f"Your age : {age}")   
except ValueError:
    print("Please Enter a valid naumber.")    