import json
from Projeto.models.Produto import Produtos

class ProdutoDAO:
    def __init__(self):
        self.__arquivo = "PRODUTO.json"
        self.__objetos = []

    def salvar(self):
        with open(self.__arquivo, "w") as f:
            json.dump([p.to_json() for p in self.__objetos], f)

    def carregar(self):
        try:
            with open(self.__arquivo, "r") as f:
                data = json.load(f)
                self.__objetos = [Produtos.from_json(p) for p in data]
        except FileNotFoundError:
            pass

    def inserir(self, produtos):
        self.__objetos.append(produtos)
        self.salvar()

    def listar(self):
        return self.__objetos

    def atualizar(self, produtos):
        for i, p in enumerate(self.__objetos):
            if p.get_id() == produtos.get_id():
                self.__objetos[i] = produtos
                break
        self.salvar()

    def excluir(self, produtos):
        self.__objetos.remove(produtos)
        self.salvar()