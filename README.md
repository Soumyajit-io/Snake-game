# 🐍 LLM-Powered Snake Game (Pygame)

An interactive Snake (named "Nada") game built with **Python and Pygame**, enhanced with a locally running **LLM-powered voice agent**.

This project combines real-time game development with asynchronous AI integration, enabling a talking snake that reacts to in-game events and user voice commands in real time.

---

## 🎮  Game Controls 

- For movement use A,D,W,S keys
- For sprinting use Space key
- To call Nada, say "Hello"

---


## 🎮 Core Game Features

- Smooth and responsive movement
- Sprint mechanic with speed control
- Randomized food spawning
- Dynamic snake growth
- Collision detection (self + boundary)
- Real-time score tracking
- Sound effects and background music
- Clean UI with dynamic caption rendering

---

## 🤖 AI Agent Features

- Locally running open-source LLM
- Personality-driven character (Nada)
- Context-aware responses to game events
- Voice-based interaction with wake-word activation
- Asynchronous microphone listening
- Thread-safe LLM invocation
- Real-time TTS voice output
- Dynamic on-screen caption system

---

## 🧠 Architecture Highlights

- Event-driven design
- Separation of concerns (Game / Voice / Agent modules)
- Non-blocking async voice perception (`listen_in_background`)
- Background thread management
- Clean startup and shutdown lifecycle handling
- Prompt-controlled personality and response constraints

This project demonstrates integration of AI systems into a real-time interactive environment.

---

## 🛠️ Tech Stack

- Python
- Pygame
- LangChain
- Ollama (Local LLM runtime)
- SpeechRecognition
- gTTS (Text-to-Speech)
- Threading & Asynchronous Callbacks


---

## ▶️ How to Run (without llm)

### 1. Clone the repository
### 2. Create VENV and Install dependencies:
   - python -m venv .venv
   - .venv\Scripts\activate
   - pip install -r requirements.txt
### 3. Run the game: 
   - python main2.py
---

## ▶️ How to Run (with llm)

### 1. Clone the repository
### 2. Download ollama:
-[ollama](https://ollama.com/)
### 3. Download LLM:
- In terminal, run : ollama run llama3.2

### 4. Create VENV and Install dependencies:
   - python -m venv .venv
   - .venv\Scripts\activate
   - pip install -r requirements.txt
### 5. Run the game: 
- python main.py

---

## 👨‍💻 Author

**Soumyajit Sadhukhan**  
B.Tech CSE




