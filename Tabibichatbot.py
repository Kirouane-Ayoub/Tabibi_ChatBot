import streamlit as st
from lib.custom import * 
from PIL import Image
img = Image.open("icon.png")
st.set_page_config(page_title='Tabibi Chatbot',page_icon = img)
st.sidebar.image("icon.png" , width=80)
st.header(":hand: Welcome To Tabibi Chatbot : ")
st.info("Tabibi Chat-bot is an advanced medical chatbot that seamlessly integrates memory capabilities, ensuring personalized and context-aware interactions. With the added dimension of voice output, Tabibi offers a holistic healthcare experience, enabling users to engage in natural conversations while benefiting from its extensive medical knowledge and tailored recommendations.")
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "Hi my name is Tabibi chatbot , how can i help you today ? "}]
st.sidebar.button(':arrow_right: Clear Chat History :arrow_left: ', on_click=clear_chat_history)
use_audio = st.sidebar.checkbox("Use audio output")
st.sidebar.write(":white_check_mark: based on ReAct paper by Google Research: https://arxiv.org/abs/2210.03629")

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Hi my name is Tabibi chatbot , how can i help you today ? "}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = run(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    if use_audio : 
        audiof(full_response)
    st.session_state.messages.append(message)