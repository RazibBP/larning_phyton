from gtts import gTTS

text = "Hello Tahsin speaking from Dhaka mohammadpur.How can i help you please tell me What is your problem.sorry please tell me details your problem again."

language  = "en"

sub =gTTS(text = text,lang=language,slow=False)
sub.save('simple.mp3')