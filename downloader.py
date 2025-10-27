import os
import sys
import re
from pytube import YouTube, Playlist
from pytube.cli import on_progress
from colorama import init, Fore, Style
from pathlib import Path
from moviepy.editor import AudioFileClip
import requests

# Initialize colorama
init(autoreset=True)

# Default folders
TERMUX_FOLDER = "/storage/emulated/0/Download/YT-Downloads/"
DESKTOP_FOLDER = os.path.join(os.getcwd(), "YT-Downloads")
DOWNLOAD_FOLDER = TERMUX_FOLDER if os.path.exists(TERMUX_FOLDER) else DESKTOP_FOLDER
THUMBNAIL_FOLDER = os.path.join(DOWNLOAD_FOLDER, "thumbnails")
HISTORY_LOG = os.path.join(DOWNLOAD_FOLDER, "downloads.log")

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
os.makedirs(THUMBNAIL_FOLDER, exist_ok=True)

# Helper: clean filenames
def clean_filename(name):
    return re.sub(r'[\\/*?:"<>|]',"", name)

# Helper: save download history
def log_history(title, url):
    with open(HISTORY_LOG, "a", encoding="utf-8") as f:
        f.write(f"{title} | {url}\n")

# Download thumbnail
def download_thumbnail(yt, folder):
    url = yt.thumbnail_url
    response = requests.get(url)
    file_path = os.path.join(folder, clean_filename(yt.title) + ".jpg")
    with open(file_path, "wb") as f:
        f.write(response.content)

# Download single video
def download_video():
    try:
        url = input(Fore.CYAN + "🎬 Enter YouTube video link: ").strip()
        yt = YouTube(url, on_progress_callback=on_progress)
        print(Fore.YELLOW + f"\nTitle: {yt.title}")
        print(Fore.YELLOW + f"Author: {yt.author}")
        print(Fore.YELLOW + f"Duration: {round(yt.length/60,2)} mins")

        # Ask download type
        print(Fore.MAGENTA + "\nSelect download type:")
        print("1. Video")
        print("2. Audio-only")
        choice_type = input("Enter choice (1/2, default 1): ").strip()
        choice_type = choice_type if choice_type in ["1","2"] else "1"

        if choice_type == "1":
            # Video streams
            streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
            print("\nAvailable qualities:")
            for i, stream in enumerate(streams,1):
                size_mb = round(stream.filesize/(1024*1024),2)
                print(f"{i}. {stream.resolution} - {size_mb} MB")
            choice_res = input("\nSelect quality number (default 1): ").strip()
            choice_res = int(choice_res)-1 if choice_res.isdigit() and int(choice_res)<=len(streams) else 0
            selected_stream = streams[choice_res]
            print(Fore.GREEN + "\n📥 Downloading video...")
            selected_stream.download(output_path=DOWNLOAD_FOLDER)
            print(Fore.GREEN + f"✅ Video saved to: {DOWNLOAD_FOLDER}")

        else:
            # Audio download
            audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
            print(Fore.GREEN + "\n📥 Downloading audio...")
            audio_path = audio_stream.download(output_path=DOWNLOAD_FOLDER)
            # Convert to MP3
            mp3_path = os.path.splitext(audio_path)[0] + ".mp3"
            clip = AudioFileClip(audio_path)
            clip.write_audiofile(mp3_path)
            clip.close()
            os.remove(audio_path)  # remove original file
            print(Fore.GREEN + f"✅ Audio saved to: {mp3_path}")

        # Download thumbnail
        download_thumbnail(yt, THUMBNAIL_FOLDER)

        # Log history
        log_history(yt.title, url)

    except Exception as e:
        print(Fore.RED + f"❌ Error: {e}")

# Download playlist
def download_playlist():
    try:
        url = input(Fore.CYAN + "🎬 Enter YouTube playlist link: ").strip()
        pl = Playlist(url)
        print(Fore.YELLOW + f"\nPlaylist: {pl.title} | Total videos: {len(pl.video_urls)}\n")
        for video_url in pl.video_urls:
            print(Fore.MAGENTA + f"\nDownloading: {video_url}")
            yt = YouTube(video_url, on_progress_callback=on_progress)
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            stream.download(output_path=DOWNLOAD_FOLDER)
            download_thumbnail(yt, THUMBNAIL_FOLDER)
            log_history(yt.title, video_url)
            print(Fore.GREEN + f"✅ Saved: {yt.title}")
    except Exception as e:
        print(Fore.RED + f"❌ Error: {e}")

# CLI Menu
def main_menu():
    while True:
        print(Fore.CYAN + "\n========== YT-Downloader ==========")
        print("1️⃣ Download Video")
        print("2️⃣ Download Audio")
        print("3️⃣ Download Playlist")
        print("4️⃣ Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            download_video()
        elif choice == "2":
            download_video()  # audio option is inside download_video()
        elif choice == "3":
            download_playlist()
        elif choice == "4":
            print(Fore.YELLOW + "Goodbye!")
            sys.exit(0)
        else:
            print(Fore.RED + "Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()