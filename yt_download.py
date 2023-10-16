#! python3
from pytube import YouTube
from sys import argv, exit

if argv[1]:
    yt = YouTube(argv[1])

    video = yt.streams.get_highest_resolution()

    video.download()
    print("Download Completed")
    exit()
print("invalid")
