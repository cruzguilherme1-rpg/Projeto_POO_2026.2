from datetime import datetime
from models.Cliente import Cliente
from models.ClienteDAO import ClienteDAO
from models.vendas import Venda
from models.vendaDAO import VendaDAO
from models.Produto import Produtos
from models.ProdutoDAO import ProdutoDAO
from models.categoria import Categoria
from models.categoriaDAO import CategoriaDAO


#coisas do cliente
class Service:
    @staticmethod
    def inserir_cliente(nome, email, fone):
        c = Cliente(0, nome, email, fone)
        ClienteDAO().inserir(c)

    @staticmethod
    def listar_clientes():
        return ClienteDAO().listar()

    @staticmethod
    def atualizar_cliente(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(c)

    @staticmethod
    def excluir_cliente(id):
        ClienteDAO().excluir(id)

#coisas das vendas

    @staticmethod
    def inserir_venda(carrinho, total, id_cliente):
        v = Venda(0, datetime.now(), carrinho, total, id_cliente)
        VendaDAO().inserir(v)
    
    @staticmethod
    def listar_vendas():
        return VendaDAO().listar()

    @staticmethod
    def listar_vendas_por_id(id):
        return VendaDAO().listar_id(id)

    @staticmethod
    def atualizar_venda(id, data, carrinho, total, id_cliente):
        v = Venda(id, data, carrinho, total, id_cliente)
        VendaDAO().atualizar(v)

    @staticmethod
    def excluir_venda(id):
        VendaDAO().excluir(id)

#coisas dos produtos

    @staticmethod
    def inserir_produto(nome, preco, quantidade, id_categoria):
        dao = ProdutoDAO()
        id_produto = max((p.get_id() for p in dao.listar()), default=0) + 1
        p = Produtos(id_produto, nome, preco, quantidade, id_categoria)
        dao.inserir(p)

    @staticmethod
    def listar_produtos():
        return ProdutoDAO().listar()

    @staticmethod
    def atualizar_produto(id, nome, preco, quantidade, id_categoria):
        p = Produtos(id, nome, preco, quantidade, id_categoria)
        ProdutoDAO().atualizar(p)

    @staticmethod
    def excluir_produto(id):
        ProdutoDAO().excluir(id)

#coisas das categorias

    @staticmethod
    def inserir_categoria(nome, descricao):
        c = Categoria(nome, 1, descricao)
        CategoriaDAO().inserir(c)

    @staticmethod
    def listar_categorias():
        return CategoriaDAO().listar()

    @staticmethod
    def atualizar_categoria(id, nome, descricao):
        c = Categoria(nome, id, descricao)
        CategoriaDAO().atualizar(c)

    @staticmethod
    def excluir_categoria(id):
        CategoriaDAO().excluir(id)

#Adm/Usuario

    @staticmethod
    def cliente_criar_admin():
        for c in Service.listar_clientes():
            if c.get_email() == "admin": return
        Service.cliente_inserir("admin", "admin", "fone", "1234")

    @staticmethod
    def cliente_autenticar(email, senha):
        for c in Service.listar_clientes():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None

    