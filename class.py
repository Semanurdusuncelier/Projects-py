class_animal = ["cat","stork","eagle","seagull"]
class_flower =["rose","orchid","peony","hyacint"]

name=input("Select name:")

if name in class_animal:
     print(" Avaiable in class animal")

elif name in class_flower:
     print("Avaiable in  class flower")

else :
     print("Oops ! Not in class animal and flower")