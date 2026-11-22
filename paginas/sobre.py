import streamlit as st

st.title("Sobre o projeto")

st.markdown("""
### Por que o CerradoMetrics existe

Dado público que só existe em tabela não é informação verdadeiramente pública.
O Distrito Federal publica muitos dados abertos, mas quase ninguém consegue
tirar respostas deles. O CerradoMetrics transforma essas tabelas em respostas
legíveis sobre a vida no DF.

### Como funciona

Cada página responde a uma pergunta concreta, com números comparáveis e uma
seção explicando o que os dados **não** dizem. Só uso fontes oficiais e
abertas, sempre com link para o dado bruto.

### O que vem primeiro

**Saúde:** onde se concentram as reclamações sobre o SUS e sobre os planos
de saúde no DF.

### Quem faz

**Fargone Maciel**, cientista de dados. Passo os dias transformando bases
de dados em decisões, e o CerradoMetrics é onde faço isso com os dados
do lugar onde eu vivo.
""")

col1, col2 = st.columns(2)
col1.link_button(
    "LinkedIn", "https://www.linkedin.com/in/fargonemaciel/", use_container_width=True
)
col2.link_button("GitHub", "https://github.com/fargonemaciel", use_container_width=True)
