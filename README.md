# Virtual Assitant - Cookie

This a very basic virtual assistant which can do wiki search for you.

Text to speech framework used is  pyttsx3 
speech_recognition Library for performing speech recognition, with support for several engines and APIs, online and offline.

```
listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
```


#### pyttsx3 
Text to speech framework

`pip install pyttsx3`

An application invokes the pyttsx3.init() factory function to get a reference to a pyttsx3

### PyWhatKit
PyWhatKit is a Python library with various helpful features. It's easy-to-use and does not require you to do any additional setup. Added support for youtbe queries and playing a song.