from loja import *
from produto import *
from carrinho import *

gerenciaDaLoja = Loja()
carrinho =Carrinho()


produto1 = Produto("Tênis", 500, 10 )
produto2 = Produto("Blusa",110,20)
produto3 = Produto("Casaco", 250 , 800)

# produto1.vizualizarInfos()

gerenciaDaLoja.criarProduto(produto1)
gerenciaDaLoja.criarProduto(produto2)
gerenciaDaLoja.criarProduto(produto3)

vitrineDeProdutos = gerenciaDaLoja.visualizarProdutos()


while True:
    print("\n=== Loja Bonitão ===")
    print("********************************************")
    print(f"Essa é nossa vitrine:\n{vitrineDeProdutos}")
    print("********************************************")
    print("O que deseja fazer ?\n")
    print("1. Adicionar produto ao carrinho")
    print("2. Visualizar carrinho")
    print("3. Pagar")
    print("4. Sair")

    opcao = int(input("Escolha uma opção: "))
    if opcao>=1 and opcao<3:
        match opcao:
            case 1:
                escolha = int(input("\nDigite o número do produto que deseja adicionar ao carrinho: ")) - 1
            
                if 0 <= escolha < len(gerenciaDaLoja.produtos):
                    produto_escolhido = gerenciaDaLoja.produtos[escolha]
                    carrinho.adicionarProduto(produto_escolhido)
                    print(f"{produto_escolhido.nomeProduto} foi adicionado ao carrinho!")
                else:
                    print("Número inválido.")
            case 2:
                print("\n=== Seu Carrinho ===")
                print(carrinho.visualizarCarrinho())
            case 3:
                print("\n=== Pagamento ===")
                print(carrinho.pagar())
            case 4:
                print("Obrigado por vir aqui")
                exit
    
        
    
    