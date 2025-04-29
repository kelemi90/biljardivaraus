import streamlit as st
import json
import os
from datetime import date, datetime

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

def save_reservations(data, file):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)

# Tiedot
temp_data = load_reservations(TEMP_FILE)
log_data = load_reservations(LOG_FILE)

st.subheader("📋 Käynnissä ja tulevat varaukset (temp)")
for i, res in enumerate(temp_data["reservations"]):
    st.write(
        f"{i+1}. {res['players']} – Token: {res['token']} – Aloitettu: {res.get('start_time', '???')} – Päättynyt: {res.get('end_time', '-')}"
    )
    if res.get("end_time") is None:
        if st.button(f"Merkitse päättyneeksi: {res['token']}", key=f"end_{i}"):
            temp_data["reservations"][i]["end_time"] = datetime.now().strftime("%H:%M:%S")
            for log_entry in log_data["reservations"]:
                if log_entry["token"] == res["token"]:
                    log_entry["end_time"] = temp_data["reservations"][i]["end_time"]
            save_reservations(temp_data, TEMP_FILE)
            save_reservations(log_data, LOG_FILE)
            st.rerun()

st.divider()

st.subheader("🗃️ Päivän kaikki varaukset (log)")
for i, res in enumerate(log_data["reservations"]):
    st.write(
        f"{i+1}. {res['players']} – Token: {res['token']} – Aloitettu: {res.get('start_time', '???')} – Päättynyt: {res.get('end_time', '-')}"
    )

# Mahdollisuus tyhjentää päivän varaukset
if st.button("🧹 Tyhjennä tämän päivän varaukset"):
    temp_data["reservations"] = []
    log_data["reservations"] = []
    save_reservations(temp_data, TEMP_FILE)
    save_reservations(log_data, LOG_FILE)
    st.success("Kaikki tämän päivän varaukset poistettu.")
