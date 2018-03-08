import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
	print('Adjusting...')
	r.adjust_for_ambient_noise(source)

with sr.Microphone() as source:
	print("Start talking")
	audio = r.listen(source)

print("Done recording")

with open("result.wav", "wb") as f:
	f.write(audio.get_wav_data())
	print("written to file")