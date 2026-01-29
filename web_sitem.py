import streamlit as st
from PIL import Image
import os
import base64

# --- SAYFA YAPILANDIRMASI ---
st.set_page_config(page_title="Mehmet Utku Çimen | Portfolyo", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

# --- ZİYARETÇİ SAYACI FONKSİYONLARI ---
counter_file = "ziyaretci_sayisi.txt"

def get_visitor_count():
    if not os.path.exists(counter_file):
        with open(counter_file, "w") as f:
            with open(counter_file, "w") as f: f.write("0")
    with open(counter_file, "r") as f:
        return int(f.read())

def update_visitor_count():
    count = get_visitor_count()
    new_count = count + 1
    with open(counter_file, "w") as f:
        f.write(str(new_count))
    return new_count

# --- ARKA PLAN GIF OKUMA ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

try:
    bin_str = get_base64_of_bin_file('arkaplan.gif')
    background_css = f"url(data:image/gif;base64,{bin_str})"
except:
    background_css = "none"

# --- TASARIM VE EFEKTLER (CSS) ---
st.markdown(f"""
    <style>
    [data-testid="stSidebar"] {{ display: none; }}
    .stApp {{
        background-image: {background_css};
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-color: #000000;
    }}
    .stApp::before {{
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.5); backdrop-filter: brightness(0.6); z-index: -1;
    }}
    h1, h2, h3, h4, p, li, span, label, div {{
        color: #ffffff !important;
        text-shadow: 2px 2px 4px #000000;
    }}
    .info-box {{
        background-color: rgba(0, 0, 0, 0.7);
        padding: 20px; border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px; backdrop-filter: blur(10px);
    }}
    .sensor-card {{
        background: rgba(0,0,0,0.8);
        padding: 15px; border: 1px solid #ffff00;
        border-radius: 10px; box-shadow: 0px 0px 10px rgba(255, 255, 0, 0.2);
    }}
    .sensor-text {{
        color: #ffff00 !important; font-weight: bold;
        text-shadow: 1px 1px 2px #000000; font-size: 1.1em;
    }}
    @keyframes float {{
        0% {{ transform: translateY(0px) rotate(0deg); opacity: 0.2; }}
        50% {{ transform: translateY(-25px) rotate(15deg); opacity: 0.5; }}
        100% {{ transform: translateY(0px) rotate(0deg); opacity: 0.2; }}
    }}
    .floating-icon {{
        position: fixed; font-size: 40px;
        animation: float 5s ease-in-out infinite;
        z-index: 0; pointer-events: none;
    }}
    </style>
    <div class="floating-icon" style="top: 10%; left: 5%;">🛠️</div>
    <div class="floating-icon" style="top: 20%; right: 10%;">⚡</div>
    <div class="floating-icon" style="top: 70%; left: 15%;">💻</div>
    """, unsafe_allow_html=True)

# --- ÜST BÖLÜM ---
col1, col2 = st.columns([1, 3])
with col1:
    try:
        st.image("profil.jpg", width=300)
    except:
        st.info("📸 profil.jpg bulunamadı.")

with col2:
    st.title("Mehmet Utku Çimen")
    st.subheader("Elektrik-Elektronik Teknisyeni & Geliştirici")
    st.write("📍 Tekirdağ | 🎂 20 Yaşında | 🎓 Elektrik-Elektronik Mezunu")
    st.write("Merhaba Ben Utku. Elektrik-elektronik sektöründe çalışırken Python ile dijital çözümler geliştiriyorum.")
    st.write("*(Umut; hiç bitmeyen bahar mevsimidir...)* - **MEVLANA**")

st.divider()

# --- UZMANLIK VE İLETİŞİM ---
c1, c2 = st.columns(2)
with c1:
    st.markdown("""<div class="info-box"><h3>🛠️ Uzmanlık Alanları</h3>
    <ul><li>Elektrik Devre Tasarımı</li><li>Python ile Otomasyon</li>
    <li>3D Printer & Prototipleme</li><li>Bakım & Onarım</li></ul></div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""<div class="info-box"><h3>📫 İletişim</h3>
    <p>📧 utkucmn11@gmail.com</p>
    <p>📸 <a href="https://www.instagram.com/59.utkucimen_/" style="color:#ffff00; text-decoration:none;">@59.utkucimen_</a></p>
    <p>💼 LinkedIn: Utku Çimen</p></div>""", unsafe_allow_html=True)

# --- TEKNİK REHBER ---
st.header("📡 Teknik Rehber")
t1, t2, t3, t4 = st.tabs(["🧲 İndüktif", "🔮 Kapasitif", "👁️ Optik", "⚡ Ohm Yasası"])

with t1:
    col_a, col_b = st.columns([1, 2])
    with col_a: st.write("### 🧲 İndüktif\nSadece metal algılar.")
    with col_b:
        st.markdown("""<div class="sensor-card"><span class="sensor-text">🟤 Kahve: +24V DC<br>🔵 Mavi: 0V (GND)<br>⚫ Siyah: Sinyal (NO)</span></div>""", unsafe_allow_html=True)

with t2:
    col_a, col_b = st.columns([1, 2])
    with col_a: st.write("### 🔮 Kapasitif\nHer nesneyi algılar.")
    with col_b:
        st.markdown("""<div class="sensor-card"><span class="sensor-text">🟤 Kahve: +24V DC<br>🔵 Mavi: 0V (GND)<br>⚫ Siyah: Sinyal (NO)</span></div>""", unsafe_allow_html=True)

with t3:
    col_a, col_b = st.columns([1, 2])
    with col_a: st.write("### 👁️ Optik\nIşık kesilmesiyle çalışır.")
    with col_b:
        st.markdown("""<div class="sensor-card"><span class="sensor-text">🟤 Kahve: +24V DC<br>🔵 Mavi: 0V (GND)<br>⚫ Siyah: NO Sinyal<br>⚪ Beyaz: NC Sinyal</span></div>""", unsafe_allow_html=True)

with t4:
    st.write("### 📐 Ohm Yasası Hesaplayıcı (V = I x R)")
    calc1, calc2 = st.columns(2)
    with calc1:
        v_in = st.number_input("Gerilim (Volt)", value=220.0)
        r_in = st.number_input("Direnç (Ohm)", value=10.0)
        if r_in > 0:
            st.markdown(f'<p class="sensor-text">Sonuç: {v_in/r_in:.2f} Amper</p>', unsafe_allow_html=True)
    with calc2:
        st.markdown('<div class="info-box">Direnç arttıkça akım düşer, gerilim arttıkça akım artar.</div>', unsafe_allow_html=True)

# --- ALT BÖLÜM ---
st.divider()
st.header("💻 Projelerim")
with st.expander("🚀 Çalışmalarım", expanded=True):
    st.write("Python otomasyon projelerim devam ediyor.")

st.write("### 🎵 Favori Parçam: AC-DC - BACK-IN-BLACK")
if os.path.exists("sarki.mp3"):
    with open("sarki.mp3", "rb") as f:
        st.audio(f.read(), format="audio/mp3")
else:
    st.error("❌ sarki.mp3 bulunamadı.")

# --- ZİYARETÇİ SAYACI ---
st.divider()
v_count = update_visitor_count() if 'visited' not in st.session_state else get_visitor_count()
st.session_state['visited'] = True
st.metric(label="👤 Toplam Ziyaret", value=v_count)
st.caption("© 2026 Mehmet Utku Çimen")
