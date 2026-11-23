from datetime import datetime
from models.vendaItem import VendaItem

class Venda:
    def __init__(self, id, data, carrinho, total, id_cliente):
        self.set_id(id)
        self.set_data(data)
        self.__carrinho = carrinho
        self.__total = total
        self.set_id_cliente(id_cliente)

    def __str__(self):
        return f"ID: {self.__id} - Data: {self.__data} - Carrinho: {self.__carrinho} - Total: {self.__total} - ID Cliente: {self.__id_cliente}"

    def set_id(self, id):
        if id < 0:
            raise ValueError("ID não pode ser negativo")
        self.__id = id

    def set_data(self, data):
        if data is None:
            data = datetime.now()
        elif isinstance(data, str):
            data = datetime.strptime(data, "%d/%m/%Y %H:%M:%S")
        if data > datetime.now():
            raise ValueError("Data não pode ser futura")
        self.__data = data.strftime("%d/%m/%Y %H:%M:%S")

    def set_carrinho(self, carrinho):
        if carrinho == True: 
            carrinho =  VendaItem.get_preco() * VendaItem.get_quantidade()  
            self.__carrinho = carrinho

    def set_total(self, total, carrinho):
        if carrinho == True:
            total = carrinho
            self.__total = total
        if total < 0.0:
            raise ValueError("Total não pode ser negativo")
        if carrinho == False: return f"Total não calculado, pois o carrinho está desligado"
            

    def set_id_cliente(self, id_cliente):
        if id_cliente < 0:
            raise ValueError("ID do cliente não pode ser negativo")
        self.__id_cliente = id_cliente

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_carrinho(self): return self.__carrinho
    def get_total(self): return self.__total
    def get_id_cliente(self): return self.__id_cliente

    def to_json(self):
        Venda_pr = {}
        Venda_pr["id"] = self.__id
        Venda_pr["data"] = self.__data 
        Venda_pr["carrinho"] = self.__carrinho
        Venda_pr["total"] = self.__total
        Venda_pr["id_cliente"] = self.__id_cliente
        return Venda_pr

    @staticmethod
    def from_json(Venda_pr):
        return Venda(
            Venda_pr["id"],
            Venda_pr["data"],
            Venda_pr["carrinho"],
            Venda_pr["total"],
            Venda_pr["id_cliente"],
        )