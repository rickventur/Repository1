from datetime import datetime

class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

class Cliente:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

class Venda:
    def __init__(self, cliente):
        self.cliente = cliente
        self.data = datetime.now()
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        self.itens.append((produto, quantidade))

    def remover_item(self, produto):
        for item in self.itens:
            if item[0] == produto:
                self.itens.remove(item)
                break

    def calcular_total(self):
        total = 0
        for item in self.itens:
            produto, quantidade = item
            total += produto.preco * quantidade
        return total

    def imprimir_recibo(self):
        print("----- Recibo de Venda -----")
        print("Data: ", self.data.strftime("%d/%m/%Y %H:%M:%S"))
        print("Cliente: ", self.cliente.nome)
        print("Endereço: ", self.cliente.endereco)
        print("Telefone: ", self.cliente.telefone)
        print("Itens: ")
        for item in self.itens:
            produto, quantidade = item
            print(f"- {produto.nome}: {quantidade} x R${produto.preco:.2f}")
        print("Total: R$", self.calcular_total())
        print("---------------------------")

# Exemplo de utilização do programa

# Criação de produtos
p1 = Produto(1, "Camiseta", 29.90)
p2 = Produto(2, "Calça", 79.90)
p3 = Produto(3, "Tênis", 99.90)

# Criação de cliente
cliente = Cliente("João Silva", "Rua A, 123", "(11) 99999-9999")

# Criação de venda
venda = Venda(cliente)

# Adição de itens na venda
venda.adicionar_item(p1, 2)
venda.adicionar_item(p2, 1)
venda.adicionar_item(p3, 1)

# Remoção de um item da venda
venda.remover_item(p2)

# Impressão do recibo da venda
venda.imprimir_recibo()
