import streamlit as st
import sys
import os

# Garante que a pasta do projeto está no caminho do Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from telasUI.menuUI import menu

st.set_page_config(page_title="YTTrack", layout="wide")

menu()
