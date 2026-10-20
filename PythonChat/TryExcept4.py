while True: 
    try:
     age = int(input("What is your age? : "))
     if age <= 0 and age >= 100 :
        print("Age must be greater than 0.")
     else:  
      print(f"Your age : {age}")  
      break
    except ValueError:
      print("Please Enter a valid number.")   