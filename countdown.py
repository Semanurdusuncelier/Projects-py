import time 
t = int(input("How many second do you want to set the timer for ? "))

while t :
     mins=t//60
     secs = t%60
     timer='{:02d}:{:02d}'.format(mins,secs)
     print(timer,end ="\r")
     time.sleep(1)
     t-=1

print ("Pomodoro stars now !!")

for i in range (4):
     t=25*60
while t :
     mins=t//60
     secs = t%60
     timer='{:02d}:{:02d}'.format(mins,secs)
     print(timer,end ="\r")
     time.sleep(1)
     t-=1
     print("Break time !!")


t=25*60
while t :
     mins=t//60
     secs = t%60
     timer='{:02d}:{:02d}'.format(mins,secs)
     print(timer,end ="\r")
     time.sleep(1)
     t-=1
     print("Work time !!")