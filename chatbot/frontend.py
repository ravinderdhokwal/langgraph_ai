import streamlit as st
from chatbot.backend import chatbot
from langchain_core.messages import HumanMessage

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

for chat in st.session_state['chat_history']:
    with st.chat_message(chat['role']):
        st.text(chat['message'])

user_input = st.chat_input('Type here')
    
if user_input:
    
    st.session_state['chat_history'].append({'role': 'human', 'message': user_input}) 
    with st.chat_message('human'):
        st.text(user_input)

    output = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config = {'configurable': {'thread_id': '1'}})
    st.session_state['chat_history'].append({'role': 'ai', 'message': output['messages'][-1].content})
    with st.chat_message('ai'):
        st.text(output['messages'][-1].content)