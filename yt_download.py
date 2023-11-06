#! python3
from pytube import YouTube
from sys import exit

link = input("Enter the link you'd like to download:")
try:
    video = YouTube(link)
except Exception as e:
    print("Invalid link. Try again:", e)
    exit()
print(f"Proceed to download :{video.title}?")

if (input("[y/n] ")) == "y":
    resolutions={}
    for i, j in enumerate(video.streams, 1):
        resolutions.setdefault(j.resolution,i)
        print(resolutions[j.resolution])
        
    resol = input("Enter the resolution:")
    video.streams.get_by_resolution(resol)

    print("Download Completed")

print("invalid")
