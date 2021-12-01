#importamos streamlit , pandas , matplotlib y numpy

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Visualización de los datos covid 19 chile ")

st.markdown("### Bienvenido al visualizador")

df = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/TotalesPorRegion.csv")

col1,col2=st.columns(2)

with col1:
    region=st.radio("Region", df.Region.unique())
    st.markdown("su seleccion es: " + region)
 
with col2:
    categoria=st.radio("Categoría", df.Categoria.unique())
    st.markdown("su seleccion es: " + categoria)



#ilocs=df.iloc[:,2:-1]
superfiltro=df[(df.Region==region)&(df.Categoria==categoria) ]
#st.table(superfiltro)

fig,ax = plt.subplots()

to_plot=superfiltro.iloc[:,2:-1]

ax.plot(to_plot.T)
ax.set_title(region)
ax.set_ylabel(categoria)
ax.set_xlabel("Fecha")
xs= np.arange(0,superfiltro.shape[1]-2,30)
plt.xticks(xs,rotation=90)

st.pyplot(fig)

