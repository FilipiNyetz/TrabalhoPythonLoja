from produto import Produto  # Importando a classe Produto
from carrinho import Carrinho

class Loja:
    def __init__(self):
        self.produtos = []
    
    def criarProduto(self,produto):
        self.produtos.append(produto)
        

    def visualizarProdutos(self):
        
        lista_produtos = [
            f"ID:{index+1} Nome: {produto.nomeProduto}, Preço: R${produto.precoProduto}, Estoque: {produto.quantidadeEmEstoque}"
            for index, produto in enumerate(self.produtos)
            
        ]
    
        return "\n".join(lista_produtos)

    
    
    def realizarPagamento(self,carrinho):
        if len(carrinho.produtosArmazenados) < 1:
            print("Não há produtos no carrinho")
            
        else:
            while True:
                print("\n=== Pagamento ===")
                print(f"Valor a pagar: {carrinho.calcularValorTotal()}R$")
                print("Escolha sua forma de pagamento")
                print("1 - Pix (10% de desconto)")
                print("2 - Débito")
                print("3 - Crédito (5% de juros)")
                escolhaTipoDePagamento = int(input("Qual a forma de pagamento ?"))
                match escolhaTipoDePagamento:
                    case 1:
                        print(f"Voce ira pagar: {Carrinho.calcularValorTotal(carrinho)*0.9}")
                        confirmacao = input("Digite sim para prosseguir a compra, digite não para selecionar outras formas de pagamento: ").lower()
                        if confirmacao == 'sim':
                            print("Pagamento concluido, obrigado e volte sempre...")
                            for produto in carrinho.produtosArmazenados:
                                produto.quantidadeEmEstoque-=1
                                print(produto.quantidadeEmEstoque)
                            
                            Carrinho.esvaziarCarrinho(carrinho)
                            break
                        
                    case 2:
                        print(f"Voce ira pagar: {Carrinho.calcularValorTotal(carrinho)}")
                        confirmacao = input("Digite sim para prosseguir a compra, digite não para selecionar outras formas de pagamento: ").lower()
                        if confirmacao == 'sim':
                            print("Pagamento concluido, obrigado e volte sempre...")
                            for produto in carrinho.produtosArmazenados:
                                produto.quantidadeEmEstoque-=1
                                print(produto.quantidadeEmEstoque)
                            Carrinho.esvaziarCarrinho(carrinho)
                            break
                    case 3:
                        print(f"Voce ira pagar: {Carrinho.calcularValorTotal(carrinho)*1.1}")
                        confirmacao = input("Digite sim para prosseguir a compra, digite não para selecionar outras formas de pagamento: ").lower()
                        if confirmacao == 'sim':
                            print("Pagamento concluido, obrigado e volte sempre...")
                            for produto in carrinho.produtosArmazenados:
                                produto.quantidadeEmEstoque-=1
                                print(produto.quantidadeEmEstoque)
                            Carrinho.esvaziarCarrinho(carrinho)
                            break

                

        

        