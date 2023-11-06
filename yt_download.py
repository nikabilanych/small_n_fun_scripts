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
    print("Downloading...")

    video.streams.get_lowest_resolution().download()

    print("Download Completed")
