import streamlit as st
from PIL import Image
import os
import base64
import time

# 1. SAYFA YAPILANDIRMASI
st.set_page_config(page_title="Mehmet Utku Çimen | Portfolyo", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

# --- GELİŞMİŞ ZİYARETÇİ SAYACI (F5 KORUMALI) ---
counter_file = "ziyaretci_sayisi.txt"

def get_visitor_count():
    if not os.path.exists(counter_file):
        with open(counter_file, "w") as f: f.write("0")
    with open(counter_file, "r") as f:
        try: return int(f.read())
        except: return 0

def update_visitor_count():
    count = get_visitor_count()
    new_count = count + 1
    with open(counter_file, "w") as f: f.write(str(new_count))
    return new_count

# Tarayıcı bazlı basit bir kilit mekanizması
if 'already_counted' not in st.session_state:
    # İlk kez geliyorsa sayıyı artır
    v_count = update_visitor_count()
    st.session_state['already_counted'] = True
    # Son sayılan zamanı tut (isteğe bağlı gelişim için)
    st.session_state['last_visit'] = time.time()
else:
    # Sayfa yenilense bile session_state silinmediği için buraya girer ve artırmaz
    v_count = get_visitor_count()

# --- YEREL GIF OKUMA ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

try:
    bin_str = get_base64_of_bin_file('arkaplan.gif')
    background_css = f"url(data:image/gif;base64,{bin_str})"
except:
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
    h1, h2, h3, h4, p, li, span, label, div {{ color: #ffffff !important; text-shadow: 2px 2px 4px #000000; }}
    .info-box {{
        background-color: rgba(0, 0, 0, 0.7); padding: 20px; border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1); margin-bottom: 20px; backdrop-filter: blur(10px);
    }}
    @keyframes float {{
        0% {{ transform: translateY(0px) rotate(0deg); opacity: 0.2; }}
        50% {{ transform: translateY(-25px) rotate(15deg); opacity: 0.5; }}
        100% {{ transform: translateY(0px) rotate(0deg); opacity: 0.2; }}
    }}
    .floating-icon {{ position: fixed; font-size: 40px; animation: float 5s ease-in-out infinite; z-index: 0; pointer-events: none; }}
    </style>
    <div class="floating-icon" style="top: 10%; left: 5%;">🛠️</div>
    <div class="floating-icon" style="top: 20%; right: 10%;">⚡</div>
    <div class="floating-icon" style="top: 70%; left: 15%;">💻</div>
    <div class="floating-icon" style="top: 80%; right: 5%;">🔧</div>
    """, unsafe_allow_html=True)

# --- İÇERİK ---
col1, col2 = st.columns([1, 3])
with col1:
    try:
        st.image(Image.open("profil.jpg"), width=300)
    except:
        st.info("📸 Fotoğraf bulunamadı.")

with col2:
    st.title("Mehmet Utku Çimen")
    st.subheader("Elektrik-Elektronik Teknisyeni & Geliştirici")
    st.write("📍 Tekirdağ | 🎂 20 Yaşında")
    st.write("Merhaba! Ben Utku. Elektrik-elektronik uzmanlığımı Python ile birleştiriyorum.")
    st.write("*(Umut; hiç bitmeyen bahar mevsimidir...)*")

st.divider()

c1, c2 = st.columns(2)
with c1:
    st.markdown("""<div class="info-box"><h3>🛠️ Uzmanlık Alanları</h3>
    <ul><li>Elektrik Devre Tasarımı</li><li>Python ile Otomasyon</li></ul></div>""", unsafe_allow_html=True)

with c2:
    st.markdown(f"""<div class="info-box"><h3>📫 İletişim</h3>
    <p>📧 utkucmn11@gmail.com</p>
    <p>📸 <a href="https://www.instagram.com/59.utkucimen_/" style="color:#ffff00; text-decoration:none;">@59.utkucimen_</a></p>
    </div>""", unsafe_allow_html=True)

# --- SES DOSYASI ---
current_dir = os.path.dirname(os.path.abspath(__file__))
for root, dirs, files in os.walk(current_dir):
    if "sarki.mp3" in files:
        with open(os.path.join(root, "sarki.mp3"), "rb") as f:
            st.audio(f.read(), format="audio/mp3")
        break

st.divider()

# --- SAYAÇ GÖSTERİMİ ---
st.metric(label="👤 Profil Ziyaret Sayısı", value=v_count)
st.caption("© 2026 Mehmet Utku Çimen")
