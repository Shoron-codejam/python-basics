def check_grade(score):
    if score >= 90:
        return ("A")
    elif score >= 80:
        return ("B")
    elif score >= 70:
        return ("C") 
    else :
        return ("Fail")   

score = int(input("Enter your score : "))
result = check_grade(score)  
print (result)  

"""It can be def get_grade(score) if I want to write "print" instade of return"""