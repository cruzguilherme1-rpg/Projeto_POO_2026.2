from templates.manterclienteui import ManterClienteUI
from templates.manterprodutoui import ManterProdutoUI
from templates.mantercategoriaui import ManterCategoriaUI

import streamlit as st 

class ReajustarProdtuoUI: 
    def main():
        st.header("Reajuste de cliente, produtos e categorias,")
        tab1, tab2, tab3 = st.tabs(["Atualizar Cliente", "Atualizar produto","Atualizar categoria"])
        with tab1: ManterClienteUI.atualizar_cliente()
        with tab2: ManterProdutoUI.atualizar_produto()
        with tab3: ManterCategoriaUI.atualizar_categoria()


    def atualizar_cliente():
        clientes = Service.listar_clientes()
        if len(clientes) == 0: st.write("nenhum cliente cadastrado.")
        else:
            op = st.selectbox("Selecione o cliente para atualizar", clientes)
            nome = st.text_input("Informe o nome: ", op.get_nome())
            email = st.text_input("Informe o e-mail: ", op.get_email())
            fone = st.text_input("Informe o fone: ", op.get_fone())
            if st.button("Atualizar Cliente"):
                Service.atualizar_cliente(op.get_id(), nome, email, fone)
                st.success("Cliente atualizado com sucesso!")
                time.sleep(2)
                st.rerun()

    def atualizar_categoria():
        categorias = Service.listar_categorias()
        if len(categorias) == 0: st.write("nenhum categoria cadastrado.")
        else:
            op = st.selectbox("Selecione o categoria para atualizar", categorias)
            nome = st.text_input("Informe o nome: ", op.get_nome())
            descricao = st.text_input("Informe a descrição: ", op.get_descricao())
            if st.button("Atualizar categoria"):
                Service.atualizar_categoria(op.get_id(), nome, descricao)
                st.success("categoria atualizado com sucesso!")
                time.sleep(2)
                st.rerun()

    def atualizar_produto():
        produtos = Service.listar_produtos()
        if len(produtos) == 0: st.write("nenhum produto cadastrado.")
        else:
            op = st.selectbox("Selecione o produto para atualizar", produtos)
            nome = st.text_input("Informe o nome: ", op.get_descricao())
            preco = st.number_input("Informe o preço: ", min_value=0.0, value=float(op.get_preco()), step=0.01, format="%.2f")
            quantidade = st.number_input("Informe a quantidade: ", min_value=1, value=int(op.get_estoque()), step=1)
            id_categoria = st.number_input("Informe o ID da categoria do produto: ", min_value=1, value=int(op.get_id_categoria()), step=1)
            if st.button("Atualizar produto"):
                Service.atualizar_produto(op.get_id(), nome, preco, quantidade, id_categoria)
                st.success("produto atualizado com sucesso!")
                time.sleep(2)
                st.rerun()