# YouTube Video Downloader

A small command-line Python script that downloads a single YouTube video (up to 1080p) as an `.mp4` file using [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Features

- Downloads the best video + audio quality up to **1080p**
- Merges video and audio into a single **MP4** file
- Ignores playlists (only the video in the URL is downloaded)
- Automatic retries (20x) for failed downloads and fragments
- Uses your **Firefox cookies**, which helps with age-restricted videos and "confirm you're not a bot" errors
- Solves YouTube's JavaScript challenges using Deno or Node.js

## Requirements

| Requirement | Why it's needed |
|---|---|
| Python 3.10+ | Runs the script |
| `yt-dlp` (with the `default` extras) | Does the downloading; the extras include `yt-dlp-ejs` |
| [FFmpeg](https://ffmpeg.org/) | Merges the separate video and audio streams into one MP4 |
| [Deno](https://deno.com/) **or** [Node.js](https://nodejs.org/) | JavaScript runtime used by yt-dlp to solve YouTube challenges |
| Firefox | Source of the cookies (`cookiesfrombrowser`) |

### Python requirements (`requirements.txt`)

```text
yt-dlp[default]
```

Python 3.10 or newer is required. The other items in the table (FFmpeg, Deno or Node.js, Firefox) are not pip packages and must be installed separately, as shown below.

### Installing the dependencies

**1. Python package**

```bash
pip install -U "yt-dlp[default]"
```

or, using the included `requirements.txt`:

```bash
pip install -r requirements.txt
```

**2. FFmpeg**

```bash
# Arch / Omarchy
sudo pacman -S ffmpeg

# Debian / Ubuntu
sudo apt install ffmpeg

# macOS (Homebrew)
brew install ffmpeg

# NixOS: add `ffmpeg` to your packages or use `nix-shell -p ffmpeg`
```

On Windows: `winget install ffmpeg`.

**3. A JavaScript runtime (Deno or Node.js)**

```bash
# Deno (matches the script's default)
sudo pacman -S deno        # Arch / Omarchy
brew install deno          # macOS
# NixOS: nix-shell -p deno

# or Node.js
sudo pacman -S nodejs
```

If you use Node.js instead of Deno, change this line in the script:

```python
"js_runtimes": {"node": {}},
```

**4. Firefox**

Install Firefox and make sure you are **logged in to YouTube** in it.

## Usage

```bash
python main.py
```

Then paste the video URL when prompted:

```
Hello! This is a YT Video Downloader!!
Enter the YouTube Video URL: https://www.youtube.com/watch?v=XXXXXXXXXXX
```

The video is saved in the folder you ran the script from.

## Configuration

All options live in the `ydl_opts` dictionary:

| Option | Meaning |
|---|---|
| `format` | `bv*[height<=1080]+ba/b[height<=1080]`: best video up to 1080p + best audio, with a single-file fallback. Change `1080` to `720`, `1440`, etc. |
| `noplaylist` | Download only the single video, not the whole playlist |
| `merge_output_format` | Final container format (`mp4`) |
| `retries` / `fragment_retries` | How many times to retry on network errors |
| `cookiesfrombrowser` | Browser to read cookies from, e.g. `("chrome",)` or `("firefox",)` |
| `js_runtimes` | `{"deno": {}}` or `{"node": {}}` |
| `remote_components` | `["ejs:github"]` downloads the challenge solver from GitHub. Remove this line if `yt-dlp-ejs` is already installed (it is, with `yt-dlp[default]`) |

## Troubleshooting

- **`ffmpeg not found` / video and audio not merged**: install FFmpeg and make sure it is in your `PATH`.
- **`Sign in to confirm you're not a bot` or missing formats**: log in to YouTube in Firefox, close Firefox if the cookie database is locked, and update yt-dlp.
- **`Could not find firefox cookies database`**: Firefox is installed in a non-standard location (e.g. Flatpak/Snap). Use `("firefox", None, "/path/to/profile")` or switch browser.
- **Downloads suddenly stop working**: YouTube changes often. Update yt-dlp:

  ```bash
  pip install -U "yt-dlp[default]"
  ```

## Legal notice

Only download videos you have the right to download. Respect YouTube's [Terms of Service](https://www.youtube.com/t/terms) and the copyright of content creators. This project is for personal and educational use.
