from produto import Produto  # Importando a classe Produto

class Loja:
    def __init__(self):
        self.produtos = []
    
    def criarProduto(self,produto):
        self.produtos.append(produto)
        

    def visualizarProdutos(self):
        
        lista_produtos = [
            f"Nome: {produto.nomeProduto}, Preço: R${produto.precoProduto}, Estoque: {produto.quantidadeEmEstoque}"
            for produto in self.produtos
        ]
    
        return "\n".join(lista_produtos)

        
    
    # def realizarPagamento(self,produto):
    #         if(produto in self.produtos):
    #             print(f"Nome: {produto.nomeProduto}, Preço: {produto.precoProduto}, Estoque: {produto.quantidadeEmEstoque}")
            
