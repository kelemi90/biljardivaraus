import streamlit as st
import qrcode
from io import BytesIO
import base64

st.set_page_config(page_title="QR-koodi varauslomakkeelle", page_icon="📱")

st.title("📱 QR-koodi varauslomakkeelle")

# Syötä tai muokkaa URL-osoitetta
form_url = st.text_input("Anna varauslomakkeen URL", "http://<YOUR-RPI-ADDRESS>:8501/varaus")

if form_url:
    # QR-koodin luonti
    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(form_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Muunnetaan kuva base64-muotoon näytettäväksi Streamlitissä
    buffered = BytesIO()
    img.save(buffered)
    img_b64 = base64.b64encode(buffered.getvalue()).decode()

    st.image(f"data:image/png;base64,{img_b64}", caption="Skannaa varauslomake", use_column_width=True)
    st.write("🔗 URL: ", form_url)
