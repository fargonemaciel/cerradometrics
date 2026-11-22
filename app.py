import streamlit as st

st.set_page_config(
    page_title="CerradoMetrics · Dados do DF",
    page_icon="assets/favicon.png",
)

st.logo("assets/logo.png", icon_image="assets/icone.png", size="large")

inicio = st.Page(
    "paginas/inicio.py", title="Início", icon=":material/home:", default=True
)
sobre = st.Page("paginas/sobre.py", title="Sobre", icon=":material/info:")

pg = st.navigation([inicio, sobre])
pg.run()
