import streamlit as st
import json
import os
from datetime import date

TEMP_FILE = "reservations_temp.json"
LOG_FILE = "reservations_log.json"
today = str(date.today())

# Ladataan tai alustetaan tiedostot
def load_data(file):
    if not os.path.exists(file):
        return {"date": today, "reservations": []}
    with open(file, "r") as f:
        return json.load(f)

def save_data(data, file):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)

temp_data = load_data(TEMP_FILE)
log_data = load_data(LOG_FILE)

# Nollataan vanhat varaukset, jos päivä on vaihtunut
if temp_data.get("date") != today:
    temp_data = {"date": today, "reservations": []}
    save_data(temp_data, TEMP_FILE)

if log_data.get("date") != today:
    log_data = {"date": today, "reservations": []}
    save_data(log_data, LOG_FILE)

st.title("🎱 Tee varaus")

with st.form("varaus_form"):
    player1 = st.text_input("Pelaaja 1")
    player2 = st.text_input("Pelaaja 2")
    token = st.text_input("Anna 4-numeroinen token (käytetään pelin lopetukseen)", type="password")
    submit = st.form_submit_button("Varaa vuoro")

    if submit:
        if not (player1 and player2 and token.isdigit() and len(token) == 4):
            st.error("Täytä kaikki kentät oikein.")
        else:
            if len(temp_data["reservations"]) > 0:
                last = temp_data["reservations"][-1]
                last_players = [p.strip().lower() for p in last["players"].split("&")]
                if player1.strip().lower() in last_players or player2.strip().lower() in last_players:
                    st.warning("Et voi varata kahta vuoroa peräkkäin.")
                    st.stop()

            new_entry = {
                "players": f"{player1.strip()} & {player2.strip()}",
                "creator": player1.strip(),
                "token": token,
                "date": today
            }

            temp_data["reservations"].append(new_entry)
            log_data["reservations"].append(new_entry)

            save_data(temp_data, TEMP_FILE)
            save_data(log_data, LOG_FILE)

            st.success("Varaus tehty onnistuneesti!")
