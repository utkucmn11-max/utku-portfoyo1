import streamlit as st
from PIL import Image
import os

# Sayfa Yapılandırması
st.set_page_config(page_title="Mehmet Utku Çimen | Portfolyo", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

# --- TASARIM VE EFEKTLER (CSS) ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] { display: none; }
    .stApp { background-color: #ffffff; }
    h1, h2, h3, h4, p, li, span, label, div { color: #1a1a1a !important; }
    .info-box {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e9ecef;
        margin-bottom: 20px;
    }
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); opacity: 0.2; }
        50% { transform: translateY(-25px) rotate(15deg); opacity: 0.5; }
        100% { transform: translateY(0px) rotate(0deg); opacity: 0.2; }
    }
    .floating-icon {
        position: fixed; font-size: 40px; animation: float 5s ease-in-out infinite; z-index: 0; pointer-events: none;
    }
    </style>
    <div class="floating-icon" style="top: 10%; left: 5%;">🛠️</div>
    <div class="floating-icon" style="top: 20%; right: 10%;">⚡</div>
    <div class="floating-icon" style="top: 70%; left: 15%;">💻</div>
    <div class="floating-icon" style="top: 80%; right: 5%;">🔧</div>
    """, unsafe_allow_html=True)

# --- ANA SAYFA İÇERİĞİ ---
col1, col2 = st.columns([1, 3])

with col1:
    try:
        img = Image.open("profil.jpg")
        st.image(img, width=230)
    except:
        st.info("📸 Fotoğraf (profil.jpg) bulunamadı.")

with col2:
    st.title("Mehmet Utku Çimen")
    st.subheader("Elektrik-Elektronik Teknisyeni & Geliştirici")
    st.write("📍 Tekirdağ, Kapaklı | 🎂 20 Yaşında")
    st.write("🎓 Elektrik-Elektronik Mezunu")
    st.write("Merhaba! Ben Utku. Elektrik-elektronik sektöründe aktif çalışırken Python ile projeler geliştiriyorum.")

st.divider()

# --- MÜZİK ÇALAR BÖLÜMÜ (YENİ VE GARANTİ YÖNTEM) ---
st.write("### 🎵 Favori Parçam")

# Bu kısım dosyanın nerede olduğunu otomatik bulur
current_dir = os.path.dirname(os.path.abspath(__file__)) # Kodun olduğu klasör
found = False

# Tüm alt klasörleri tara ve sarki.mp3'ü bul
for root, dirs, files in os.walk(current_dir):
    if "sarki.mp3" in files:
        audio_path = os.path.join(root, "sarki.mp3")
        with open(audio_path, "rb") as f:
            st.audio(f.read(), format="audio/mp3")
        found = True
        break

if not found:
    st.error("❌ 'sarki.mp3' dosyası hiçbir klasörde bulunamadı!")
    st.info(f"Lütfen müziğin adının tam olarak **sarki.mp3** olduğundan emin ol.")

st.divider()

# Yetenekler, İletişim ve Hobiler alt alta
c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="info-box"><h3>🛠️ Uzmanlık Alanları</h3><ul><li>Elektrik Devre Tasarımı</li><li>Elektronik Bakım & Onarım</li><li>Python ile Otomasyon</li></ul></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="info-box"><h3>📫 İletişim</h3><p>📧 <b>E-posta:</b> utkucmn11@gmail.com</p><p>📸 <b>Instagram:</b> <a href="https://www.instagram.com/59.utkucimen_/" style="color:#1a1a1a;">59.utkucimen_</a></p></div>', unsafe_allow_html=True)

st.write("### 🎮 Hobiler")
st.write("Müzik Dinlemek | Yürüyüş Yapmak | Oyun Oynamak")

st.caption("© 2026 Mehmet Utku Çimen - Tüm Hakları Saklıdır.")
