from templates.manterclienteui import ManterClienteUI
from templates.manterprodutoui import ManterProdutoUI
from templates.mantercategoriaui import ManterCategoriaUI
from templates.reajustarprodutoui import ReajustarProdtuoUI

import streamlit as st 

class IndexUI:

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Cliente", "Cadastro de Produto", "Reajustes", "Cadastro de Categoria"])
        if op == "Cadastro de Cliente": ManterClienteUI.main()
        if op == "Cadastro de Produto": ManterProdutoUI.main()
        if op == "Reajustes": ReajustarProdtuoUI.main()
        if op == "Cadastro de Categoria": ManterCategoriaUI.main()

    def sidebar():
        IndexUI.menu_admin()

    def main():
        st.title("Sistema de Vendas")
        IndexUI.sidebar()

IndexUI.main()