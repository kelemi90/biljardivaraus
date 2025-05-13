# biljardivaraus
Nurkkaan suunniteltu biljardivaraus järjestelmä

# Muista aina!
uv init
uv sync
uv run streamlit run main.py --client.showSidebarNavigation=False

# Aja
streamlit run lomake.py --server.port 8501 --client.showSidebarNavigation=False
streamlit run varaukset.py --server.port 8502 --client.showSidebarNavigation=False
streamlit run ohjaaja.py --server.port 8503 --client.showSidebarNavigation=False
streamlit run qr.py --server.port 8504 --client.showSidebarNavigation=False
