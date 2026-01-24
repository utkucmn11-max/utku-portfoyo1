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
# Kullanıcının giriş yapıp yapmadığını tutar. Uygulama her yenilendiğinde bu bilgi kalır.
if 'giris_yapildi' not in st.session_state:
    st.session_state.giris_yapildi = False

# --- GÖRSELİ BASE64 OLARAK KODA GÖMME ---
# Streamlit'in harici görsel dosyalarını doğrudan yükleyemediği durumlarda kullanışlıdır.
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"⚠️ Görsel dosyası '{image_path}' bulunamadı. Lütfen klasöre ekle.")
        return None
    except Exception as e:
        st.error(f"Görsel yüklenirken bir hata oluştu: {e}")
        return None

# --- CSS VE ANİMASYONLAR (Tüm uygulama için geçerli) ---
st.markdown("""
    <style>
    /* Streamlit'in varsayılan sidebar'ını gizle (giriş ekranında) */
    [data-testid="stSidebar"] { display: none; }
    
    /* Ana uygulama arka plan rengi */
    .stApp { background-color: #ffffff; color: #1a1a1a; }
    
    /* Giriş ekranı kapsayıcısı */
    .cover-container {
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        background-color: white;
        z-index: 9999; /* En üstte görünmesini sağlar */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    /* Şimşek Logosu stili */
    .bolt-img {
        width: 300px; /* Logo boyutu */
        cursor: pointer; /* Tıklanabilir olduğunu belirtir */
        transition: transform 0.3s ease; /* Fare üzerine gelince yumuşak geçiş */
    }

    .bolt-img:hover {
        transform: scale(1.1) rotate(5deg); /* Fare üzerine gelince büyü ve dön */
    }

    /* Tıklama ipucu yazısı */
    .click-hint {
        margin-top: 20px;
        color: #DAA520; /* Sarı renk */
        font-weight: bold;
        letter-spacing: 2px;
        animation: blink 1.5s infinite; /* Yanıp sönme animasyonu */
    }

    @keyframes blink { 
        0% {opacity: 0.3;} 
        50% {opacity: 1;} 
        100% {opacity: 0.3;} 
    }
    
    /* Genel Bilgi Kutuları */
    .info-box {
        background-color: #f0f2f6; /* Hafif gri arka plan */
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        min-height: 180px; /* Kutuların aynı hizada olmasını sağlar */
    }
    .info-box h3 {
        color: #000000;
        margin-top: 0;
        margin-bottom: 15px;
    }
    .info-box ul {
        list-style-type: disc; /* Liste işaretlerini disk olarak ayarlar */
        padding-left: 20px;
    }
    .info-box p, .info-box li {
        color: #333333;
        line-height: 1.6;
    }# CSS kodlarının bittiği yer (temsili)
    </style>
    """, unsafe_allow_html=True) # İşte bu satırı eklemelisin



