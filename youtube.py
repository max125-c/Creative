

import yt_dlp

def download_video():
    video_url = input("Enter a YouTube link to download: ")
    
    ydl_opts = {
        'format': 'best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

download_video()
