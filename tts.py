import pyttsx3

# Voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
voiceRate = 145
engine.setProperty("rate", voiceRate)


# Speak Function
def speak(text: str):
    engine.say(text)
    print("Gideon: " + text)
    engine.runAndWait()
