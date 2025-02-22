import streamlit as st
from googletrans import Translator
from languages import *

# Page Routing
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["Home"])[0]

# Home Page
if page == "Home":
    st.markdown("""
        <h1 style='text-align: center; color: #1e88e5;'>Welcome to Shiksha Translate </h1>
        <p style='text-align: center;'>Language should never be a barrier to learning, and with our platform, students can seamlessly convert educational content into their local languages.
                 Whether it’s textbooks, research papers, or online courses, we ensure that knowledge reaches everyone in a language they understand best.
                 By bridging the gap between diverse linguistic backgrounds, we empower learners to grasp complex concepts effortlessly. 
                With Shiksha Translate, education becomes truly universal—because learning is for everyone! 🚀</p>
    """, unsafe_allow_html=True)
    
   

    
    st.markdown("""
        <style>
            .center-button { 
                display: flex; 
                justify-content: center; 
                align-items: center; 
                margin-top: 20px;
            }
            .stButton button {
                background-color: #1e88e5;
                color: white;
                border-radius: 5px;
                padding: 10px 20px;
                border: none;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            .stButton button:hover {
                background-color: #1565c0;
            }
            .stButton button:active {
                background-color: #0d47a1;
            }
        </style>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Go to Translator", key="go_translator", use_container_width=False):
            st.experimental_set_query_params(page="Translator")

# Translator Page
elif page == "Translator":
    st.markdown("""
        <style>
            .stButton button {
                background-color: #1e88e5;
                color: white;
                border-radius: 5px;
                padding: 5px 15px;
                border: none;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            .stButton button:hover {
                background-color: #1565c0;
            }
            .stButton button:active {
                background-color: #0d47a1;
            }
        </style>
    """, unsafe_allow_html=True)
    
    if st.button("⬅ Back", key="back_home", use_container_width=False):
        st.experimental_set_query_params(page="Home")
    
    st.markdown("<h1 class='stTitle'>🌍 Language Translator</h1>", unsafe_allow_html=True)
    
    source_text = st.text_area("✏️ Enter text to translate:")
    target_language = st.selectbox("🌎 Select target language:", languages)
    
    if st.button("Translate", key="translate_button", use_container_width=False):
        if source_text:
            translator = Translator()
            out = translator.translate(source_text, dest=target_language)
            st.markdown("### ✅ Translated Text:")
            st.success(out.text)

# About Page
elif page == "About":
    st.markdown("""
        <h1 style='text-align: center; color: #1e88e5;'>About This App</h1>
        <p>This application is built using Streamlit and Google Translate API. It allows users to translate text into different languages with a simple and user-friendly interface.</p>
    """, unsafe_allow_html=True)
