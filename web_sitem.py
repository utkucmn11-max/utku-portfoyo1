import streamlit as st
from PIL import Image
import base64

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Mehmet Utku Çimen | Portfolyo", 
    page_icon="⚡", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- GİRİŞ KONTROLÜ (Session State) ---
if 'giris_yapildi' not in st.session_state:
    st.session_state.giris_yapildi = False

# --- GÖRSELİ KODA GÖMME ---
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# --- GİRİŞ EKRANI ---
if not st.session_state.giris_yapildi:
    # CSS ve Animasyonlar
    st.markdown("""
        <style>
        [data-testid="stSidebar"] { display: none; }
        .stApp { background-color: #ffffff; }
        
        .cover-container {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            background-color: white;
            z-index: 9999;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        /* Şimşek Logosu */
        .bolt-img {
            width: 300px;
            cursor: pointer;
            transition: transform 0.3s ease;
        }

        .bolt-img:hover {
            transform: scale(1.1) rotate(5deg);
        }

        .click-hint {
            margin-top: 20px;
            color: #DAA520;
            font-weight: bold;
            letter-spacing: 2px;
            animation: blink 1.5s infinite;
        }

        @keyframes blink { 0% {opacity: 0.3;} 50% {opacity: 1;} 100% {opacity: 0.3;} }
        </style>
    """, unsafe_allow_html=True)

    # Görseli göster ve butonu şeffaf bir katman olarak üzerine koy
    try:
        # Görsel dosyasının adının 'simsek.png' olduğundan emin ol
        img_data = get_base64_image("simsek.png")
        st.markdown(f"""
            <div class="cover-container">
                <img src="data:image/png;base64,{img_data}" class="bolt-img">
                <div class="click-hint">GİRİŞ İÇİN ŞİMŞEĞE DOKUN</div>
            </div>
        """, unsafe_allow_html=True)
    except:
        st.warning("⚠️ 'simsek.png' dosyası bulunamadı! Lütfen klasöre ekle.")

    # Streamlit Butonu (Görünmez ama dokunmayı yakalayan alan)
    # Bu buton sayesinde "dokunma eylemi" kesin olarak çalışır.
    if st.button("⚡", use_container_width=True):
        st.session_state.giris_yapildi = True
        st.rerun()

# --- ANA SAYFA (Sadece giriş yapıldıysa görünür) ---
else:
    # Üst Kısım: Fotoğraf ve Başlık
    col1, col2 = st.columns([1, 3])
    with col1:
        try:
            img

import streamlit as st

def main():
    try:
        st.title("Utku'nun Portfolyosu")
        st.write("Hoş geldiniz!")
        # Diğer kodlarını buraya ekle
        
    except Exception as e:
        st.error(f"Sistemde bir hata oluştu: {e}")

if __name__ == "__main__":
    main()
    




