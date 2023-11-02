#! python3
from pytube import YouTube
from sys import exit

link = input("Enter the link you'd like to download:")
try:
    video = YouTube(link)
except Exception as e:
    print("Invalid link %s. Try again", e)
    exit()
print(f"Proceed to download :{video.title}?")

if (input("[y/n] ")) == "y":

    for i,j in enumerate(video.streams, 1):
        print(i, j.resolution)
    resolution = input("Enter the resolution:")
    video.streams.get_by_resolution(resolution)

    print("Download Completed")

print("invalid")
