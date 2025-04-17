import streamlit as st
import json
import os
from datetime import date

TEMP_FILE = "reservations_temp.json"
LOG_FILE = "reservations_log.json"
PASSWORD = "salasana123"  # Vaihda omaan salasanaan

st.title("🛠️ Ohjaajan hallintasivu")

# Salasanatarkistus
password = st.text_input("Syötä ohjaajan salasana", type="password")
if password != PASSWORD:
    st.warning("Kirjoita oikea salasana nähdäksesi sisällön.")
    st.stop()

# Tiedostojen luku
def load_reservations(file):
    if not os.path.exists(file):
        return {"date": str(date.today()), "reservations": []}
    with open(file, "r") as f:
        return json.load(f)

# Tiedot
temp_data = load_reservations(TEMP_FILE)
log_data = load_reservations(LOG_FILE)

st.subheader("📋 Käynnissä ja tulevat varaukset (temp)")
for i, res in enumerate(temp_data["reservations"]):
    st.write(f"{i+1}. {res['players']} – Token: {res['token']}")

st.divider()

st.subheader("🗃️ Päivän kaikki varaukset (log)")
for i, res in enumerate(log_data["reservations"]):
    st.write(f"{i+1}. {res['players']} – Token: {res['token']}")

# Mahdollisuus tyhjentää päivän varaukset
if st.button("🧹 Tyhjennä tämän päivän varaukset"):
    temp_data["reservations"] = []
    log_data["reservations"] = []
    with open(TEMP_FILE, "w") as f:
        json.dump(temp_data, f, indent=2)
    with open(LOG_FILE, "w") as f:
        json.dump(log_data, f, indent=2)
    st.success("Kaikki tämän päivän varaukset poistettu.")
