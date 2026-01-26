import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import os

# --- 1. SAYFA YAPILANDIRMASI ---
st.set_page_config(
    page_title="Mehmet Utku Çimen | Portfolyo", 
    page_icon="⚡", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. YILDIRIM EFEKTİ (JavaScript & HTML) ---
# Görseldeki sarı yıldırımları siyah arka plana yerleştiren ana mekanizma
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
            // Siyah arka planı her karede hafif şeffaf boyayarak iz bırakma efekti yaratır
            ctx.fillStyle = 'rgba(0, 0, 0, 0.15)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            if (Math.random() > 0.82) { // Yıldırım sıklığı (0.82 = Oldukça sık)
                ctx.strokeStyle = '#fffb00'; // Görseldeki elektrik sarısı
                ctx.lineWidth = Math.random() * 3 + 1;
                ctx.shadowBlur = 40; // Neon parlama efekti
                ctx.shadowColor = '#ffff00';
                
                let x = Math.random() * canvas.width;
                let y = 0;
                ctx.beginPath();
                ctx.moveTo(x, y);
                
                while (y < canvas.height) {
                    x += (Math.random() - 0.5) * 90; // Kırılma mesafesi
                    y += Math.random() * 40;
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

# --- 3. STREAMLIT TASARIM AYARLARI (CSS) ---
st.markdown("""
    <style>
    /* Arka planı ve başlığı tamamen şeffaflaştırır */
    .stApp, [data-testid="stHeader"] {
        background: transparent !important;
        background-color: #000000 !important;
    }
    
    /* Yazı renklerini beyaz yapar */
    h1, h2, h3, h4, p, li, span, label, div {
        color: #ffffff !important;
    }

    /* Bilgi kutuları (Yarı şeffaf cam efekti) */
    .info-box {
        background-color: rgba(255, 255, 255, 0.07);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }

    /* Kayan ikonların opaklığını ve stilini ayarlar */
    .floating-icon {
        position: fixed;
        font-size: 45px;
        opacity: 0.5;
        z-index: 0;
        pointer-events: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. PORTFOLYO İÇERİĞİ ---
# Havada uçuşan ikonlar
st.markdown('<div class="floating-icon" style="top: 10%; left: 5%;">🛠️</div>', unsafe_allow_html=True)
st.markdown('<div class="floating-icon" style="top: 25%; right: 10%;">⚡</div>', unsafe_allow_html=True)
st.markdown('<div class="floating-icon" style="top: 75%; left: 15%;">💻</div>', unsafe_allow_html=True)
st.markdown('<div class="floating-icon" style="top: 45%; right: 7%;">🔧</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])

with col1:
    try:
        img = Image.open("profil.jpg")
        st.image(img, width=280)
    except:
        st.info("📸 'profil.jpg' bulunamadı.")

with col2:
    st.title("Mehmet Utku Çimen")
    st.subheader("⚡ Elektrik-Elektronik Teknisyeni & Python Geliştirici")
    st.write("📍 Tekirdağ | 🎂 20 Yaşında")
    st.write("Elektrik dünyasının enerjisini Python'un gücüyle birleştiriyorum.")
    st.markdown("### *'Umut; hiç bitmeyen bahar mevsimidir...'*")
    st.caption("- MEVLANA")

st.divider()

# Yetenekler ve İletişim
c1, c2 = st.columns(2)
with c1:
    st.markdown("""<div class="info-box"><h3>🛠️ Uzmanlık Alanları</h3><ul>
    <li>Elektrik Devre Tasarımı</li><li>Elektronik Bakım & Onarım</li>
    <li>Python ile Otomasyon</li><li>3D Model Tasarımı & Baskı</li></ul></div>""", unsafe_allow_html=True)

with c2:
    st.markdown(f"""<div class="info-box"><h3>📫 İletişim</h3>
    <p>📧 <b>E-posta:</b> utkucmn11@gmail.com</p>
    <p>📸 <b>Instagram:</b> <a href="https://www.instagram.com/59.utkucimen_/" style="color:#ffff00; text-decoration:none;">@59.utkucimen_</a></p>
    </div>""", unsafe_allow_html=True)

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
