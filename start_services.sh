
#!/bin/bash

# source /home/kipe/biljardivaraus/.venv/bin/activate

# echo "Käynnistetään: lomake"
# streamlit run /home/kipe/biljardivaraus/pages/01_lomake.py --server.port 8501 &

# echo "Käynnistetään: varaukset"
# streamlit run /home/kipe/biljardivaraus/pages/02_varaukset.py --server.port 8502 &

# echo "Käynnistetään: ohjaaja"
# streamlit run /home/kipe/biljardivaraus/pages/03_ohjaaja.py --server.port 8503 &

# echo "Käynnistetään: qr"
# streamlit run /home/kipe/biljardivaraus/pages/04_qr.py --server.port 8504 &

echo "Käynnistetään: main"
uv run streamlit run /home/kipe/biljardivaraus/etusivu.py --client.showSidebarNavigation=true &
