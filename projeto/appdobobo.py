import streamlit as st
import funcoes  # pyright: ignore[reportMissingImports]


st.image("https://i.pinimg.com/originals/4f/e0/08/4fe008e3993dc13bd310ad8225c2fcf0.gif")
st.title("Meu site ✌️🌞")
st.subheader("Criado com Streamlit 🌚🤙")

st.markdown("""
# Grampus\n
*Marque já e de bonus ganhe uma etiqueta*\n
**30% de desconto para quem tiver ideia origi**
                    
""")

st.title("Calculadora IMC 🧠")
peso = st.number_input("Digite seu peso",min_value=0.0)
altura = st.number_input("Digite sua altura",min_value=0.0)
btn_calcular = st.button("Calcular")

if btn_calcular:
    imc = funcoes.calcular_imc(peso,altura)
    st.success(imc)
