import streamlit as st
from langchain_groq import ChatGroq

st.set_page_config(page_title='personal AI Chat',layout='centered')

st.title('🤖 The Groq Chatbot')
st.write('A fully integrated,memory-enabled AI Assistant.')

#sidebar(api security)
with st.sidebar:
  st.header('⚙️ Configuration')
  user_api_key=st.text_input('enter the Groq API KEY:',type='password')
  st.info('your api key is required to wakeup the AI brain')

if 'messages' not in st.session_state:
  st.session_state.messages=[]

#---Display history-----
for msg in st.session_state.messages:
  with st.chat_message(msg['role']):
    st.markdown(msg['content'])

#chat input and input
if user_query:=st.chat_input('ask somethings!!!!!!!!!!!!!!!!!!!'):
  if not user_api_key:
    st.error('enter api key first to use the machine!!!!!')
  else:
    with st.chat_message('user'):
      st.markdown(user_query)

    #store this message to the vault
    st.session_state.messages.append({'role':'user', 'content': user_query}) 


    #chatbot
    llm=ChatGroq(
        model='openai/gpt-oss-20b',
        temperature=0.5,
        api_key=user_api_key
    ) 

    with st.spinner('Ai is thinking'):
      response=llm.invoke(st.session_state.messages)
      bot_answer=response.content

    st.session_state.messages.append({'role':'assistant','content':bot_answer}) 
    with st.chat_message('assistant'):
      st.markdown(bot_answer) 


    

