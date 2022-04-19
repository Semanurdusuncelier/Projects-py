import imp
from pytube import YouTube

link= input("Please add the  video link here :")
directory= input("directory")

try :
     yt=YouTube(link)
except:
     print("İnvalid link !")
     exit()

mp4s =yt.stream.filter(file_extension="mp4")

 
for i , mp4 in enumerate (mp4s):
     print(i+ 1 , mp4)

n=int(input("Select :"))

print("Video is Downloading...")

mp4s[n-1].download(directory)
print("Download complete !!")