import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

# Sayfa Yapılandırması
st.set_page_config(page_title="Mehmet Utku Çimen | Portfolyo", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

# --- CANLI MAVİ YILDIRIM EFEKTİ (JS) ---
lightning_js = """
<div id="lightning-container" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 9999; pointer-events: none;">
    <canvas id="canvas"></canvas>
</div>
<script>
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
let width, height;
let lightning = [];

function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
}
window.addEventListener('resize', resize);
resize();

class Lightning {
    constructor() { this.reset(); }
    reset() {
        this.x = Math.random() * width;
        this.y = 0;
        this.segments = [];
        this.life = 25; 
        this.opacity = 1;
        this.createPath();
    }
    createPath() {
        let currX = this.x;
        let currY = this.y;
        while (currY < height) {
            let nextX = currX + (Math.random() * 120 - 60);
            let nextY = currY + (Math.random() * 40 + 20);
            this.segments.push({x1: currX, y1: currY, x2: nextX, y2: nextY});
            currX = nextX;
            currY = nextY;
        }
    }
    draw() {
        if (this.life <= 0) return;
        
        // Dış Parlama (Mavi Glow)
        ctx.strokeStyle = `rgba(0, 191, 255, ${this.opacity * 0.5})`;
        ctx.lineWidth = 5;
        ctx.shadowBlur = 20;
        ctx.shadowColor = '#00bfff';
        
        ctx.beginPath();
        for (let s of this.segments) {
            ctx.moveTo(s.x1, s.y1);
            ctx.lineTo(s.x2, s.y2);
        }
        ctx.stroke();

        // İç Çizgi (Beyaz/Açık Mavi Merkez)
        ctx.strokeStyle = `rgba(255, 255, 255, ${this.opacity})`;
        ctx.lineWidth = 2;
        ctx.stroke();
        
        this.life--;
        this.opacity -= 0.04;
    }
}

function animate() {
    ctx.clearRect(0, 0, width, height);
    if (Math.random() < 0.04) { // Çakma sıklığı artırıldı
        lightning.push(new Lightning());
    }
    lightning.forEach((l, i) => {
        l.draw();
        if (l.life <= 0) lightning.splice(i, 1);
    });
    requestAnimationFrame(animate);
}
animate();
</script>
<style>
    #canvas { width: 100%; height: 100%; }
</style>
"""

# Efekti en üste ekle
components.html(lightning_js, height=0)

# --- TASARIM VE EFEKTLER (CSS) ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] { display: none; }
    .stApp { background-color: #ffffff; }
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
        z-index: 1; /* Yıldırım bunun üstünde kalacak */
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
    st.write("🎓 Elektrik-Elektronik Mezunu")
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
