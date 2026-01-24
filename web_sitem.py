import streamlit as st
from PIL import Image

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Mehmet Utku Çimen | Portfolyo", 
    page_icon="⚡", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- ANIMASYON VE TASARIM (CSS/JS) ---
st.markdown("""
    <style>
    /* Sidebar gizleme */
    [data-testid="stSidebar"] { display: none; }
    
    /* Giriş Ekranı (Overlay) */
    #intro-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: #ffffff;
        z-index: 9999;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        transition: opacity 0.8s ease-out;
    }

    /* Şimşek Konteynırı */
    .bolt-container {
        position: relative;
        width: 300px;
        height: 300px;
        display: flex;
    }

    /* Şimşek Parçaları (Z-şekli simülasyonu) */
    .bolt-half {
        width: 50%;
        height: 100%;
        background-color: #FFD700; /* Altın Sarısı */
        transition: transform 1s cubic-bezier(0.7, 0, 0.3, 1);
        clip-path: polygon(100% 0, 0 0, 100% 100%); /* Sol parça kesimi */
    }
    
    .bolt-half.right {
        clip-path: polygon(0 0, 0 100%, 100% 100%); /* Sağ parça kesimi */
        margin-left: -2px;
    }

    /* Tıklandığında ayrılma efekti */
    .split-left { transform: translateX(-150%) rotate(-10deg); opacity: 0; }
    .split-right { transform: translateX(150%) rotate(10deg); opacity: 0; }
    .fade-out { opacity: 0; pointer-events: none; }

    /* Yazı Efekti */
    .click-text {
        position: absolute;
        bottom: -50px;
        width: 100%;
        text-align: center;
        font-family: sans-serif;
        color: #DAA520;
        font-weight: bold;
        letter-spacing: 2px;
        animation: blink 1.5s infinite;
    }

    @keyframes blink { 0% {opacity: 0.2;} 50% {opacity: 1;} 100% {opacity: 0.2;} }

    /* Arka plan ve genel stil */
    .stApp { background-color: #ffffff; }
    .info-box {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e9ecef;
        margin-bottom: 20px;
    }
    </style>

    <div id="intro-overlay" onclick="startAnimation()">
        <div class="bolt-container">
            <div id="left-bolt" class="bolt-half"></div>
            <div id="right-bolt" class="bolt-half right"></div>
            <div class="click-text">GİRİŞ İÇİN DOKUN</div>
        </div>
    </div>

    <script>
    function startAnimation() {
        const left = document.getElementById('left-bolt');
        const right = document.getElementById('right-bolt');
        const overlay = document.getElementById('intro-overlay');
        
        left.classList.add('split-left');
        right.classList.add('split-right');
        
        setTimeout(() => {
            overlay.classList.add('fade-out');
            setTimeout(() => {
                overlay.style.display = 'none';
            }, 800);
        }, 600);
    }
    </script>
""", unsafe_allow_html=True)

# --- PORTFOLYO İÇERİĞİ (Tıkladıktan Sonra Görünecek) ---

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
        <p>📸 <b>Instagram:</b> <a href="https://www.instagram.com/59.utkucimen_/" target="_blank" style="color:#1a1a1a;">59.utkucimen_</a></p>
        <p>💼 <b>LinkedIn:</b> <a href="#" style="color:#1a1a1a;">Utku Çimen</a></p>
    </div>
    """, unsafe_allow_html=True)

st.header("💻 Projelerim")
with st.expander("🚀 Devam Eden Çalışmalar", expanded=True):
    st.write("Şu an üzerinde çalıştığım projeler Python tabanlı otomasyon sistemleri üzerine odaklanıyor.")
    st.warning("Gizlilik nedeniyle detaylar yakında paylaşılacaktır! 😂")

st.divider()
st.write("### 🎵 Hobiler")
st.write("Müzik Dinlemek | Yürüyüş Yapmak | Oyun Oynamak")

st.caption("© 2026 Mehmet Utku Çimen - Tüm Hakları Saklıdır.")





