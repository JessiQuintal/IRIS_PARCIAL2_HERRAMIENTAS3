import pandas as pd
import streamlit as st
import os
import importlib

hide_streamlit_style= """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Análisis estadistico de Iris Dataset")
st.header("En las siguientes páginas se presentan estadísticas, gráficas y modelo.")


pages = [f[:-3] for f in os.listdir("Clasificacion/Clasificacion/Pages") if f.endswith(".py")]
selection = st.sidebar.radio("Pages:", pages)
page_module = importlib.import_module(f"Pages.{selection}")
page_module.show()