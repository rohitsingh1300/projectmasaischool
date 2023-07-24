from pytube import YouTube
link ="https://www.youtube.com/live/QhSFibjnclw?feature=share"
youtube_1=YouTube(link)
print(youtube_1.title)
print(youtube_1.thumbnail_url)
videos =youtube_1.streams.all()
vid=list(enumerate(videos))
for i in vid:
    print(i)
print()
strm=int(input("enter :"))
videos[strm].download()
print("successfully")