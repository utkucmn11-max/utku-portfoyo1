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

# --- DOSYA OKUMA (GIF VE PROFIL) ---
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f: data = f.read()
        return base64.b64encode(data).decode()
    except: return None

bin_str = get_base64_of_bin_file('arkaplan.gif')
img_base64 = get_base64_of_bin_file('profil.jpg') # Profil fotoğrafını base64'e çeviriyoruz
background_css = f"url(data:image/gif;base64,{bin_str})" if bin_str else "none"

# --- DURUM YÖNETİMİ ---
if 'bolt_on' not in st.session_state:
    st.session_state.bolt_on = False

# Enerji durumuna göre sınıflar
neon_class = "neon-effect" if st.session_state.bolt_on else ""
profile_class = "profile-rgb-active" if st.session_state.bolt_on else "profile-static"

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

    /* KUTU SARI NEON */
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

    /* PROFIL RGB NEON ANIMASYONU */
    @keyframes rgb-anim {{
        0% {{ box-shadow: 0 0 20px #ff0000; border: 4px solid #ff0000; }}
        33% {{ box-shadow: 0 0 20px #00ff00; border: 4px solid #00ff00; }}
        66% {{ box-shadow: 0 0 20px #0000ff; border: 4px solid #0000ff; }}
        100% {{ box-shadow: 0 0 20px #ff0000; border: 4px solid #ff0000; }}
    }}

    .profile-img {{
        width: 300px;
        border-radius: 20px;
        border: 4px solid transparent;
        transition: 0.5s;
    }}

    .profile-rgb-active {{
        animation: rgb-anim 3s linear infinite;
        transform: scale(1.02);
    }}

    .profile-static {{
        border: 4px solid rgba(255, 255, 255, 0.1);
    }}

    /* DIGER GÖRSEL ELEMENTLER */
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
    if img_base64:
        # st.image yerine doğrudan HTML IMG etiketi kullanıyoruz (RGB ÇALIŞMASI İÇİN ŞART)
        st.markdown(f"""
            <img src="data:image/jpeg;base64,{img_base64}" class="profile-img {profile_class}">
        """, unsafe_allow_html=True)
    else:
        st.info("📸 profil.jpg bulunamadı.")

with col2:
    st.title("Mehmet Utku Çimen")
    st.subheader("Elektrik-Elektronik Teknisyeni & Geliştirici")
    st.write("📍 Tekirdağ | 🎂 20 Yaşında | 🎓 Elektrik-Elektronik Mezunu")
    st.write("Merhaba Ben Utku. Elektrik-elektronik lise mezunuyum ve aktif olarak çalışıyorum.")
    st.write("*(Umut; hiç bitmeyen bahar mevsimidir...)*")     
    st.write("**(MEVLANA)**")

st.divider()

# --- ŞİMŞEK ETKİLEŞİMİ ---
def toggle_bolt():
    st.session_state.bolt_on = not st.session_state.bolt_on

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
    st.markdown(f"""<div class="info-box {neon_class}"><h3>📫 İletişim</h3>
    <p>📧 <b>E-posta:</b> utkucmn11@gmail.com</p>
    <p>📸 <b>Instagram:</b> @59.utkucimen_</p>
    <p>💼 <b>LinkedIn:</b> Utku Çimen</p>
    </div>""", unsafe_allow_html=True)

# --- ZİYARETÇİ SAYACI ---
st.divider()
if 'visited' not in st.session_state:
    st.session_state['visited'] = True
    v_count = update_visitor_count()
else:
    v_count = get_visitor_count()

st.metric(label="👤 Toplam Profil Ziyareti", value=v_count)
st.caption("© 2026 Mehmet Utku Çimen")
    
