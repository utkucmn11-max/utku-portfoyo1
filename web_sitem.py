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
    try:
        with open(bin_file, 'rb') as f: data = f.read()
        return base64.b64encode(data).decode()
    except: return None

bin_str = get_base64_of_bin_file('arkaplan.gif')
background_css = f"url(data:image/gif;base64,{bin_str})" if bin_str else "none"

# --- DURUM YÖNETİMİ ---
if 'bolt_on' not in st.session_state:
    st.session_state.bolt_on = False

def toggle_bolt():
    st.session_state.bolt_on = not st.session_state.bolt_on

# Enerji durumuna göre neon class'ı
neon_class = "neon-effect" if st.session_state.bolt_on else ""

# Profil RGB Efekti (Orijinal yapıyı bozmamak için sadece CSS üzerinden)
profile_rgb_style = """
    div[data-testid="stImage"] img {
        animation: rgb-anim 3s linear infinite !important;
        border-radius: 20px !important;
    }
""" if st.session_state.bolt_on else "div[data-testid='stImage'] img { border-radius: 20px; }"

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

    /* NEON EFEKTLERİ */
    .neon-effect {{
        border: 2px solid #ffff00 !important;
        box-shadow: 0 0 15px #ffff00, 0 0 30px #ffff00, inset 0 0 10px #ffff00 !important;
    }}

    @keyframes rgb-anim {{
        0% {{ box-shadow: 0 0 20px #ff0000; border: 3px solid #ff0000; }}
        33% {{ box-shadow: 0 0 20px #00ff00; border: 3px solid #00ff00; }}
        66% {{ box-shadow: 0 0 20px #0000ff; border: 3px solid #0000ff; }}
        100% {{ box-shadow: 0 0 20px #ff0000; border: 3px solid #ff0000; }}
    }}

    {profile_rgb_style}

    .sensor-card {{
        background: rgba(0,0,0,0.8);
        padding: 15px;
        border: 1px solid #ffff00;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(255, 255, 0, 0.2);
    }}

    .bolt-container {{ display: flex; justify-content: center; padding: 20px; }}
    .bolt-svg {{ width: 80px; height: 80px; transition: 0.5s; stroke: #444; fill: none; }}
    .bolt-on {{ fill: #ffff00; stroke: #fff; filter: drop-shadow(0 0 20px #ffff00); transform: scale(1.1); }}

    @keyframes float {{
        0% {{ transform: translateY(0px) rotate(0deg); opacity: 0.2; }}
        50% {{ transform: translateY(-25px) rotate(15deg); opacity: 0.5; }}
        100% {{ transform: translateY(0px) rotate(0deg); opacity: 0.2; }}
    }}
    .floating-icon {{
        position: fixed; font-size: 40px;
        animation: float 5s ease-in-out infinite;
        z-index: 0; pointer-events: none;
    }}
    </style>
    
    <div class="floating-icon" style="top: 10%; left: 5%;">🛠️</div>
    <div class="floating-icon" style="top: 20%; right: 10%;">⚡</div>
    <div class="floating-icon" style="top: 70%; left: 15%;">💻</div>
    """, unsafe_allow_html=True)

# --- ÜST BÖLÜM (PROFİL) ---
col1, col2 = st.columns([1, 3])
with col1:
    try:
        st.image("profil.jpg", width=300)
    except:
        st.info("📸 Fotoğraf (profil.jpg) bulunamadı.")

with col2:
    st.title("Mehmet Utku Çimen")
    st.subheader("Elektrik-Elektronik Teknisyeni & Geliştirici")
    st.write("📍 Tekirdağ | 🎂 20 Yaşında | 🎓 Elektrik-Elektronik Mezunu")
    st.write("Merhaba Ben Utku. Elektrik-elektronik lise mezunuyum ve aktif olarak çalışıyorum.")
    st.write("*(Umut; hiç bitmeyen bahar mevsimidir...)*")     
    st.write("**(MEVLANA)**")

st.divider()

# --- ŞİMŞEK ETKİLEŞİMİ ---
bolt_col1, bolt_col2 = st.columns([1, 2])
with bolt_col1:
    bolt_status_class = "bolt-on" if st.session_state.bolt_on else ""
    bolt_color = "#ffff00" if st.session_state.bolt_on else "#444"
    st.markdown(f"""
        <div class="bolt-container">
            <svg class="bolt-svg {bolt_status_class}" viewBox="0 0 24 24">
                <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" fill="{bolt_color}"/>
            </svg>
        </div>
    """, unsafe_allow_html=True)
with bolt_col2:
    st.write("### ⚡ Enerji Testi")
    btn_text = "Enerjiyi Kes" if st.session_state.bolt_on else "Sisteme Enerji Ver"
    st.button(btn_text, on_click=toggle_bolt)

st.divider()

# --- UZMANLIK VE İLETİŞİM ---
c1, c2 = st.columns(2)
with c1:
    st.markdown(f"""<div class="info-box {neon_class}"><h3>🛠️ Uzmanlık Alanları</h3>
    <ul><li>Elektrik Devre Tasarımı</li><li>Elektronik Bakım & Onarım</li>
    <li>Python ile Otomasyon</li><li>3D Printer Model & Baskı</li></ul></div>""", unsafe_allow_html=True)

with c2:
    linkedin_url = "https://www.linkedin.com/in/utkucimen" 
    st.markdown(f"""<div class="info-box {neon_class}"><h3>📫 İletişim</h3>
    <p>📧 <b>E-posta:</b> utkucmn11@gmail.com</p>
    <p>📸 <b>Instagram:</b> @59.utkucimen_</p>
    <p>💼 <b>LinkedIn:</b> Utku Çimen</p>
    </div>""", unsafe_allow_html=True)

# --- TEKNİK REHBER VE DİĞERLERİ ---
st.header("📡 Teknik Rehber")
t1, t2, t3, t4 = st.tabs(["🧲 İndüktif", "🔮 Kapasitif", "👁️ Optik", "📐 Ohm Yasası"])

with t1:
    st.markdown("""<div class="sensor-card">🟤 Kahve: +24V | 🔵 Mavi: 0V | ⚫ Siyah: Sinyal</div>""", unsafe_allow_html=True)

with t4:
    v_input = st.number_input("Gerilim (Volt)", value=220.0, key="v_calc")
    r_input = st.number_input("Direnç (Ohm)", value=10.0, key="r_calc")
    if r_input > 0:
        st.markdown(f"""<div class="sensor-card">Hesaplanan Akım: {v_input/r_input:.2f} Amper</div>""", unsafe_allow_html=True)

# --- PROJELER, MÜZİK VE HOBİLER ---
st.divider()
st.write("### 🎵 Favori Parçam")
st.write("(AC-DC) BACK-İN-BLACK ")

if os.path.exists("sarki.mp3"):
    st.audio("sarki.mp3", format="audio/mp3")

st.write("### 🎮 Hobiler")
st.write("Müzik Dinlemek | Yürüyüş Yapmak | Oyun Oynamak")

# --- ZİYARETÇİ SAYACI ---
st.divider()
v_count = get_visitor_count()
if 'visited' not in st.session_state:
    st.session_state['visited'] = True
    v_count = update_visitor_count()

st.metric(label="👤 Toplam Profil Ziyareti", value=v_count)
st.caption("© 2026 Mehmet Utku Çimen")
