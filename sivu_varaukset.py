import streamlit as st
import json
import os
from datetime import date

TEMP_FILE = "reservations_temp.json"

def load_data(file):
    if not os.path.exists(file):
        return {"date": str(date.today()), "reservations": []}
    with open(file, "r") as f:
        return json.load(f)

def save_data(data, file):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)

st.title("🎮 Käynnissä oleva peli ja varaukset")

temp_data = load_data(TEMP_FILE)

if len(temp_data["reservations"]) == 0:
    st.info("Ei käynnissä olevia varauksia.")
    st.stop()

current = temp_data["reservations"][0]
st.subheader("Nyt pelaa:")
st.write(f"**{current['players']}**")

# Peli päättyi
if "end_open" not in st.session_state:
    st.session_state.end_open = False

if not st.session_state.end_open:
    if st.button("Peli päättyi!"):
        st.session_state.end_open = True
else:
    name = st.text_input("Syötä oma nimesi (pelaaja 1 tai 2)")
    token_input = st.text_input("Syötä token", type="password")
    if st.button("Vahvista lopetus"):
        if name.strip().lower() in current["players"].lower() and token_input == current["token"]:
            temp_data["reservations"].pop(0)
            save_data(temp_data, TEMP_FILE)
            st.success("Peli päättyi ja varaus poistettu.")
            st.session_state.end_open = False
        else:
            st.error("Nimi tai token ei täsmää.")

st.divider()

st.subheader("⏭️ Seuraava pari")
if len(temp_data["reservations"]) > 1:
    st.write(temp_data["reservations"][1]["players"])
else:
    st.write("Ei vielä seuraavaa paria.")
