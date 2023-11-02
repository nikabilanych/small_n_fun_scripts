#! python3
from pytube import YouTube

link=input("Enter the link you'd like to download:")
video=YouTube(link)
print(f"Proceed to download :{video.title}?")

if (input("[y/n] "))=="y":
    resolution=input()
    print(f"Enter the resolution {i for i}
    video.streams.get_highest_resolution()

    video.download()
    print("Download Completed")

print("invalid")
