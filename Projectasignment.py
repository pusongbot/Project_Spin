import random 
import streamlit as st
# Set page configuration
st.set_page_config( page_title="Deep Night Questions", page_icon="🌙", layout="centered" 
)
# Custom CSS for aesthetic night-themed card styling
st.markdown(
     """ <style> 
     .stApp { 
     background-color: #1a1a2e; color: #ffffff;
     } 
     .card-container {
     background: linear-gradient(135deg, #2c2c54, #474787);
     border: 2px solid #706fd3; 
     border-radius: 20px; 
     padding: 40px; 
     text-align: center; 
     box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37); 
     margin-top: 30px; 
     margin-bottom: 30px; 
     min-height: 250px; 
     display: flex; 
     flex-direction: column; 
     justify-content: center; 
     align-items: center; 
     } 
     .card-title { 
     font-size: 1.1rem; 
     letter-spacing: 3px; 
     text-transform: uppercase;
     color: #d1d8e0; 
     margin-bottom: 20px; 
     } 
     .card-question { 
     font-size: 1.5rem; 
     font-weight: 500; 
     color: #ffffff; 
     line-height: 1.4; 
     } 
     .footer-text { 
     text-align: center; 
     color: #84817a; 
     font-size: 0.85rem; 
     margin-top: 50px; 
     } 
     </style> 
     """, 
     unsafe_allow_html=True, 
     )
# Curated question bank for friends
questions = [ 
    "What is the last book you read? Would you recommend it?", 
    "What's something you wish you were really good at?", 
    "What is a core memory with someone in this room that always makes you smile?", 
    "What is a belief you held strongly five years ago that has completely changed?", 
    "If you had a free weekend with no responsibilities or budget limits, how would you spend it?", 
    "What is something small that instantly brightened your day recently?", 
    "What is the most adventurous thing you've ever done, or want to do?", 
    "What quality do you value most in your closest friendships?", 
    "If you could instantly master any skill without trying, what would it be?", 
    "What's a question you've been wanting to ask someone here, but haven't yet?", 
    ]
# Initialize session state to keep track of the current question
if "current_question" not in st.session_state: 
    st.session_state.current_question = ( 
        "Tap the button below to draw your first question" 
        )
# App Header
st.markdown( 
    "<h1 style='text-align: center; color: #f7f1e3;'>Party Questions</h1>", 
    unsafe_allow_html=True,
      ) 
st.markdown( "<p style='text-align: center; color: #aaa69d;'>For Friends & Café Hangouts</p>", 
    unsafe_allow_html=True, 
    )
# Display Question Card
st.markdown(
     f""" 
     <div class="card-container"> 
     <div class="card-title"> For friends </div> 
     <div class="card-question">{st.session_state.current_question}</div> 
     </div> 
     """, 
     unsafe_allow_html=True, 
     )
# Button interaction to draw a random question
col1, col2, col3 = st.columns([1, 2, 1]) 
with col2: 
    if st.button(" Draw Next Question", use_container_width=True): 
       st.session_state.current_question = random.choice(questions) 
       st.rerun()
# Footer
st.markdown( 
    "<div class='footer-text'>Inspired by deepnightquestions.com • Built with Python & Streamlit</div>", 
    unsafe_allow_html=True, 
     )