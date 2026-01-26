import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import os

# 1. SAYFA YAPILANDIRMASI (En üstte olmalı)
st.set_page_config(
    page_title="Mehmet Utku Çimen | Portfolyo", 
    page_icon="⚡", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. YILDIRIM EFEKTİ (Bağımsız Katman)
# Bu kısım ekranın en arkasına yıldırımları yerleştirir
components.html(
    """
    <style>
        body { margin: 0; background: #000000; overflow: hidden; }
        canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -1;
            pointer-events: none;
        }
    </style>
    <canvas id="lightning"></canvas>
    <script>
        const canvas = document.getElementById('lightning');
        const ctx = canvas.getContext('2d');
        function resize() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        window.onresize = resize;
        resize();

        function draw() {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.15)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            if (Math.random() > 0.85) { // Sıklık ayarı
                ctx.strokeStyle = '#fffb00';
                ctx.lineWidth = 3;
                ctx.shadowBlur = 20;
                ctx.shadowColor = '#fffb00';
                let x = Math.random() * canvas.width;
                let y = 0;
                ctx.beginPath();
                ctx.moveTo(x, y);
                while (y < canvas.height) {
                    x += (Math.random() - 0.5) * 80;
                    y += Math.random() * 35;
                    ctx.lineTo(x, y);
                }
                ctx.stroke();
            }
            requestAnimationFrame(draw);
        }
        draw();
    </script>
    """,
    height=0,
)

# 3. GENEL TASARIM (CSS)
# Streamlit'in beyaz alanlarını şeffaf yapar ve yazıları beyazlatır
st.markdown("""
    <style>
    /* Streamlit bileşenlerini şeffaflaştır */
    .stApp { background: transparent !important; }
    [data-testid="stHeader"] { background: transparent !important; }
    [data-testid="stSidebar"] { display: none; }
    
    /* Yazı renklerini zorla beyaz yap */
    h1, h2, h3, h4, p, li, span, label, div {
        color: #ffffff !important;
    }

    /* Bilgi kutuları (Yarı şeffaf cam efekti) */
    .info-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }

    /* Yüzen ikonlar */
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); opacity: 0.4; }
        50% { transform: translateY(-20px) rotate(10deg); opacity: 0.7; }
        100% { transform: translateY(0px) rotate(0deg); opacity: 0.4; }
    }
    .floating-icon {
        position: fixed;
        font-size: 40px;
        animation: float 5s ease-in-out infinite;
        z-index: 1;
        pointer-events: none;
    }
    </style>
    
    <div class="floating-icon" style="top: 15%; left: 5%;">🛠️</div>
    <div class="floating-icon" style="top: 25%; right: 10%;">⚡</div>
    <div class="floating-icon" style="top: 75%; left: 15%;">💻</div>
    <div class="floating-icon" style="top: 45%; right: 5%;">🔧</div>
    """, unsafe_allow_html=True)

# 4. İÇERİK (Sizin Mevcut Portfolyonuz)
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
    st.write("Teknoloji tutkusuyla Python dünyasında çözümler üretiyorum.")
    st.markdown("### *'Umut; hiç bitmeyen bahar mevsimidir...'*")
    st.caption("- MEVLANA")

st.divider()

c1, c2 = st.columns(2)
with c1:
    st.markdown("""<div class="info-box"><h3>🛠️ Uzmanlık Alanları</h3><ul>
    <li>Elektrik Devre Tasarımı</li><li>Elektronik Bakım & Onarım</li>
    <li>Python ile Otomasyon</li><li>3D Model Tasarımı & Baskı</li></ul></div>""", unsafe_allow_html=True)

with c2:
    st.markdown("""<div class="info-box"><h3>📫 İletişim</h3>
    <p>📧 utkucmn11@gmail.com</p>
    <p>📸 <a href='https://instagram.com/59.utkucimen_' style='color:yellow;'>@59.utkucimen_</a></p>
    </div>""", unsafe_allow_html=True)

# Müzik Bölümü
st.write("### 🎵 Favori Parçam: AC/DC - Back In Black")
current_dir = os.path.dirname(os.path.abspath(__file__))
if os.path.exists(os.path.join(current_dir, "sarki.mp3")):
    st.audio(os.path.join(current_dir, "sarki.mp3"), format="audio/mp3")
else:
    st.error("❌ 'sarki.mp3' bulunamadı.")

st.caption("© 2026 Mehmet Utku Çimen")



