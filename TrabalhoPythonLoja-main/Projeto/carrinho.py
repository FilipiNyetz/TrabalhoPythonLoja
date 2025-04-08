from produto import *

class Carrinho:
    valorCarrinho = 0
    
    def __init__(self):
        self.produtosArmazenados = []
        self.valorTotal = 0
    def adicionarProduto(self,produto):
        if produto.quantidadeEmEstoque <1:
            print("Este produto não está disponível")
        else:
            print(f"O produto: {produto} foi adicionado ao carrinho")
            self.produtosArmazenados.append(produto)

    def calcularValorTotal(self):
        self.valorTotal = 0
        for produto in self.produtosArmazenados:
            self.valorTotal+=produto.precoProduto
            
        
        return self.valorTotal
    
    def visualizarCarrinho(self):
        lista_produtos_carrinho = [
            f"|ID:{index+1} Nome: {produto.nomeProduto}, Preço: R${produto.precoProduto}, Estoque: {produto.quantidadeEmEstoque}|"
            for index, produto in enumerate(self.produtosArmazenados)
        ]
        valorCarrinho = self.calcularValorTotal()
        return "\n".join(lista_produtos_carrinho) + f"\nO valor total do carrinho: R${valorCarrinho:.2f}"


        
    
    
    def esvaziarCarrinho(self):
        self.produtosArmazenados.clear()
        
    