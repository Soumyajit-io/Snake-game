import time
import speech_recognition as sr
from agent import snkagent
is_awake = False
listening = False
stop_listening = None

r = sr.Recognizer()

mic = sr.Microphone()

def callback(recognizer, audio):
   global is_awake, listening

   try:
      text = recognizer.recognize_google(audio).lower()
      print("Heard:", text)
      if not is_awake:
            if "hello" in text:
               print("Wake word detected")
               listening = True
               is_awake = True
            return
      print("User command:", text)
      listening =False
      snkagent("user query: " + text, user_input=True)
      is_awake = False
   except:
      pass

def start_voice():
   global stop_listening
   with mic as source:
      r.adjust_for_ambient_noise(source)
   stop_listening = r.listen_in_background(mic,callback)
   print("Voice started")

def stop_voice():
   global stop_listening
   if stop_listening:
        stop_listening(wait_for_stop=False)

            
            