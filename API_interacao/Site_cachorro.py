import streamlit as st
import requests

st.title("Photo Dog")
st.subheader("🐈🐶🐩🌭")

#Faz requisiçãp GET e guarda a resposta na variável "reposta"
resposta = requests.get("https://dog.ceo/api/breeds/image/random")
#Pega o JSON da resposta e guarda como dicionário em "dicionario_resposta"
dicionario_reposta = resposta.json()
#Acessa a chave "message" do dicionario_reposta e guarda o link da foto em
link_foto = dicionario_reposta["message"] #dicionario_resposta.get("message") funcionaria também



if st.button("Nova Foto Aleatória"):
    resposta = requests.get("https://dog.ceo/api/breeds/image/random")
    link_foto = resposta.json()["message"] 
    link_foto = st.button(link_foto)
    #st.image(link_foto)