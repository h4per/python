from pytube import YouTube

url = input('Вставьте ссылку: ')
type_video = input('mp3, mp4:')
yt = YouTube(url)
# yt.streams.first().download()
if type_video == 'mp4':
    yt.streams.filter(file_extension='mp4').first().download('video', f'{yt.title}.mp4')
elif type_video == 'mp3':
    yt.streams.filter(only_audio=True).first().download('audio', f'{yt.title}.mp3')
print("Скачано")