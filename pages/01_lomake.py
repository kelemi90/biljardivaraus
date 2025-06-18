import streamlit as st
import json
import os
from datetime import date, datetime

TEMP_FILE = "reservations_temp.json"
LOG_FILE = "reservations_log.json"
ADMIN_PASSWORD = "salasana123"  # Vaihda haluamaksesi

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

st.markdown("# 🎱 Tee varaus \n # 🎱 Make a Reservation")

with st.form("varaus_form"):
    player1 = st.text_input("Pelaaja 1/Player 1")
    player2 = st.text_input("Pelaaja 2")
    token = st.text_input("Anna 4-numeroinen token (käytetään pelin lopetukseen)/Give 4-digit token (used to end game)", type="password")

    admin_needed = (
        player1.strip().lower() == "ohjaaja" or player2.strip().lower() == "ohjaaja"
    )

    admin_pass = ""
    if admin_needed:
        admin_pass = st.text_input("Syötä ohjaajan salasana", type="password")

    submit = st.form_submit_button("Varaa vuoro")

    if submit:
        if not (player1 and player2 and token.isdigit() and len(token) == 4):
            st.error("Täytä kaikki kentät oikein./Please fill all fields correctly.")
            st.stop()

        is_admin = admin_needed and (admin_pass == ADMIN_PASSWORD)
        if admin_needed and not is_admin:
            st.error("Väärä ohjaajan salasana.")
            st.stop()

        # Estetään peräkkäinen varaus, jos ei ole ohjaaja
        if not is_admin and len(temp_data["reservations"]) > 0:
            last = temp_data["reservations"][-1]
            last_players = [p.strip().lower() for p in last["players"].split("&")]
            if player1.strip().lower() in last_players or player2.strip().lower() in last_players:
                st.warning("Et voi varata kahta vuoroa peräkkäin./")
                st.stop()

        new_entry = {
                "players": f"{player1.strip()} & {player2.strip()}",
                "creator": player1.strip() if not is_admin else "OHJAAJA",
                "token": token,
                "date": today,
                "start_time": datetime.now().strftime("%H:%M:%S"),
                "end_time": None
            }

        temp_data["reservations"].append(new_entry)
        log_data["reservations"].append(new_entry)

        save_data(temp_data, TEMP_FILE)
        save_data(log_data, LOG_FILE)

        st.success("Varaus tehty onnistuneesti!" \
        "Reservation made successfully!")
