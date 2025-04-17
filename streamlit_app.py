import streamlit as st

st.set_page_config(
    page_title="Biljardin varausjärjestelmä",
    page_icon="🎱",
    layout="centered"
)

st.title("🎱 Biljardivarausjärjestelmä")

st.markdown("""
Tervetuloa varaamaan biljardivuoroja!

➡️ Käytä vasemman reunan valikkoa:
- **Tee varaus**: Pelaajat syöttävät nimensä ja 4-numeroisen tokenin
- **Varaukset ja pelin lopetus**: Näet nykyisen ja seuraavan peliparin, ja voit lopettaa pelin
- **QR-koodi**: Luo QR-koodi varauslomakkeelle
- **Ohjaaja**: Salasanalla suojattu näkymä päivän kaikkiin varauksiin
""")
