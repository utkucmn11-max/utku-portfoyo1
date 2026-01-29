import streamlit as st
from PIL import Image
import os
import base64

# Sayfa Yapılandırması
st.set_page_config(page_title="Mehmet Utku Çimen | Portfolyo", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

# --- ZİYARETÇİ SAYACI FONKSİYONLARI ---
counter_file = "ziyaretci_sayisi.txt"

def get_visitor_count():
    if not os.path.exists(counter_file):
        with open(counter_file, "w") as f:
            f.write("0")
    with open(counter_file, "r") as f:
        return int(f.read())

def update_visitor_count():
    count = get_visitor_count()
    new_count = count + 1
    with open(counter_file, "w") as f:
        f.write(str(new_count))
    return new_count

# --- YEREL GIF DOSYASINI OKUMA FONKSİYONU ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# --- HATA DÜZELTİLEN BÖLÜM (39. SATIR CİVARI) ---
try:
    if os.path.exists('arkaplan.gif'):
        bin_str = get_base64_of_bin_file('arkaplan.gif')
        background_css = f"url(data:image/gif;base64,{bin_str})"
    else:
        background_css = "none"
except Exception:
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
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        backdrop-filter: brightness(0.6);
        z-index: -1;
    }}

    h1, h2, h3, h4, p, li, span, label, div {{
        color: #ffffff !important;
        text-shadow: 2px 2px 4px #000000;
    }}

    .info-box {{
        background-color: rgba(0, 0, 0, 0.7);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }}

    .sensor-card {{
        background: rgba(0,0,0,0.8);
        padding: 15px;
        border: 1px solid #ffff00;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(255, 255, 0, 0.2);
    }}
    .sensor-text {{
        color: #ffff00 !important;
        font-weight: bold;
        text-shadow: 1px 1px 2px #000000;
        font-size: 1.1em;
    }}

    @keyframes float {{
        0% {{ transform: translateY(0px) rotate(0deg); opacity: 0.2; }}
        50% {{ transform: translateY(-25px) rotate(15deg); opacity: 0.5; }}
        100% {{ transform: translateY(0px) rotate(0deg); opacity: 0.2; }}
    }}
    .floating-icon {{
        position: fixed;
        font-size: 40px;
        animation: float 5s ease-in-out infinite;
        z-index: 0;
        pointer-events: none;
    }}
    </style>
    
    <div class="floating-icon" style="top: 10%; left: 5%;">🛠️</div>
    <div class="floating-icon" style="top: 20%; right: 10%;">⚡</div>
    <div class="floating-icon" style="top: 70%; left: 15%;">💻</div>
    """, unsafe_allow_html=True)

# --- İÇERİK BÖLÜMLERİ ---
col1, col2 = st.columns([1, 3])

with col1:
    try:
        img = Image.open("profil.jpg")
        st.image(img, width=300)
    except:
        st.info("
