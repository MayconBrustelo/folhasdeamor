import streamlit      as st
import pandas         as pd
#import plotly.express as px

st.set_page_config(page_title="Folhas de Amor S2",
                   layout="wide"
                    )
#st.set_page_config(backgroud="black")

df = pd.read_csv("FolhasDeAmor.csv", sep=";", decimal=",")

blankIndex1 =[''] * len(df)
df.index = blankIndex1
df = df.drop(columns=["Cod"])
df = df.drop(columns=["DT_COMP"])
df = df.drop(columns=["VL_COMP"])
df = df.drop(columns=["PORC_VEN"])
df = df.drop(columns=["VL_LUCRO"])
df = df.drop(columns=["VL_UNIT"])
df = df.drop(columns=["VL_VEND_TOT"])
df = df.drop(columns=["Vendeu"])
#df = df.drop(columns=["DT_VENDA"])
df = df.drop(columns=["QTD_VEND"])

#display(df.head())

df = df.sort_values("Descrição")

Grupo = st.sidebar.selectbox("Grupo", df["Grupo"].unique())

df_filtered = df[df["Grupo"] == Grupo]
df_filtered
