# biljardivaraus
Nurkkaan suunniteltu biljardivaraus järjestelmä

# Muista aina!
source billiardi_env/bin/activate

# Aja
streamlit run sivu_lomake.py --server.port 8501
streamlit run sivu_varaukset.py --server.port 8502
streamlit run sivu_ohjaaja.py --server.port 8503
streamlit run sivu_qr.py --server.port 8504
