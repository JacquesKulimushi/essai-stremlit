import streamlit as st
from datetime import datetime
# interface streamlite
st.title("Afficheur de Date et heure")
st.write("cliquez sur le bouton ci-dessous pour afficher la date et l\'heure actuelles.")

if st.button("Afficher Date et Heure"): #obtenir la date et l'heure actuelles
    # obtenir la date et l'heure actuelles
    now = datetime.now()
    curent_time = now.strftime("%Y-%m-%d-%H: %M:%S")
    st.write(f"Date et Heure actuelles :{curent_time}")