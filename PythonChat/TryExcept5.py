def check_grade(test_score):
            if test_score >= 90:
               return ("A")
            elif test_score >= 80:
               return ("B")
            elif test_score >= 70:
               return ("C")
            elif test_score >= 60:
               return ("D")
            else:
               return ("F")


while True:
    try:
      test_score = int(input("What is your test score: "))
      if test_score < 0 or test_score > 100 :
         print ("Test score must be into or 0 to 100")
      else:
         result = check_grade(test_score)
         print (f"Your gread is : {result}")
         break
    except ValueError:
          print("Please Enter a valid number.")     
            
