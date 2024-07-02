from gtts import gTTS

language = "en"
text = " hello world i am sentient machine"
speech  = gTTS(text = text, lang = language, slow= False , tld="com.au")
speech.save("textToSpeech.mp3")