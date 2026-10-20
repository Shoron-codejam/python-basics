with open ("myname.txt","a") as file :
    file.write("\nLearning Python every day.")

with open ("myname.txt","r") as file :
       print (file.read ())     