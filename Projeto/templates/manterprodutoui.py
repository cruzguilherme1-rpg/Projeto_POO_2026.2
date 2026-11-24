import streamlit as st
import pandas as pd
import time
from services import Service

class ManterProdutoUI:
    def main():
        st.header("Cadastro de produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Inserir produto", "Listar produtos", "Atualizar produto", "Excluir produto"])
        with tab1: ManterProdutoUI.inserir_produto()
        with tab2: ManterProdutoUI.listar_produtos()
        with tab3: ManterProdutoUI.atualizar_produto()
        with tab4: ManterProdutoUI.excluir_produto()

    def inserir_produto():
        nome = st.text_input("Informe o nome: ")
        preco = st.text_input("Informe o preço: ")
        quantidade = st.text_input("Informe a quantidade: ")
        id_categoria = st.text_input("Informe o ID da categoria do produto: ")
        if st.button("Inserir produto"):
            Service.inserir_produto(nome, preco, quantidade, id_categoria)
            st.success("produto inserido com sucesso!")
            time.sleep(2)
            st.rerun()

    def listar_produtos():
        produtos = Service.listar_produtos()
        if len(produtos) == 0: st.write("Nenhum produto cadastrado.")
        else:
            list_produtos = []
            for obj in produtos: list_produtos.append(obj.to_json())
            df = pd.DataFrame(list_produtos)
            st.dataframe(df)

    def atualizar_produto():
        produtos = Service.listar_produtos()
        if len(produtos) == 0: st.write("nenhum produto cadastrado.")
        else:
            op = st.selectbox("Selecione o produto para atualizar", produtos)
            nome = st.text_input("Informe o nome: ", op.get_nome())
            preco = st.text_input("Informe o e-mail: ", op.get_preco())
            quantidade = st.text_input("Informe o quantidade: ", op.get_quantidade())
            id_categoria = st.text_input("Informe o ID da categoria do produto: ", op.get_id_produto())
            if st.button("Atualizar produto"):
                Service.atualizar_produto(op.get_id(), nome, preco, quantidade)
                st.success("produto atualizado com sucesso!")
                time.sleep(2)
                st.rerun()

    def excluir_produto():
        produtos = Service.listar_produtos()
        if len(produtos) == 0: st.write("nenhum produto cadastrado.")
        else:
            op = st.selectbox("Selecione o produto para excluir", produtos)
            if st.button("Excluir produto"):
                Service.excluir_produto(op.get_id())
                st.success("produto excluído com sucesso!")
                time.sleep(2)
                st.rerun()