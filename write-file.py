from certifi import contents


content ="Hello world !"

#with open("file.txt","w") as file :  -another option
     #file.write(content) another -option
file = open ("file.txt","a")
file.close()