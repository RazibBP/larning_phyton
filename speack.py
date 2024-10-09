from gtts import gTTS

text ="Hello guys. I am Tahsin from bangladesh in dhaka. how are you . all fine? so Wheare are your from? i am from home distric of madaripur. "

language = "en"

obj = gTTS(text =text,lang=language,slow=False)
obj.save("simpleintro.mp3")
