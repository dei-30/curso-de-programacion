import pyttsx3

def texto_a_voz(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

texto_a_voz("Hola; soy tu asistente virtual.")

