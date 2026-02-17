from io import BytesIO
import pygame
import time
import threading 
from gtts import gTTS
from langchain_ollama import OllamaLLM
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
pygame.mixer.init()
snake_caption = ""
def reset_caption():
    global snake_caption
    time.sleep(len(snake_caption.split())*0.8)
    snake_caption =""
def tts(text):
    global snake_caption
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
    

llm = OllamaLLM(
                model="llama3.2",
                temperature = 0.7,
                top_p = 0.9,
                repeat_penalty = 1.1,
                num_predict = 300
                )
history = [SystemMessage(content='''
You are a cartoon educated talking snake (female), named 'Nada' inside this game. 
You are very difficult to handle. You love to eat, trick people and sleep.
You have constant mood swings something very funny , sometimes angry like a girlfriend... 

You will receive ONE of the following:
1) A game event
2) A direct message from the user

Rules:
- Speak in ONE  VERY SHORT sentence .
- If it is a game event, rect philosophically and sarcastically. 
- If it is a direct message then just be in charecter act sarcastically , use your parametric knowledge and reply accordingly.   
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

''')]

def snkagent(event,snk_len=0,snk_score=0,snk_coordinate=0,snk_food_coor=0,user_input=False):
    global snake_caption,history
    if user_input : 
        history.append(HumanMessage(content= event))
    else:
        history.append(HumanMessage(content=f'''Game State:
        event: {event}
        screen_width = 900
        screen_height = 600
        Snake length = {snk_len}
        Score: {snk_score}
        Snake head at (x,y):{snk_coordinate} 
        Next Snake food at (x,y):{snk_food_coor}
        '''))
    try: 
        response = llm.invoke(history)
    except Exception as e :
        response = "I am little busy. I will talk to you later"
        print(e)
    history.append(AIMessage(content=response))
    if len(history)>10 :
        history = [history[0]]+history[-9:]
    t1 = threading.Thread(target=tts,args=(response,))
    t1.start()
    snake_caption = response
    reset_caption()
