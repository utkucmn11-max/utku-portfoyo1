import streamlit as st
from PIL import Image
import os

# --- 1. SAYFA YAPILANDIRMASI ---
st.set_page_config(
    page_title="Mehmet Utku Çimen | Portfolyo", 
    page_icon="⚡", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. GIF ARKA PLAN VE CSS AYARLARI ---
# Paylaştığın bağlantıdaki GIF'i tüm ekrana yayar
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://i.pinimg.com/originals/65/d8/85/65d8852fee19c22b80921cbcf3e65197.gif?nii=t");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* İçeriğin okunması için arka planı hafif karartır */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5); /* %50 karartma */
        z-index: -1;
    }}

    /* Yazıları beyaz ve belirgin yapar */
    h1, h2, h3, h4, p, li, span, label, div {{
        color: #ffffff !important;
        text-shadow: 2px 2px 4px #000000; /* Yazıların altına gölge ekler */
    }}

    /* Kart tasarımı (Yarı şeffaf cam efekti) */
    .info-box {{
        background-color: rgba(0, 0, 0, 0.7);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid rgba(255, 235, 59, 0.3); /* Sarı ince çerçeve */
        margin-bottom: 20px;
        backdrop-filter: blur(5px);
    }}

    /* Header ve diğer gereksiz alanları şeffaflaştırır */
    [data-testid="stHeader"] {{
        background: transparent !important;
    }}
    [data-testid="stSidebar"] {{
        display: none;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- 3. PORTFOLYO İÇERİĞİ ---
col1, col2 = st.columns([1, 3])

with col1:
    try:
        img = Image.open("profil.jpg")
        st.image(img, width=280)
    except:
        st.info("📸 'profil.jpg' dosyası bulunamadı.")

with col2:
    st.title("Mehmet Utku Çimen")
    st.subheader("⚡ Elektrik-Elektronik Teknisyeni & Python Geliştirici")
    st.write("📍 Tekirdağ | 🎂 20 Yaşında")
    st.write("Elektrik-elektronik uzmanlığını yazılımla birleştiren projeler geliştiriyorum.")
    st.markdown("### *'Umut; hiç bitmeyen bahar mevsimidir...'*")
    st.caption("- MEVLANA")

st.divider()

# Yetenekler ve İletişim
c1, c2 = st.columns(2)
with c1:
    st.markdown("""
    <div class="info-box">
        <h3>🛠️ Uzmanlık Alanları</h3>
        <ul>
            <li>Elektrik Devre Tasarımı</li>
            <li>Elektronik Bakım & Onarım</li>
            <li>Python ile Otomasyon</li>
            <li>3D Printer Model & Baskı</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="info-box">
        <h3>📫 İletişim</h3>
        <p>📧 <b>E-posta:</b> utkucmn11@gmail.com</p>
        <p>📸 <b>Instagram:</b> <a href="https://www.instagram.com/59.utkucimen_/" style="color:#ffeb3b; text-decoration:none;">@59.utkucimen_</a></p>
    </div>
    """, unsafe_allow_html=True)

# Müzik Bölümü
st.write("### 🎵 Favori Parçam: AC/DC - Back In Black")
current_dir = os.path.dirname(os.path.abspath(__file__))
if os.path.exists(os.path.join(current_dir, "sarki.mp3")):
    with open(os.path.join(current_dir, "sarki.mp3"), "rb") as f:
        st.audio(f.read(), format="audio/mp3")
else:
    st.error("❌ 'sarki.mp3' bulunamadı.")

st.write("##")
st.caption("© 2026 Mehmet Utku Çimen - Tüm Hakları Saklıdır.")

