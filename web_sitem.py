import streamlit as st
from PIL import Image

# Sayfa Konfigürasyonu
st.set_page_config(page_title="Mehmet Utku Çimen | Portfolio", page_icon=" Image.open(1.png)", layout="wide")

# CSS ile Şimşek Butonunu Özelleştirme ve Ortalama
st.markdown("""
    <style>
    .stButton > button {
        display: block;
        margin: 0 auto;
        background-color: transparent;
        border: none;
        font-size: 100px;
        transition: transform 0.3s, filter 0.3s;
        cursor: pointer;
    }
    .stButton > button:hover {
        transform: scale(1.2);
        filter: drop-shadow(0 0 15px #FFD700);
        background-color: transparent;
        border: none;
    }
    .stButton > button:active {
        color: #FFD700;
        background-color: transparent;
    }
    .splash-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 60vh;
    }
    .info-box {
        padding: 20px;
        border-radius: 15px;
        background-color: #f0f2f6;
        border: 1px solid #e0e0e0;
        height: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# Session State ile sayfa kontrolü
if 'sayfa_acildi' not in st.session_state:
    st.session_state.sayfa_acildi = False

# --- AÇILIŞ EKRANI ---
if not st.session_state.sayfa_acildi:
    st.markdown('<div class="splash-container">', unsafe_allow_html=True)
    st.write("<h1 style='text-align: center; color: #333;'>Portfolyoya Giriş Yap</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: center; color: #666;'>Devreleri tamamlamak için şimşeğe dokun!</p>", unsafe_allow_html=True)
    
    # Şimşek Butonu
    if st.button("⚡"):
        st.session_state.sayfa_acildi = True
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- ANA SAYFA İÇERİĞİ ---
else:
    # Geri dönmek istersen diye küçük bir çıkış butonu (isteğe bağlı)
    if st.sidebar.button("⬅️ Giriş Ekranına Dön"):
        st.session_state.sayfa_acildi = False
        st.rerun()

    # Üst Kısım: Fotoğraf ve Başlık
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

    # Alt Kısım: Projeler ve Hobiler
    st.header("💻 Projelerim")
    with st.expander("🚀 Devam Eden Çalışmalar", expanded=True):
        st.write("Şu an üzerinde çalıştığım projeler Python tabanlı otomasyon sistemleri üzerine odaklanıyor.")
        st.warning("Gizlilik nedeniyle detaylar yakında paylaşılacaktır! 😂")

    st.divider()
    st.write("### 🎵 Hobiler")
    st.write("Müzik Dinlemek | Yürüyüş Yapmak | Oyun Oynamak")

    st.write("##")
    st.caption("© 2026 Mehmet Utku Çimen - Tüm Hakları Saklıdır.")

