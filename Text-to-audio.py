from gtts import gTTS



from playsound import playsound



audio='speech.mp3'

language='en'



a=input("Enter the text to convert into audio : ")



sp=gTTS(a,lang=language,slow=False)



sp.save(audio)



playsound(audio)
