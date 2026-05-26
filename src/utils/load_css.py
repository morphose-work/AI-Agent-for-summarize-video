import streamlit as st
import os

def load_css(file_name: str = './src/style.css'):
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    else:
        print(f'Предупреждение: CSS файл {file_name} не найден.')