from templates.manterclienteui import ManterClienteUI
from templates.manterprodutoui import ManterProdutoUI
from templates.mantercategoriaui import ManterCategoriaUI


import streamlit as st 

class IndexUI:

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Cliente", "Cadastro de Produto", "Reajustar Produto", "Cadastro de Categoria"])
        if op == "Cadastro de Cliente": ManterClienteUI.main()
        if op == "Cadastro de Produto": ManterProdutoUI.main()
        if op == "Reajustar Produto": ReajustarProdtuoUI.main()
        if op == "Cadastro de Categoria": ManterCategoriaUI.main()

    def sidebar():
        IndexUI.menu_admin()

    def main():
        st.title("Sistema de Vendas")
        IndexUI.sidebar()

IndexUI.main()