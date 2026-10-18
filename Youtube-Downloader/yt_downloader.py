import yt_dlp
# Remember to install videos about Python librairies

def download_yt_video(url):
    ydl_opts = {
        "format": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
        "noplaylist": True,
        "merge_output_format": "mp4",
        "postprocessors": [
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    print("Hello! This is a YT Video Downloader!!")
    video_url = input("Enter the YouTube Video URL: ")
    download_yt_video(video_url)
    print("Video Downloaded!")
