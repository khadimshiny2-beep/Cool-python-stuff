from gtts import gTTS

text = "Hello Dear Traveler! Welcome to this small Python speech generator project. This project was made by importing the gtts module that converts text into that very .mp3 file that you're listening to right now. By the way, I wanted this to be the the README.md but I was just changed my mind hahaha. Also I advise you to use the 'uv' package when you wanna install Python modules. It's way more faster and it was made with Rust. After installing it on your system, run 'uv pip install' + the name of the module you're tryna use. Until we meet again Traveler!"

tts = gTTS (text=text,lang="en")

tts.save("speech.mp3")

print("Speech saved as speech.mp3")



