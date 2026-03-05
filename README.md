# LLM2LLM: The Autonomous Physics Discovery Engine

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Gemini API](https://img.shields.io/badge/Gemini-API-orange.svg)](https://ai.google.dev/)

**LLM2LLM** is an experimental framework designed to set up autonomous philosophical and scientific dialogues between two distinct AI personas powered by Google's Gemini models. 

In this repository, we simulate a conversation between the **visionary CEO** and the **technically-grounded CTO** of a fictional DeepMind-like company. Their shared objective? To figure out how to build an AI that can autonomously derive the fundamental laws of physics from a tabula rasa state.

## 🌟 Features

- **Multi-Agent Simulation**: Pit two distinct system instructions against each other to foster debate and collaboration.
- **Automated Turn-Taking**: A continuous conversational loop where Agent A's output acts as Agent B's prompt, and vice-versa.
- **Robust Error Handling**: Built-in retry logic that automatically paces the conversation and handles `429 Quota Exhausted` errors gracefully for users on the Google AI Studio free tier.
- **Transcript Logging**: Automatically saves the fascinating insights, debates, and theories generated during the conversation to a local `conversation_transcript.txt` log, neatly date-stamped.

## 🚀 Getting Started

### 1. Prerequisites

You will need a free API key from Google AI Studio to run the Gemini models.
*   Get your API key here: [Google AI Studio](https://aistudio.google.com/app/apikey)

### 2. Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/Quantumplations/LLM2LLM.git
cd LLM2LLM
pip install -r requirements.txt
```

### 3. Configuration

Create your local environment file:

1. Rename the provided `.env.example` file to `.env`.
2. Open `.env` and paste your Gemini API key:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

*(Note: The `.env` file is included in `.gitignore` to protect your API key from accidental commits).*

### 4. Running the Simulation

Kick off the conversation by executing the main script:

```bash
python main.py
```

Sit back and watch Alice and Bob debate the fundamental nature of reality right in your terminal! 

## 🧠 Changing the Conversation 

Want them to argue about something else? 
Simply open `main.py` and modify:
1. `alice_config`'s `system_instruction` to change Agent A's persona.
2. `bob_config`'s `system_instruction` to change Agent B's persona.
3. The initial `prompt` variable to kickstart a new topic of debate!
