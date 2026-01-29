import streamlit as st
from PIL import Image
import os
import base64

# --- SAYFA YAPILANDIRMASI ---
st.set_page_config(page_title="Mehmet Utku Çimen | Portfolyo", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

# --- FONKSİYONLAR ---
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

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f: return base64.b64encode(f.read()).decode()

# Arka plan ayarı
try:
    bin_str = get_base64_of_bin_file('arkaplan.gif')
    background_css = f"url(data:image/gif;base64,{bin_str})"
except FileNotFoundError:
    background_css = "none"

# --- TASARIM VE CSS ---
st.markdown(f"""
    <style>
    [data-testid="stSidebar"] {{ display: none; }}
    .stApp {{
        background-image: {background_css};
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .stApp::before {{
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.6); z-index: -1;
    }}
    h1, h2, h3, p, li {{ color: #ffffff !important; text-shadow: 2px 2px 4px #000000; }}
    .info-box {{
        background-color: rgba(255, 255, 255, 0.05);
        padding: 20px; border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }}
    .sensor-card {{
        background: rgba(0,0,0,0.5);
        padding: 15px;
        border-left: 5px solid #ffff00;
        border-radius: 5px;
    }}
    @keyframes float {{
        0% {{ transform: translateY(0px); opacity: 0.3; }}
        50% {{ transform: translateY(-20px); opacity: 0.6; }}
        100% {{ transform: translateY(0px); opacity: 0.3; }}
    }}
    .floating-icon {{
        position: fixed; font-size: 40px;
        animation: float 5s ease-in-out infinite;
        z-index: 0; pointer-events: none;
    }}
    </style>
    <div class="floating-icon" style="top: 10%; left: 5%;">🛠️</div>
    <div class="floating-icon" style="top: 70%; right: 10%;">⚡</div>
    """, unsafe_allow_html=True)

# --- ÜST BÖLÜM (PROFİL) ---
col1, col2 = st.columns([1, 3])
with col1:
    try:
        st.image("profil.jpg", width=250)
    except:
        st.info("📸 Fotoğraf Yüklenemedi.")

with col2:
    st.title("Mehmet Utku Çimen")
    st.subheader("Elektrik-Elektronik Teknisyeni & Python Geliştirici")
    st.write("📍 Tekirdağ | 🎂 20 Yaşında")
    st.write("> \"Umut; hiç bitmeyen bahar mevsimidir. İçine kar da yağar, fırtına da kopar ama çiçekler hep açar.\" - MEVLANA")

# --- YETENEKLER VE İLETİŞİM ---
st.divider()
c1, c2 = st.columns(2)
with c1:
    st.markdown("""<div class="info-box"><h3>🛠️ Uzmanlık Alanları</h3>
    <ul><li>Elektrik Devre Tasarımı</li><li>Python ile Otomasyon</li>
    <li>3D Yazıcı Teknolojileri</li><li>Elektronik Bakım-Onarım</li></ul></div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""<div class="info-box"><h3>📫 İletişim</h3>
    <p>📧 utkucmn11@gmail.com</p>
    <p>📸 <a href="https://www.instagram.com/59.utkucimen_/" style="color:#ffff00;">@59.utkucimen_</a></p>
    <p>💼 LinkedIn: Utku Çimen</p></div>""", unsafe_allow_html=True)

# --- SENSÖR REHBERİ (YENİ EKLEDİĞİMİZ BÖLÜM) ---
st.header("📡 Teknik Rehber: Sensör Renk Kodları")
st.write("Endüstriyel sensörlerin standart bağlantı şemaları ve çalışma prensipleri.")



t1, t2, t3 = st.tabs(["🧲 İndüktif", "🔮 Kapasitif", "👁️ Optik / Fotosel"])

with t1:
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        st.markdown("### 🧲 İndüktif\n*Sadece metal algılar.*")
    with col_txt:
        st.markdown("""<div class="sensor-card">
        🟤 <b>Kahve:</b> +24V DC<br>🔵 <b>Mavi:</b> 0V (GND)<br>⚫ <b>Siyah:</b> Sinyal (NO)</div>""", unsafe_allow_html=True)

with t2:
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        st.markdown("### 🔮 Kapasitif\n*Yoğunluk farkını algılar.*")
    with col_txt:
        st.markdown("""<div class="sensor-card">
        🟤 <b>Kahve:</b> +24V DC<br>🔵 <b>Mavi:</b> 0V (GND)<br>⚫ <b>Siyah:</b> Sinyal (NO)</div>""", unsafe_allow_html=True)

with t3:
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        st.markdown("### 👁️ Optik\n*Işık yansımasıyla çalışır.*")
    with col_txt:
        st.markdown("""<div class="sensor-card">
        🟤 <b>Kahve:</b> +24V DC<br>🔵 <b>Mavi:</b> 0V (GND)<br>⚫ <b>Siyah:</b> Sinyal (NO)<br>⚪ <b>Beyaz:</b> Sinyal (NC)</div>""", unsafe_allow_html=True)

# --- PROJELER VE HOBİLER ---
st.divider()
st.header("💻 Projelerim")
with st.expander("🚀 Aktif Geliştirmeler"):
    st.write("Python tabanlı otomasyon sistemleri ve veri analizi üzerine çalışıyorum.")

st.write("### 🎵 Favori Parçam")
if os.path.exists("sarki.mp3"):
    st.audio("sarki.mp3")
else:
    st.caption("AC-DC | BACK-IN-BLACK (Ses dosyası bulunamadı)")

# --- SAYAC ---
st.divider()
v_count = update_visitor_count() if 'visited' not in st.session_state else get_visitor_count()
st.session_state['visited'] = True
st.metric(label="👤 Toplam Profil Ziyareti", value=v_count)

st.caption("© 2026 Mehmet Utku Çimen")




