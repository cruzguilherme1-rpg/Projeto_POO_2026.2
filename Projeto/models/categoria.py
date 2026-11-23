class Categoria:
    def __init__(self, nome, id, descricao):
        self.set_nome(nome)
        self.set_id(id)
        self.set_descricao(descricao)

    def __str__(self):
        return f"{self.get_nome()} - {self.get_id()} - {self.get_descricao()}"
    
    def set_id(self, id):
        if id <= 0:
            raise ValueError("ID não pode ser negativo")
        self.__id = id

    def set_descricao(self, descricao):
        if descricao == "":
            raise ValueError("Descrição não pode ser vazia")
        self.__descricao = descricao

    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Nome não pode ser vazio")
        self.__nome = nome

    def get_nome(self): return self.__nome

    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao

    def to_json(self):
        CATEGORIA = {}
        CATEGORIA["nome"] = self.get_nome()
        CATEGORIA["id"] = self.get_id()
        CATEGORIA["descricao"] = self.get_descricao()
        return CATEGORIA

    @staticmethod
    def from_json(CATEGORIA):
        return Categoria(CATEGORIA["nome"], CATEGORIA["id"], CATEGORIA["descricao"])