from  pytube import YouTube
from sys import argv

"""Get Info Video"""
#link = argv[1]
link = input("Link video: ")
yt = YouTube(link)  
print(f"Title: {yt.title}")
print(f"Views: {yt.views}")
print(f"Author: {yt.author}")
print(f"Channel: {yt.channel_url}")

"""DownLoad Video"""
# yd = yt.streams.get_highest_resolution()
# yd.download(*)
