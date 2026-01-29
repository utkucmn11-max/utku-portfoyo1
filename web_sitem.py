import streamlit as st
from PIL import Image
import os
import base64

# --- SAYFA YAPILANDIRMASI ---
st.set_page_config(page_title="Mehmet Utku Çimen | Portfolyo", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

# --- ZİYARETÇİ SAYACI FONKSİYONLARI ---
counter_file = "ziyaretci_sayisi.txt"

def get_visitor_count():
    if not os.path.exists(counter_file):
        with open(counter_file, "w") as f: f.write("0")
    with open(counter_file, "r") as f: return int(f.read())

def update_visitor_count():
    count = get_visitor_count()
    new_count = count + 1
    with open(counter_file, "w") as f: f.write(str(new_count))
    return new_count

# --- ARKA PLAN GIF OKUMA ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f: data = f.read()
    return base64.b64encode(data).decode()

try:
    bin_str = get_base64_of_bin_file('arkaplan.gif')
    background_css = f"url(data:image/gif;base64,{bin_str})"
except FileNotFoundError:
    background_css = "none"

# --- TASARIM VE EFEKTLER (CSS) ---
st.markdown(f"""
    <style>
    [data-testid="stSidebar"] {{ display: none; }}
    
    .stApp {{
        background-image: {background_css};
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-color: #000000;
    }}

    .stApp::before {{
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.5); backdrop-filter: brightness(0.6); z-index: -1;
    }}

    h1, h2, h3, h4, p, li, span, label, div {{
        color: #ffffff !important;
        text-shadow: 2px 2px 4px #000000;
    }}

    .info-box {{
        background-color: rgba(0, 0, 0, 0.7);
        padding: 20px; border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px; backdrop-filter: blur(10px);
    }}

    .sensor-card {{
        background: rgba(0,0,0,0.8);
        padding: 15px;
        border: 1px solid #ffff00;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(255, 255, 0, 0.2);
