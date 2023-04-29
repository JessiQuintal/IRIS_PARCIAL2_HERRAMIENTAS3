import pandas as pd
import streamlit as st
import streamlit.components.vl as components
hide_streamlit_style= """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
URL= 'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'
dfIris= pd.read_csv(URL)

print(dfIris.head())
st.title("Análisis estadistico de Iris Dataset")
st.header("Estadisticas")
st.write("Filas, Columnas:")
st.write(dfIris.shape)

st.write("Describe:")
st.dataframe(dfIris.describe())

st.write("Clases:")
st.write(dfIris["variety"].value_counts())