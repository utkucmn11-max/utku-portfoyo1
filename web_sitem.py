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

# --- DURUM YÖNETİMİ ---
if 'bolt_on' not in st.session_state:
    st.session_state.bolt_on = False
if 'bg_animated' not in st.session_state:
    st.session_state.bg_animated = True

def toggle_bolt():
    st.session_state.bolt_on = not st.session_state.bolt_on

def toggle_bg():
    st.session_state.bg_animated = not st.session_state.bg_animated

# --- ARKA PLAN GIF OKUMA ---
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f: data = f.read()
        return base64.b64encode(data).decode()
    except: return None

bin_str = get_base64_of_bin_file('arkaplan.gif')
if st.session_state.bg_animated and bin_str:
    background_css = f"url(data:image/gif;base64,{bin_str})"
else:
    background_css = "none"

# Enerji durumuna göre neon class'ları
neon_class = "neon-effect" if st.session_state.bolt_on else ""
profile_rgb_style = """
    div[data-testid="stImage"] img {
        animation: rgb-anim 3s linear infinite !important;
        border-radius: 20px !important;
        border: 3px solid transparent;
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

    /* BUTONLARI UFALTAN CSS */
    div.stButton > button {{
        padding: 5px 15px !important;
        font-size: 14px !important;
        height: auto !important;
        width: auto !important;
        min-width: 150px;
        border-radius: 8px !important;
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
        transition: 0.5s ease-in-out;
    }}

    .neon-effect {{
        border: 2px solid #ffff00 !important;
        box-shadow: 0 0 15px #ffff00, 0 0 30px #ffff00, inset 0 0 10px #ffff00 !important;
    }}

    @keyframes rgb-anim {{
        0% {{ box-shadow: 0 0 20px #ff0000; border-color: #ff0000; }}
        33% {{ box-shadow: 0 0 20px #00ff00; border-color: #00ff00; }}
        66% {{ box-shadow: 0 0 20px #0000ff; border-color: #0000ff; }}
        100% {{ box-shadow: 0 0 20px #ff0000; border-color: #ff0000; }}
    }}

    {profile_rgb_style}

    .bolt-container {{ display: flex; justify-content: center; padding: 10px; }}
    .bolt-svg {{ width: 60px; height: 60px; transition: 0.5s; stroke: #444; fill: none; }}
    .bolt-on {{ fill: #ffff00; stroke: #fff; filter: drop-shadow(0 0 20px #ffff00); transform: scale(1.1); }}

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
    </style>
    """, unsafe_allow_html=True)

# --- ÜST BÖLÜM (PROFİL) ---
col1, col2 = st.columns([1, 3])
with col1:
    try:
        st.image("profil.jpg", width=300)
    except:
        st.info("📸 profil.jpg bulunamadı.")

with col2:
    st.title("Mehmet Utku Çimen")
    st.subheader("Elektrik-Elektronik Teknisyeni & Geliştirici")
    st.write("📍 Tekirdağ | 🎂 20 Yaşında | 🎓 Elektrik-Elektronik Mezunu")
    st.write("Merhaba Ben Utku. Elektrik-elektronik lise mezunuyum ve aktif olarak çalışıyorum. Python dünyasında kendimi geliştiriyorum.")
    st.write("*(Umut; hiç bitmeyen bahar mevsimidir. İçine kar da yağar, fırtına da kopar ama çiçekler hep açar.)*")     
    st.write("**(MEVLANA)**")

st.divider()

# --- KONTROL PANELİ ---
col_ctrl1, col_ctrl2 = st.columns(2)
with col_ctrl1:
    st.write("### ⚡ Enerji")
    btn_text = "Enerjiyi Kes" if st.session_state.bolt_on else "Enerji Ver"
    st.button(btn_text, on_click=toggle_bolt)
    bolt_color = "#ffff00" if st.session_state.bolt_on else "#444"
    st.markdown(f'<div class="bolt-container"><svg class="bolt-svg {"bolt-on" if st.session_state.bolt_on else ""}" viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" fill="{bolt_color}"/></svg></div>', unsafe_allow_html=True)

with col_ctrl2:
    st.write("### 🖼️ Arka Plan")
    bg_btn_text = "GIF'i Durdur" if st.session_state.bg_animated else "GIF'i Başlat"
    st.button(bg_btn_text, on_click=toggle_bg)
    st.write("Durum: " + ("🟢 Hareketli" if st.session_state.bg_animated else "🔴 Sabit"))

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
    <p>📸 <b>Instagram:</b> <a href="https://www.instagram.com/59.utkucimen_/" target="_blank" style="color:#ffff00; text-decoration:none;">@59.utkucimen_</a></p>
    <p>💼 <b>LinkedIn:</b> <a href="{linkedin_url}" target="_blank" style="color:#ffff00; text-decoration:none;">Utku Çimen</a></p>
    </div>""", unsafe_allow_html=True)

# --- TEKNİK REHBER ---
st.header("📡 Teknik Rehber")
t1, t2, t3, t4 = st.tabs(["🧲 İndüktif", "🔮 Kapasitif", "👁️ Optik", "📐 Ohm Yasası"])

with t1:
    st.markdown("""<div class="sensor-card"><span class="sensor-text">🟤 Kahve: +24V | 🔵 Mavi: 0V | ⚫ Siyah: Sinyal</span></div>""", unsafe_allow_html=True)
with t2:
    st.markdown("""<div class="sensor-card"><span class="sensor-text">🟤 Kahve: +24V | 🔵 Mavi: 0V | ⚫ Siyah: Sinyal</span></div>""", unsafe_allow_html=True)
with t3:
    st.markdown("""<div class="sensor-card"><span class="sensor-text">🟤 Kahve: +24V | 🔵 Mavi: 0V | ⚫ Siyah: NO | ⚪ Beyaz: NC</span></div>""", unsafe_allow_html=True)
with t4:
    v_in = st.number_input("Gerilim (V)", value=220.0, key="v_calc")
    r_in = st.number_input("Direnç (Ω)", value=10.0, key="r_calc")
    if r_in > 0:
        st.markdown(f'<div class="sensor-card"><span class="sensor-text">Hesaplanan Akım: {v_in/r_in:.2f} Amper</span></div>', unsafe_allow_html=True)

# --- PROJELER ---
st.divider()
st.header("💻 Projelerim")
with st.expander("🚀 Devam Eden Çalışmalar", expanded=True):
    st.write("Python tabanlı otomasyon sistemleri üzerine odaklanıyorum.")



st.write("### 🎮 Hobiler")
st.write("Müzik Dinlemek | Yürüyüş Yapmak | Oyun Oynamak")

# --- ZİYARETÇİ SAYACI ---
st.divider()
v_count = get_visitor_count()
if 'visited' not in st.session_state:
    st.session_state['visited'] = True
    v_count = update_visitor_count()
st.metric(label="👤 Ziyaret", value=v_count)
st.caption("© 2026 Mehmet Utku Çimen")

