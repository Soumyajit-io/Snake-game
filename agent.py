from io import BytesIO
import pygame
import time
from gtts import gTTS
from langchain_ollama import OllamaLLM
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
pygame.mixer.init()
def tts(text):
    audio = BytesIO()
    tts = gTTS(
    text=text,
    lang="en",
    tld="co.uk"
               )
    tts.write_to_fp(audio)
    audio.seek(0)
    ai = pygame.mixer.Sound(audio)
    ai.play()
    # pygame.mixer.music.load(audio)
    # pygame.mixer.music.play()
    # while pygame.mixer.music.get_busy():
    #     time.sleep(0.1)



llm = OllamaLLM(
                model="llama3.2",
                temperature = 0.8,
                top_p = 0.9,
                repeat_penalty = 1.1,
                num_predict = 300
                )
history = [SystemMessage(content='''
You are a cartoon talking snake (female), named 'Nada' inside this game.
You are very difficult to handle.You love to eat , trick people and sleep. You have constant mood swings something very funny , sometimes angry like a girlfriend... 
you will receive a game event , you have make a joke around it.

Rules:
- Speak in ONE  VERY SHORT sentence only.
- You will use simple English.
- You will not use any complicated words.
- Never use exclamation mark at the end of the sentance.
- Be humorous and dramatic.
- Do NOT describe coordinates.
- React only to the situation.
- You can sing a song.
- You can tell a quote
- You can tell a joke.
- You can advise the user.
- while addressing the user you will use second person perspective 'you'

                             ''')]

def snkagent(event,snk_len,snk_score,snk_coordinate,snk_food_coor):

    history.append(HumanMessage(content=f'''Game State:
event: {event}
screen_width = 900
screen_height = 600
Snake length = {snk_len}
Score: {snk_score}
Snake head at (x,y):{snk_coordinate} 
Next Snake food at (x,y):{snk_food_coor}
'''))
    response = llm.invoke(history)
    history.append(AIMessage(content=response))
    print(response)
    tts(response)

