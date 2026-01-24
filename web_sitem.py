import streamlit as st
from PIL import Image

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
        position: fixed;
        font-size: 40px;
        animation: float 5s ease-in-out infinite;
        z-index: 0;
        pointer-events: none;
    }
    </style>
    
    <div class="floating-icon" style="top: 10%; left: 5%;">🛠️</div>
    <div class="floating-icon" style="top: 20%; right: 10%;">⚡</div>
    <div class="floating-icon" style="top: 70%; left: 15%;">💻</div>
    <div class="floating-icon" style="top: 80%; right: 5%;">🔧</div>
    <div class="floating-icon" style="top: 40%; left: 80%;">🔌</div>
    <div class="floating-icon" style="top: 50%; right: 50%;">⚙️</div>
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
    st.write("""
    Merhaba! Ben Utku. Elektrik-elektronik lise mezunuyum ve aktif olarak bu sektörde çalışıyorum. 
    Teknolojiye olan tutkumla beraber Python dünyasında kendimi geliştiriyor ve dijital çözümler üretiyorum.
    """)

st.divider()

# Orta Kısım: Yetenekler ve İletişim
c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="info-box">
        <h3>🛠️ Uzmanlık Alanları</h3>
        <ul>
            <li>Elektrik Devre Tasarımı</li>
            <li>Elektronik Bakım & Onarım</li>
            <li>Python ile Otomasyon</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="info-box">
        <h3>📫 İletişim & Sosyal Medya</h3>
        <p>📧 <b>E-posta:</b> utkucmn11@gmail.com</p>
        <p>📸 <b>Instagram:</b> <a href="https://www.instagram.com/59.utkucimen_/" style="color:#1a1a1a;">59.utkucimen_</a></p>
        <p>💼 <b>LinkedIn:</b> <a href="https://www.linkedin.com/" style="color:#1a1a1a;">Utku Çimen</a></p>
    </div>
    """, unsafe_allow_html=True)

# Alt Kısım: Projeler
st.header("💻 Projelerim")
with st.expander("🚀 Devam Eden Çalışmalar", expanded=True):
    st.write("Şu an üzerinde çalıştığım projeler Python tabanlı otomasyon sistemleri üzerine odaklanıyor.")
    st.warning("Gizlilik nedeniyle detaylar yakında paylaşılacaktır! 😂")

st.divider()

# --- MÜZİK ÇALAR BÖLÜMÜ ---
st.write("### 🎵 Favori Parçam")
try:
    # "muzikler" yazan yere kendi klasör adını yazmalısın (Örn: "assets" veya "audio")
    audio_file = open("musıc"/sarki.mp3", 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
except FileNotFoundError:
    st.error("🎵 Müzik dosyası belirtilen klasörde bulunamadı.")

st.write("### 🎮 Hobiler")
st.write("Müzik Dinlemek | Yürüyüş Yapmak | Oyun Oynamak")

st.write("##")
st.caption("© 2026 Mehmet Utku Çimen - Tüm Hakları Saklıdır.")





