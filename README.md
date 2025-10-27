
# ðŸŽ¬ YT-Downloader

A powerful **YouTube Video & Playlist Downloader** written in **Python**, supporting **video**, **audio (MP3)**, and **playlist downloads** with **thumbnail saving**, **progress tracking**, and **history logging**.

---

## ðŸš€ Features
âœ… Download **single YouTube videos** in any resolution  
âœ… Download **audio-only (MP3)** versions  
âœ… Download **entire playlists** automatically  
âœ… Save **video thumbnails**  
âœ… Maintain **download history log**  
âœ… Works on **Desktop & Termux (Android)**  
âœ… Beautiful **colored CLI interface**

---

## ðŸ§° Requirements

### Install Required Libraries
Run this in your terminal:
```bash
pip install pytube moviepy colorama requests
```

> âš ï¸ On Termux, use:
```bash
pkg install python ffmpeg
pip install pytube moviepy colorama requests
```

---

## ðŸ“ Folder Structure

```
YT-Downloads/
â”‚
â”œâ”€â”€ thumbnails/         # Saved video thumbnails
â”œâ”€â”€ downloads.log       # History log file
â””â”€â”€ *.mp4 / *.mp3       # Downloaded videos or audios
```

---

## ðŸ’» How to Use

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/YT-Downloader.git
   cd YT-Downloader
   ```

2. **Run the script**
   ```bash
   python main.py
   ```

3. **Choose an option**
   ```
   1ï¸âƒ£ Download Video
   2ï¸âƒ£ Download Audio
   3ï¸âƒ£ Download Playlist
   4ï¸âƒ£ Exit
   ```

4. Paste your YouTube or Playlist link when prompted.

---

## ðŸ§  Example Run

```
========== YT-Downloader ==========
1ï¸âƒ£ Download Video
2ï¸âƒ£ Download Audio
3ï¸âƒ£ Download Playlist
4ï¸âƒ£ Exit
Enter your choice: 1
ðŸŽ¬ Enter YouTube video link: https://youtu.be/xyz123
```

âœ… Downloads your selected video/audio  
âœ… Saves thumbnail under `/thumbnails`  
âœ… Logs all downloads in `downloads.log`

---

## âš™ï¸ Code Explanation

### ðŸ— Imports
Handles video/audio downloading, file conversions, and colorful terminal output.

### ðŸ“‚ Folder Setup
Automatically detects **Termux (Android)** or **Desktop** and creates folders:
- Downloads
- Thumbnails
- History Log

### ðŸ§© Helper Functions
- **clean_filename()** â†’ Cleans file names.  
- **log_history()** â†’ Logs video title & URL.  
- **download_thumbnail()** â†’ Saves thumbnail images.

### ðŸ“º Video & Audio Downloader
- Supports **video** or **audio-only (MP3)** download.
- Converts `.mp4` audio streams to `.mp3` using **MoviePy**.

### ðŸŽ§ Playlist Downloader
- Downloads each video from a YouTube playlist.  
- Saves its thumbnail and updates the history log.

### ðŸ§­ CLI Menu
Interactive text-based interface with colorized choices.

---

## ðŸ§© Supported Platforms
- ðŸªŸ Windows  
- ðŸ§ Linux  
- ðŸŽ macOS  
- ðŸ“± Termux (Android)

---

## ðŸ“œ License
This project is open-source under the [MIT License](LICENSE).

---

## ðŸ’¡ Author
**Developed by [Amos Anand](https://github.com/BuiltByAmos-1801)**  
ðŸš€ _Freelancer â€¢ Software Developer â€¢ UI/UX Designer_
