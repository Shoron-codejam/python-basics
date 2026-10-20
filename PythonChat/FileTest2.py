file = open("myname.txt","r")
content = file.read()
print(content)

file = open("myname.txt","a")
file.write("\nI am improving in Python.")
file.close()

"""with open("myname.txt", "r") as file:
    content = file.read()

print(content)    ...   The professional way to open file"""