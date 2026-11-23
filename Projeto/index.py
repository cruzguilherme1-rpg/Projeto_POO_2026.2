from templates.manterclienteui import ManterClienteUI


import streamlit as st 

class IndexUI:

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Manter Cliente", "Manter Venda", "Manter Produto", "Manter Categoria"])
        if op == "Manter Cliente": ManterClienteUI.main()

    def sidebar():
        IndexUI.menu_admin()

    def main():
        st.title("Sistema de Vendas")
        IndexUI.sidebar()

IndexUI.main()