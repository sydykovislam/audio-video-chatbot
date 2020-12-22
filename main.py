import youtube_dl
import telebot


bot = telebot.TeleBot('botsId')

def youtube(url):
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    
    with youtube_dl.YoutubeDL(options) as ydl:
        res = ydl.extract_info(url, download=False)
        return res['url']

