import streamlit as st
from PIL import Image
import os

# Sayfa Yapılandırması
st.set_page_config(page_title="Mehmet Utku Çimen | Portfolyo", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

# --- TASARIM VE EFEKTLER (CSS ve Yıldırım JS) ---
st.markdown("""
    <style>
    /* Sol menüyü tamamen gizle */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* Arka planı siyah yaparak yıldırımı belirginleştiriyoruz */
    .stApp {
        background-color: #000000;
    }
    
    /* Yazı renklerini açık renk yapıyoruz (Karanlık tema uyumu) */
    h1, h2, h3, h4, p, li, span, label, div {
        color: #ffffff !important;
    }

    /* Kart tasarımı - Biraz şeffaflık ekledik */
    .info-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 20px;
        backdrop-filter: blur(5px);
    }

    /* Yıldırım Canvas ayarları */
    #lightning-canvas {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        pointer-events: none;
    }

    /* Havada uçuşan el aletleri animasyonu */
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); opacity: 0.3; }
        50% { transform: translateY(-25px) rotate(15deg); opacity: 0.6; }
        100% { transform: translateY(0px) rotate(0deg); opacity: 0.3; }
    }
    .floating-icon {
        position: fixed;
        font-size: 40px;
        animation: float 5s ease-in-out infinite;
        z-index: 0;
        pointer-events: none;
    }
    </style>
    
    <canvas id="lightning-canvas"></canvas>

    <script>
    const canvas = document.getElementById('lightning-canvas');
    const ctx = canvas.getContext('2d');

    function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resize);
    resize();

    function createLightning() {
        ctx.strokeStyle = 'rgba(255, 255, 0, 0.8)'; // Sarı renk
        ctx.lineWidth = 2;
        ctx.shadowBlur = 15;
        ctx.shadowColor = '#ffff00';

        let x = Math.random() * canvas.width;
        let y = 0;

        ctx.beginPath();
        ctx.moveTo(x, y);

        while (y < canvas.height) {
            x += (Math.random() - 0.5) * 50;
            y += Math.random() * 30;
            ctx.lineTo(x, y);
        }
        ctx.stroke();

        // Yıldırımın anlık çakıp sönmesi için
        setTimeout(() => {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        }, 100);
    }

    // Rastgele aralıklarla yıldırım çaktır
    function loop() {
        if (Math.random() > 1) {
            createLightning();
        }
        requestAnimationFrame(loop);
    }
    loop();
    </script>
    
    <div class="floating-icon" style="top: 10%; left: 5%;">🛠️</div>
    <div class="floating-icon" style="top: 20%; right: 10%;">⚡</div>
    <div class="floating-icon" style="top: 70%; left: 15%;">💻</div>
    <div class="floating-icon" style="top: 80%; right: 5%;">🔧</div>
    <div class="floating-icon" style="top: 40%; left: 80%;">🔌</div>
    <div class="floating-icon" style="top: 50%; right: 50%;">⚙️</div>
    """, unsafe_allow_html=True)


# --- ÜST KISIM: Fotoğraf ve Başlık ---
col1, col2 = st.columns([1, 3])

with col1:
    try:
        img = Image.open("profil.jpg")
        st.image(img, width=300)
    except:
        st.info("📸 Fotoğraf (profil.jpg) bulunamadı.")

with col2:
    st.title("Mehmet Utku Çimen")
    st.subheader("Elektrik-Elektronik Teknisyeni & Geliştirici")
    st.write("📍 Tekirdağ | 🎂 20 Yaşında")
    st.write("🎓 Elektrik-Elektronik Mezunu")
    st.write("""
    Merhaba! Ben Utku. Elektrik-elektronik lise mezunuyum ve aktif olarak bu sektörde çalışıyorum. 
    Teknolojiye olan tutkumla beraber Python dünyasında kendimi geliştiriyor ve dijital çözümler üretiyorum.
    """)
    st.title("(Umut; hiç bitmeyen bahar mevsimidir. İçine kar da yağar, fırtına da kopar ama çiçekler hep açar.)")     
    st.write("(MEVLANA)")
st.divider()

# --- ORTA KISIM: Yetenekler ve İletişim (Yan Yana) ---
c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="info-box">
        <h3>🛠️ Uzmanlık Alanları</h3>
        <ul>
            <li>Elektrik Devre Tasarımı</li>
            <li>Elektronik Bakım & Onarım</li>
            <li>Python ile Otomasyon</li>
            <li>3D Printer Model Tasarımı & Model Baskı Alımı</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="info-box">
        <h3>📫 İletişim & Sosyal Medya</h3>
        <p>📧 <b>E-posta:</b> utkucmn11@gmail.com</p>
        <p>📸 <b>Instagram:</b> <a href="https://www.instagram.com/59.utkucimen_/" style="color:#ffcc00;">59.utkucimen_</a></p>
        <p>💼 <b>LinkedIn:</b> <a href="https://www.linkedin.com/" style="color:#ffcc00;">Utku Çimen</a></p>
    </div>
    """, unsafe_allow_html=True)

# --- ALT KISIM: Projeler ---
st.header("💻 Projelerim")
with st.expander("🚀 Devam Eden Çalışmalar", expanded=True):
    st.write("Şu an üzerinde çalıştığım projeler Python tabanlı otomasyon sistemleri üzerine odaklanıyor.")
    st.warning("Gizlilik nedeniyle detaylar yakında paylaşılacaktır! 😂")

st.divider()

# --- MÜZİK VE HOBİLER ---
st.write("### 🎵 Favori Parçam")
st.write("(AC-DC) BACK-İN-BLACK ")

# Otomatik bulma fonksiyonu
current_dir = os.path.dirname(os.path.abspath(__file__))
found = False
for root, dirs, files in os.walk(current_dir):
    if "sarki.mp3" in files:
        audio_path = os.path.join(root, "sarki.mp3")
        with open(audio_path, "rb") as f:
            st.audio(f.read(), format="audio/mp3")
        found = True
        break

if not found:
    st.error("❌ 'sarki.mp3' bulunamadı.")

st.write("### 🎮 Hobiler")
st.write("Müzik Dinlemek | Yürüyüş Yapmak | Oyun Oynamak")

st.write("##")
st.caption("© 2026 Mehmet Utku Çimen - Tüm Hakları Saklıdır.")


