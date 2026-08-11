import streamlit as st
import requests
import json
import BuscarCep
import pandas as pd


##### TÍTULO DA APLICAÇÃO #####



##### Lista de Opções #####

opcoes = ["Buscar CEP", "Descobrir CEP"]



##### BARRA LATERAL #####
st.sidebar.title("Busca CEP")
st.image("logo.png", width=400)
st.sidebar.write("Aplicação para buscar endereço a partir do CEP e mostrar localização no mapa.")
escolha =st.sidebar.selectbox("Escolha uma Opção: ",opcoes)
##### BOTÃO BUSCAR CEP #####
if escolha == "Buscar CEP":
    st.header("Buscar endereço pelo CEP")
    cep = st.text_input("digite o CEP (somente numero):")

    if st.button("Buscar"):
        if len(cep) !=8 or not cep.isdigit():
            st.error("por favor, insira um CEP válido com 8 digitos numericos")
        else:
            try:
                endereco = BuscarCep.buscar_cep(cep)
                if endereco:
                    st.success("Endereço encontrado:")
                    st.write(f"CEP: {endereco[0]}")
                    st.write(f"endereço: {endereco[1]}")
                    st.write(f"bairro: {endereco[2]}")
                    st.write(f"Cidade: {endereco[3]}")
                    st.write(f"estado: {endereco[4]}")


                    st.title("Localização no mapa")
                    st.title("Localização no mapa")
                    df = pd.DataFrame({"Latitude": [endereco[5]], "longitude": [endereco[6]]})
                    st.map(df, zoom=15)
                else:
                    st.error("CEP não encontrado.")
            except Exception as e:
                st.error(f"Ocorreu um erro ao buscar o CEP: {e}")

##### BOTÃO DESCOBRIR CEP #####
elif escolha == "descobri CEP":
    st.header("Descobrir CEP pelo endereço")
    endereco_usuario = st.text_input("Digite o endereço (ex: Rua olga, Barueri, SP:)")

    if st.button("descobrir"):
        if not endereco_usuario.strip():
            st.error("Por favor, digite um endereço valido.")
        else:
            try:
                resultado = BuscarCep.descobrir_cep(endereco_usuario)
                st.success("link de busca no Google:")
                st.write(resultado)
            except Exception as e:
                st.error(f"Ocorreu um erro ao descobrir um CEP: {e}")