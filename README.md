# Tabibi ChatBot

## Overview 

**Tabibi Chat-bot** is an advanced medical chatbot that seamlessly integrates memory capabilities, ensuring personalized and context-aware interactions. With the added dimension of voice output, Tabibi offers a holistic healthcare experience, enabling users to engage in natural conversations while benefiting from its extensive medical knowledge and tailored recommendations.

## ReAct: Synergizing Reasoning and Acting in Language Models 
ReAct is a framework that synergizes reasoning and acting in language models. It does this by prompting LLMs to generate both verbal reasoning traces and actions pertaining to a task in an interleaved manner. This allows the model to perform dynamic reasoning to create, maintain, and adjust high-level plans for acting (reason to act), while also interacting with the external environments (e.g. Wikipedia) to incorporate additional information into reasoning (act to reason).**https://arxiv.org/abs/2210.03629**

## Tools and Frameworks
+ **Streamlit**: For an interactive and user-friendly interface, we've incorporated Streamlit. This web app framework simplifies the presentation of our assistant, making it accessible and engaging for users.
* **Langchain**: We've implemented Langchain for the chat functionality, enabling smooth interactions with the assistant.
* **ElevenLabs Text-to-Speech API**: The official Python API for ElevenLabs text-to-speech software is utilized to provide audio output capabilities. This integration brings lifelike and expressive voices to the assistant, enhancing the accessibility of information.
+ **GPT-4** : is a large language model (LLM) developed by OpenAI. It is the fourth generation of the GPT family of models, and it is significantly larger and more powerful than its predecessors. GPT-4 has 175 billion parameters, which is more than 10 times the number of parameters in GPT-3. 

## Usage
```
pip install -r requirements.txt
streamlit run Tabibichatbot.py
```
[vokoscreenNG-2023-09-11_20-07-18.webm](https://github.com/Tuning-AI/Tabibi_ChatBot/assets/145156896/e0e2622c-2480-46bd-bf6b-9d200cd4870a)
