import pytube
url = input('Digite o Link do video: ')
yt = pytube.YouTube(url)
print(f'O video está sendo baixado {yt.title}')
video = yt.streams.first()
video.download()