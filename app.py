import streamlit as st
from excuse import *

#heade
st.header('Ultimate Excuse Generator')
st.markdown('Dumb teacher? Make a funny excuse. Ridiculously intellegent parent? Figure out how to shrug it off. If you did anything wrong, the answer is here!')

api_key = st.text_input("API Key")

#colums
col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)

# inputs
person = col1.text_input("Person (their job, age, etc.)", "My evil 70 y.o. teacher")
intellegence = col2.text_input("Approximate IQ", "80-90")
cause = col3.text_input("What you did wrong", "stole 5 bucks")
procedure = col4.text_input("What to do", "Slip out of the situation")
p_info = col5.text_input("a bit about you", "approx. age, in school or at job, etc")

#space
st.text(' ')

# Generate button
generate_button = st.button("Create Excuses!", type='primary')

#space
st.text(' ')

if generate_button:
    excuse = create_excuses(person, intellegence, cause, procedure, p_info, api_key)

    conversation_text = excuse.candidates[0].content.parts[0].text
    st.markdown(conversation_text)
