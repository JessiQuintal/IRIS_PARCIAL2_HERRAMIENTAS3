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


# Obtener todas las páginas .py en la carpeta Pages
pages = [f[:-3] for f in os.listdir("Clasificacion/Pages") if f.endswith(".py")]

# Agregar la página seleccionada a la barra lateral
selection = st.sidebar.radio("Pages:", pages)

# Importar la página seleccionada y ejecutarla
page_module = importlib.import_module(f"Pages.{selection}")
page_module.show()