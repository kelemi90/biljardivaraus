import streamlit as st
import qrcode
from io import BytesIO
import base64

st.title("📱 QR-koodi varauslomakkeelle")

# Lomakkeen URL, muuta tarvittaessa oikeaksi osoitteeksi
form_url = "http://<YOUR-RPI-ADDRESS>:8501/varaus"

# QR-koodin luonti
qr = qrcode.QRCode(box_size=10, border=2)
qr.add_data(form_url)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")

# Näytetään QR-koodi
buffered = BytesIO()
img.save(buffered)
img_b64 = base64.b64encode(buffered.getvalue()).decode()

st.image(f"data:image/png;base64,{img_b64}", caption="Skannaa varauslomake", use_column_width=True)
st.write("URL: ", form_url)
