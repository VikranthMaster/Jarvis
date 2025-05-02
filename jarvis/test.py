import yt_dlp

def get_video_url(song_name):
    ydl_opts = {
        'quiet': True,  # Suppress output
        'extract_flat': True,  # Only get video URL without downloading
        'force_generic_extractor': True,  # Use generic extractor
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(f"ytsearch:{song_name}", download=False)
        if 'entries' in result:
            video_url = result['entries'][0]['url']  # Get the URL of the first result
            return video_url
        return None

song_name = "ONe of your girls weeknd"
video_url = get_video_url(song_name)
print(video_url)
