import pytube
link="https://www.youtube.com/watch?v=vQFcqcpySyY"
yt= pytube.YouTube(link)
yt.streams.first().download()
print("Success")