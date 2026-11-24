import streamlit as st
import pandas as pd
import time
from services import Service

class ManterCategoriaUI:
    def main():
        st.header("Cadastro de Categorias")
        tab1, tab2, tab3, tab4 = st.tabs(["Inserir categoria", "Listar categorias", "Atualizar categoria", "Excluir categoria"])
        with tab1: ManterCategoriaUI.inserir_categoria()
        with tab2: ManterCategoriaUI.listar_categoria()
        with tab3: ManterCategoriaUI.atualizar_categoria()
        with tab4: ManterCategoriaUI.excluir_categoria()

    def inserir_categoria():
        nome = st.text_input("Informe a categoria: ") 
        descricao = st.text_input("informe a descrição: ")
        if st.button("Inserir categoria"):
            Service.inserir_categoria(nome, descricao)
            st.success("Categoria inserida com sucesso!")
            time.sleep(2)
            st.rerun()

    def listar_categoria():
        categoria = Service.listar_categorias()
        if len(categoria) == 0: st.write("Nenhuma categoria cadastrada.")
        else:
            list_categoria = []
            for obj in categoria: list_categoria.append(obj.to_json())
            df = pd.DataFrame(list_categoria)
            st.dataframe(df)

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

    def excluir_categoria():
        categorias = Service.listar_categorias()
        if len(categorias) == 0: st.write("nenhum categoria cadastrado.")
        else:
            op = st.selectbox("Selecione o categoria para excluir", categorias)
            if st.button("Excluir categoria"):
                Service.excluir_categoria(op.get_id())
                st.success("categoria excluído com sucesso!")
                time.sleep(2)
                st.rerun()