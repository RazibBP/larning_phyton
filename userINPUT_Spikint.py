from gtts import gTTS
try:
    sal = input("you can convert your writin data to skioing MP3 voice data so Enter your all data: ")

    sub = gTTS(text=sal,lang='en',slow=False)
    sub.save("Your Audio File.mp3")
except KeyboardInterrupt:
    print("Enput Error: ")
except AssertionError:
    print("Assertion Error: ")