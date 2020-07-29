import pyttsx3
speak_engine = pyttsx3.init()
def speak(sOutput, sName):
    print("{} говорит: ".format(sName) + sOutput )
    speak_engine.say( sOutput )
    speak_engine.runAndWait()
    speak_engine.stop()