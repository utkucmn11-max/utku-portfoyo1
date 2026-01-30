# 1. Önce CSS kısmına neon efektini tanımlayan class'ı ekleyelim
# (st.markdown içindeki <style> bloğunun içine ekle)

neon_style = """
<style>
    .neon-border {
        border: 2px solid #ffff00 !important;
        box-shadow: 0 0 15px #ffff00, 0 0 30px #ffff00, inset 0 0 10px #ffff00 !important;
        transition: all 0.6s ease-in-out;
    }
</style>
"""
st.markdown(neon_style, unsafe_allow_html=True)

# 2. Enerji durumuna göre class ismini belirle
# Bu değişken butonun durumuna göre "neon-border" metnini alacak
neon_active_class = "neon-border" if st.session_state.bolt_on else ""

# 3. Uzmanlık ve İletişim bölümünde bu değişkeni kullan
c1, c2 = st.columns(2)

with c1:
    # f-string kullanarak neon_active_class'ı div'in içine gömüyoruz
    st.markdown(f"""
        <div class="info-box {neon_active_class}">
            <h3>🛠️ Uzmanlık Alanları</h3>
            <ul>
                <li>Elektrik Devre Tasarımı</li>
                <li>Elektronik Bakım & Onarım</li>
                <li>Python ile Otomasyon</li>
                <li>3D Printer Model & Baskı</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with c2:
    linkedin_url = "https://www.linkedin.com/in/utkucimen" 
    st.markdown(f"""
        <div class="info-box {neon_active_class}">
            <h3>📫 İletişim</h3>
            <p>📧 <b>E-posta:</b> utkucmn11@gmail.com</p>
            <p>📸 <b>Instagram:</b> <a href="https://www.instagram.com/59.utkucimen_/" target="_blank" style="color:#ffff00; text-decoration:none;">@59.utkucimen_</a></p>
            <p>💼 <b>LinkedIn:</b> <a href="{linkedin_url}" target="_blank" style="color:#ffff00; text-decoration:none;">Utku Çimen</a></p>
        </div>
    """, unsafe_allow_html=True)
