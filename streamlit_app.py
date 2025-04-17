import streamlit as st
import urllib.parse
from pathlib import Path

# Määrittele käytettävät sivut
pages = {
    "lomake": "sivu_lomake.py",
    "varaukset": "sivu_varaukset.py",
    "ohjaaja": "sivu_ohjaaja.py",
    "qr": "sivu_qr.py"
}

# Ota page-parametri URL:sta
query_params = st.query_params
page = query_params.get("page", [None])[0]

# Aja haluttu sivu
if page in pages:
    file = Path(pages[page])
    if file.exists():
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        exec(code, globals())  # Ajetaan valittu sivu
    else:
        st.error("Sivua ei löytynyt.")
else:
    # Etusivu, jos ei page-parametria
    st.title("🎱 Biljardivarausjärjestelmä")
    st.markdown("""
    Käytä suoraa osoitetta:

    - `/streamlit_app.py?page=lomake` – Tee varaus
    - `/streamlit_app.py?page=varaukset` – Näytä varaukset ja lopeta peli
    - `/streamlit_app.py?page=ohjaaja` – Ohjaajan näkymä
    - `/streamlit_app.py?page=qr` – QR-koodin generointi
    """)
