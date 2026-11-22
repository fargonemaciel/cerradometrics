import streamlit as st

st.title("O DF publica muitos dados. Aqui eles viram respostas.")

st.markdown(
    "O **CerradoMetrics** transforma dados públicos do Distrito Federal "
    "em respostas claras sobre saúde, mobilidade e o dia a dia de quem vive aqui."
)

if st.button("Conheça o projeto", type="primary"):
    st.switch_page("paginas/sobre.py")

st.divider()
st.subheader("O que está sendo construído")

col1, col2, col3 = st.columns(3)

with col1.container(border=True):
    st.markdown("#### :material/medical_services: Saúde")
    st.badge("Em produção", color="primary")
    st.write("Onde o SUS e os planos de saúde mais geram reclamação no DF?")

with col2.container(border=True):
    st.markdown("#### :material/directions_bus: Mobilidade")
    st.badge("Próximo", color="gray")
    st.write("Transporte público e deslocamento no DF.")

with col3.container(border=True):
    st.markdown("#### :material/add_circle: E mais")
    st.badge("Em breve", color="gray")
    st.write("Novos temas a partir dos dados abertos do DF.")

st.divider()
st.caption("Atualizado em 21/11/2026 · Dados abertos e oficiais do Distrito Federal")
