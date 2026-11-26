import streamlit as st
import pandas as pd
import time
from services import Service

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Inserir Cliente", "Listar Clientes", "Atualizar Cliente", "Excluir Cliente"])
        with tab1: ManterClienteUI.inserir_cliente()
        with tab2: ManterClienteUI.listar_clientes()
        with tab3: ManterClienteUI.atualizar_cliente()
        with tab4: ManterClienteUI.excluir_cliente()

    def inserir_cliente():
        nome = st.text_input("Informe o nome: ")
        email = st.text_input("Informe o e-mail: ")
        fone = st.text_input("Informe o fone: ")
        senha = st.text_input("Informe a senha: ", type="password")
        if st.button("Inserir Cliente"):
            Service.inserir_cliente(nome, email, fone, senha)
            st.success("Cliente inserido com sucesso!")
            time.sleep(2)
            st.rerun()

    def listar_clientes():
        clientes = Service.listar_clientes()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado.")
        else:
            list_clientes = []
            for obj in clientes: list_clientes.append(obj.to_json())
            df = pd.DataFrame(list_clientes)
            st.dataframe(df)

    def atualizar_cliente():
        clientes = Service.listar_clientes()
        if len(clientes) == 0: st.write("nenhum cliente cadastrado.")
        else:
            op = st.selectbox("Selecione o cliente para atualizar", clientes)
            nome = st.text_input("Informe o nome: ", op.get_nome())
            email = st.text_input("Informe o e-mail: ", op.get_email())
            fone = st.text_input("Informe o fone: ", op.get_fone())
            senha = st.text_input("Nova senha: ", op.get_senha(), type="password")
            if st.button("Atualizar Cliente"):
                Service.atualizar_cliente(op.get_id(), nome, email, fone)
                st.success("Cliente atualizado com sucesso!")
                time.sleep(2)
                st.rerun()

    def excluir_cliente():
        clientes = Service.listar_clientes()
        if len(clientes) == 0: st.write("nenhum cliente cadastrado.")
        else:
            op = st.selectbox("Selecione o cliente para excluir", clientes)
            if st.button("Excluir Cliente"):
                Service.excluir_cliente(op.get_id())
                st.success("Cliente excluído com sucesso!")
                time.sleep(2)
                st.rerun()