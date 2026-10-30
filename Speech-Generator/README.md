# Speech Generator

A small Python project that converts text into an MP3 file using Google Text-to-Speech ([gTTS](https://gtts.readthedocs.io/)).

## Requirements

| Requirement | Why it's needed |
|---|---|
| Python 3.10+ | Runs the script |
| `gTTS` | Converts text to speech (`from gtts import gTTS`) |
| Internet connection | gTTS uses Google's online text-to-speech service |
| An audio player | To listen to the generated `speech.mp3` |

### Python requirements (`requirements.txt`)

```text
gTTS
```

## Installation

```bash
pip install -r requirements.txt
```

or with [`uv`](https://docs.astral.sh/uv/), a fast Python package installer written in Rust:

```bash
uv pip install -r requirements.txt
```

## Usage

```bash
python speech_generator.py
```

```
Speech saved as speech.mp3
```

The file `speech.mp3` is created in the folder you ran the script from.

## Configuration

Change these lines in the script:

```python
text = "Your text here"
tts = gTTS(text=text, lang="en")   # language code: "en", "fr", "es", ...
```

## Troubleshooting

- **`gTTSError` / connection errors**: check your internet connection. Google may also temporarily block too many rapid requests.
- **Wrong language or accent**: set the `lang` parameter (and optionally `tld`, e.g. `tld="co.uk"`).