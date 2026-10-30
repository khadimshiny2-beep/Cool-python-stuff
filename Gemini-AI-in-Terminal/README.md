# Gemini Chatbot

A simple terminal chatbot that sends your questions to Google's Gemini API and prints the answers. Type `exit` to quit.

## Requirements

| Requirement | Why it's needed |
|---|---|
| Python 3.10+ | Runs the script |
| `google-genai` | Official Google Gen AI SDK (`from google import genai`) |
| `python-dotenv` | Loads your API key from a `.env` file |
| Gemini API key | Authenticates your requests, get one free at [Google AI Studio](https://aistudio.google.com/apikey) |
| Internet connection | Needed to reach the Gemini API |

### Python requirements (`requirements.txt`)

```text
google-genai
python-dotenv
```

## Installation

```bash
pip install -r requirements.txt
```

or with `uv`:

```bash
uv pip install -r requirements.txt
```

## Setup

Create a file named `.env` in the same folder as the script:

```env
GEMINI_API_KEY=your_api_key_here
```

> **Never commit your `.env` file.** Add `.env` to your `.gitignore`.

## Usage

```bash
python gemini_chatbot.py
```

```
--You--: What is a Python decorator?
'-_Gemini_-':  A decorator is a function that wraps another function...
--You--: exit
```

## Configuration

The model is set in the script:

```python
model = "gemini-3.6-flash",
```

If you get a "model not found" error, replace it with a model name that is currently listed in the [Gemini API docs](https://ai.google.dev/gemini-api/docs/models).

## Troubleshooting

- **`KeyError: 'GEMINI_API_KEY'`**: the `.env` file is missing, is in a different folder, or the variable name is misspelled.
- **`403` / `API key not valid`**: check that the key is correct and has not been revoked.
- **`429` errors**: you hit the free-tier rate limit; wait a bit and retry.
- The chatbot does **not** remember previous messages: each question is sent on its own.