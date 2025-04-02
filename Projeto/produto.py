class Produto:
    def __init__(self,nomeProduto,precoProduto,quantidadeEmEstoque):
        self.nomeProduto = nomeProduto
        self.precoProduto = precoProduto
        self.quantidadeEmEstoque = quantidadeEmEstoque
    
    def vizualizarInfos(self):
        print(f"Nome: {self.nomeProduto}, Preço: {self.precoProduto}, Estoque: {self.quantidadeEmEstoque}")