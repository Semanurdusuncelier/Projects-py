from pytube import YouTube
import os 

link = input("Please add the link here:")
directory= input("Directory :")

try :
     yt=YouTube(link)
except:
     print("İnvalid link !!")
     exit()

mp3 = yt.streams.filter(only_audio=True).first()

print("Downloading audio file...")
output=mp3.dowload(directory)

base,ext=os.path.splittext()
to_mp3=".mp3"
os.rename(output,to_mp3)

print("Dowload completed !!")