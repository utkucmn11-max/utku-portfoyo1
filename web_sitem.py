import streamlit as st
from PIL import Image

# Sayfa Yapılandırması
st.set_page_config(page_title="Mehmet Utku Çimen | Portfolyo", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

# --- GARANTİLENMİŞ CSS YILDIRIM EFEKTİ ---
st.markdown("""
    <style>
    /* 1. Tüm ekranı kaplayan çakma efekti */
    @keyframes lightning-flash {
        0% { background-color: transparent; }
        1% { background-color: rgba(0, 150, 255, 0.15); }
        2% { background-color: transparent; }
        3% { background-color: rgba(255, 255, 255, 0.2); }
        4% { background-color: transparent; }
    }

    /* 2. Dikey yıldırım çizgisi animasyonu */
    @keyframes bolt {
        0% { opacity: 0; transform: scaleY(0); }
        1% { opacity: 1; transform: scaleY(1); }
        2% { opacity: 0; }
        100% { opacity: 0; }
    }

    .stApp {
        background-color: #ffffff;
        animation: lightning-flash 6s infinite; /* Her 6 saniyede bir ekran parlar */
    }

    /* Yıldırım Çizgisi */
    .bolt-container {
        position: fixed;
        top: 0;
        left: 50%;
        width: 2px;
        height: 100vh;
        background: linear-gradient(to bottom, transparent, #00bfff, #ffffff, transparent);
        box-shadow: 0 0 20px #00bfff;
        z-index: 999;
        opacity: 0;
        pointer-events: none;
        animation: bolt 6s infinite;
    }

    /* Farklı konumlarda ek yıldırım çizgileri */
    .bolt-2 { left: 20%; animation-delay: 2s; width: 1px; }
    .bolt-3 { left: 80%; animation-delay: 4s; width: 1px; }

    /* Mevcut tasarım kodların */
    [data-testid="stSidebar"] { display: none; }
    h1, h2, h3, h4, p, li, span, label, div { color: #1a1a1a !important; }
    .info-box {
        background-color: rgba(248, 249, 250, 0.9);
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
        z-index: 1;
        pointer-events: none;
    }
    </style>

    <div class="bolt-container"></div>
    <div class="bolt-container bolt-2"></div>
    <div class="bolt-container bolt-3"></div>
    
    <div class="floating-icon" style="top: 10%; left: 5%;">🛠️</div>
    <div class="floating-icon" style="top: 20%; right: 10%;">⚡</div>
    <div class="floating-icon" style="top: 70%; left: 15%;">💻</div>
    <div class="floating-icon" style="top: 80%; right: 5%;">🔧</div>
    """, unsafe_allow_html=True)

# --- İÇERİK ---
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
    st.write("Python dünyasında kendimi geliştiriyor ve dijital çözümler üretiyorum.")

st.divider()

c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="info-box"><h3>🛠️ Uzmanlık Alanları</h3><ul><li>Elektrik Devre Tasarımı</li><li>Elektronik Bakım & Onarım</li><li>Python ile Otomasyon</li><li>3D tasarım ve printer</li></ul></div>', unsafe_allow_html=True)

with c2:
    st.markdown(f'<div class="info-box"><h3>📫 İletişim & Sosyal Medya</h3><p>📧 <b>E-posta:</b> utkucmn11@gmail.com</p><p>📸 <b>Instagram:</b> <a href="https://www.instagram.com/59.utkucimen_/" style="color:#1a1a1a;">59.utkucimen_</a></p><p>💼 <b>LinkedIn:</b> Utku Çimen</p></div>', unsafe_allow_html=True)

st.header("💻 Projelerim")
with st.expander("🚀 Devam Eden Çalışmalar", expanded=True):
    st.write("Python tabanlı otomasyon sistemleri üzerine odaklanıyorum.")
    st.warning("Gizlilik nedeniyle detaylar yakında paylaşılacaktır! 😂")

st.divider()
st.caption("© 2026 Mehmet Utku Çimen - Tüm Hakları Saklıdır.")
