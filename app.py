import streamlit as st

st.set_page_config(
    page_title="Webpage",
    page_icon="⛹🏻",
    layout="wide",
)

st.title("My Biography 🏀 ")

with st.container():
    st.header("HI I'm Rj Rivera 🙌")
    st.subheader("A BSCpE Student In SURIGAO DEL NORTE STATE UNIVERSITY ")

with st.container():
    st.markdown("<h1 style='text-align: right;'>Homepage</h1>", unsafe_allow_html=True)
    st.markdown("------")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("""
        I am Rj Rivera, 21 years old, living in P8 Brgy. Cagniog Surigao City. 
        I have many hobbies, and basketball is one of the hobbies I have. 
        Basketball is a sport that requires personal skill, teamwork, and speed.
        Basketball is a great sport; I enjoy it every time when I crossover the opponent and then I score. 
        Teamwork is one of the important keys for playing basketball. A good basketball team always does some great teamwork. 
        It is wonderful when we do some fake moves to make the opponent jump, and then we pass the ball to our teammate. 
        I like to play basketball outside with my friend; we always have a good time together. 
        Basketball makes me feel great and satisfied. Basketball is like my friend. Without basketball, I will lose a lot of fun in my life. 
        Playing basketball is like studying for the test; if you don't play hard, you may lose the game. 
        Basketball means a lot to me; I feel at ease and relaxed when playing basketball with my friend. 
        There is no limit for a basketball game; you can do anything you can to win the game except for faults. 
        Sometimes, we lose the game, and we will discuss our weaknesses together because we all believe the next time we can play better.
        """)


 

st.header(":mailbox: Get In Touch With Me!")

contact_form = """
<form action="https://formsubmit.co/rrivera3@ssct.edu.ph" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="your name" required>
    <input type="email" name="email" placeholder="your email" required>
    <textarea name="message" placeholder="your message here"></textarea>
    <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("pages/style/style.css")
  
with st.container():
    st.write("---")
 



