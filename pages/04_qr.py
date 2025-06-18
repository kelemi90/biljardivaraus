import streamlit as st
import qrcode
from io import BytesIO
import base64

st.set_page_config(page_title="QR-koodi varauslomakkeelle", page_icon="📱")

st.title("📱 QR-koodi varauslomakkeelle" \
" QR Code for Reservation Form")

# Kiinteä URL varauslomakkeelle
form_url = "http://<YOUR-RPI-ADDRESS>:8501/varaus"

# QR-koodin luonti
qr = qrcode.QRCode(box_size=10, border=2)
qr.add_data(form_url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Muunnetaan kuva base64-muotoon
buffered = BytesIO()
img.save(buffered)
img_b64 = base64.b64encode(buffered.getvalue()).decode()

# Näytetään QR-koodi
st.image(
    f"data:image/png;base64,{img_b64}",
    caption="Skannaa varauslomake" \
    "Scan the reservation form",
    use_container_width=True
)
