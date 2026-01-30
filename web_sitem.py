import streamlit as st
import os
import base64

# --- SAYFA YAPILANDIRMASI ---
st.set_page_config(page_title="Mehmet Utku Çimen | Portfolyo", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

# --- ZİYARETÇİ SAYACI FONKSİYONLARI ---
counter_file = "ziyaretci_sayisi.txt"

def get_visitor_count():
    if not os.path.exists(counter_file):
        with open(counter_file, "w") as f: f.write("0")
    with open(counter_file, "r") as f: return int(f.read())

def update_visitor_count():
    count = get_visitor_count()
    new_count = count + 1
    with open(counter_file, "w") as f: f.write(str(new_count))
    return new_count

# --- ARKA PLAN GIF OKUMA ---
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f: data = f.read()
        return base64.b64encode(data).decode()
    except: return None

bin_str = get_base64_of_bin_file('arkaplan.gif')
background_css = f"url(data:image/gif;base64,{bin_str})" if bin_str else "none"

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
        background-color: rgba(0, 0, 0, 0.6); backdrop-filter: brightness(0.5); z-index: -1;
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
        padding: 15px; border: 1px solid #00f2ff;
        border-radius: 10px; box-shadow: 0px 0px 10px rgba(0, 242, 255, 0.2);
    }}
    
    .sensor-text {{
        color: #00f2ff !important; font-weight: bold;
        text-shadow: 1px 1px 2px #000000; font-size: 1.1em;
    }}

    /* ŞİMŞEK EFEKTİ */
    .bolt-container {{
        display: flex; justify-content: center; align-items: center; padding: 20px;
    }}
    .bolt-svg {{
        width: 100px; height: 100px; transition: 0.4s; stroke: #444; stroke-width: 2; fill: none;
    }}
    .bolt-on {{
        fill: #00f2ff; stroke: #fff;
        filter: drop-shadow(0 0 15px #00f2ff) drop-shadow(0 0 30px #00f2ff);
        transform: scale(1.1);
    }}

    @keyframes float {{
        0% {{ transform: translateY(0px) rotate(0deg); opacity: 0.2; }}
        50% {{ transform: translateY(-25px) rotate(15deg); opacity: 0.5; }}
        100% {{ transform: translateY(0px) rotate(0deg); opacity: 0.2; }}
    }}
    .floating-icon {{
        position: fixed; font-size: 40px; animation: float 5s ease-in-out infinite;
        z-index: 0; pointer-events: none;
    }}
    </style>
    
    <div class="floating-icon" style="top: 10%; left: 5%;">🛠️</div>
    <div class="floating-icon" style="top: 20%; right: 10%;">⚡</div>
    <div class="floating-icon" style="top: 70%; left: 15%;">💻</div>
    """, unsafe_allow_html=True)

# --- ÜST BÖLÜM (PROFİL) ---
col1, col2 = st.columns([1, 3])
with col1:
    try:
        st.image("profil.jpg", width=250)
    except:
        st.info("📸 Fotoğraf (profil.jpg) bekleniyor.")

with col2:
    st.title("Mehmet Utku Çimen")
    st.subheader("⚡ Elektrik-Elektronik Teknisyeni & Geliştirici")
    st.write("📍 Tekirdağ | 🎂 20 Yaşında")
    st.write("Elektrik-elektronik lise mezunuyum. Endüstriyel sistemler ve Python tabanlı otomasyonlarla ilgileniyorum.")
    st.write("> *'Umut; hiç bitmeyen bahar mevsimidir.'* — Mevlana")

st.divider()

# --- ŞİMŞEK ETKİLEŞİMİ ---
if 'bolt_active' not in st.session_state:
    st.session_state.bolt_active = False

def toggle_bolt():
    st.session_state.bolt_active = not st.session_state.bolt_active

col_bolt_1, col_bolt_2 = st.columns([1, 2])
with col_bolt_1:
    bolt_class = "bolt-on" if st.session_state.bolt_active else ""
    st.markdown(f"""
        <div class="bolt-container">
            <svg class="bolt-svg {bolt_class}" viewBox="0 0 24 24">
                <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
            </svg>
        </div>
    """, unsafe_allow_html=True)
    
with col_bolt_2:
    st.write("### ⚡ Enerji Testi")
    btn_label = "Sistemi Kapat" if st.session_state.bolt_active else "Sisteme Enerji Ver"
    st.button(btn_label, on_click=toggle_bolt, use_container_width=True)
    if st.session_state.bolt_active:
        st.info("Sistem Aktif: Yüksek Gerilim Tespit Edildi! ⚡")

st.divider()

# --- UZMANLIK VE İLETİŞİM ---
c1, c2 = st.columns(2)
with c1:
    st.markdown("""<div class="info-box"><h3>🛠️ Uzmanlık Alanları</h3>
    <ul><li>Elektrik Devre Tasarımı</li><li>Elektronik Bakım & Onarım</li>
    <li>Python ile Otomasyon</li><li>3D Printer Model & Baskı</li></ul></div>""", unsafe_allow_html=True)

with c2:
    linkedin_url = "https://www.linkedin.com/in/utkucimen" 
    st.markdown(f"""<div class="info-box"><h3>📫 İletişim</h3>
    <p>📧 <b>E-posta:</b> utkucmn11@gmail.com</p>
    <p>📸 <b>Instagram:</b> <a href="https://www.instagram.com/59.utkucimen_/" target="_blank" style="color:#00f2ff; text-decoration:none;">@59.utkucimen_</a></p>
    <p>💼 <b>LinkedIn:</b> <a href="{linkedin_url}" target="_blank" style="color:#00f2ff; text-decoration:none;">Utku Çimen</a></p>
    </div>""", unsafe_allow_html=True)

# --- TEKNİK REHBER ---
st.header("📡 Teknik Rehber")
t1, t2, t3, t4 = st.tabs(["🧲 İndüktif", "🔮 Kapasitif", "👁️ Optik", "📐 Ohm Yasası"])

with t1:
    st.write("### 🧲 İndüktif Sensör\nSadece metal nesneleri algılar. Elektromanyetik alan prensibiyle çalışır.")
    st.markdown("""<div class="sensor-card"><span class="sensor-text">🟤 Kahve: +24V | 🔵 Mavi: 0V | ⚫ Siyah: Sinyal (Output)</span></div>""", unsafe_allow_html=True)

with t4:
    st.write("### 📐 Ohm Yasası Hesaplayıcı")
    calc_col1, calc_col2 = st.columns(2)
    with calc_col1:
        v_input = st.number_input("Gerilim (Volt)", value=220.0)
        r_input = st.number_input("Direnç (Ohm)", value=10.0)
        if r_input > 0:
            i_result = v_input / r_input
            st.markdown(f"""<div class="sensor-card"><span class="sensor-text">Akım: {i_result:.2f} Amper</span></div>""", unsafe_allow_html=True)

# --- ALT BÖLÜM ---
st.divider()
st.write("### 🎵 Favori Parçam: AC-DC - BACK IN BLACK")
if os.path.exists("sarki.mp3"):
    st.audio("sarki.mp3")

# --- ZİYARETÇİ SAYACI ---
if 'visited' not in st.session_state:
    st.session_state['visited'] = True
    v_count = update_visitor_count()
else:
    v_count = get_visitor_count()

st.metric(label="👤 Profil Ziyareti", value=v_count)
st.caption("© 2026 Mehmet Utku Çimen | Tüm Hakları Saklıdır.")
