class Carrinho:
    def __init__(self):
        self.produtosArmazenados = []
        self.valorTotal = 0
    def adicionarProduto(self,produto):
        self.produtosArmazenados.append(produto)
    
    def calcularValorTotal(self):
        
        for i in self.produtosArmazenados:
            self.valor+=i.precoProduto
    def esvaziarCarrinho(self):
        self.produtosArmazenado.clear()