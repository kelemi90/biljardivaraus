import streamlit as st
import importlib.util
from pathlib import Path

# Määrittele saatavilla olevat sivut ja niiden tiedostopolut
# pages = {
#     "lomake": "sivu_lomake.py",
#     "varaukset": "sivu_varaukset.py",
#     "ohjaaja": "sivu_ohjaaja.py",
#     "qr": "sivu_qr.py"
# }

# Hae URL-parametri ?page=...
query_params = st.query_params
page = query_params.get("page", [None])[0]

# # Jos parametrina on tunnettu sivu, ladataan se dynaamisesti
# if page in pages:
#     filepath = Path(pages[page])
#     if filepath.exists():
#         spec = importlib.util.spec_from_file_location("module.name", filepath)
#         module = importlib.util.module_from_spec(spec)
#         spec.loader.exec_module(module)
#     else:
#         st.error(f"Sivua '{page}' ei löytynyt.")
# else:
#     # Jos ei ole parametria tai tuntematon sivu
#     st.title("🎱 Biljardivarausjärjestelmä")
#     st.markdown("""
#     Käytä näitä URL-osoitteita:

#     - `/streamlit_app.py?page=lomake` – Pelaajien varauslomake  
#     - `/streamlit_app.py?page=varaukset` – Käynnissä olevat pelit & "Peli päättyi"  
#     - `/streamlit_app.py?page=ohjaaja` – Ohjaajan näkymä  
#     - `/streamlit_app.py?page=qr` – QR-koodin generointi  
#     """)
