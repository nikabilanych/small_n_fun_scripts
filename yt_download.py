#! python3
from pytube import YouTube
from sys import argv, exit
link=input("Enter the link you'd like to download:")
video=YouTube(link)
print(f"Proceed to download :{video.title}?")
activator=
if video:
    video = yt.streams.get_highest_resolution()

    video.download()
    print("Download Completed")
    exit()
print("invalid")
