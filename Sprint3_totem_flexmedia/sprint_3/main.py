# aqui puxamos as funções do arquivo funcoes.py para usar no main.py.
from funcoes import (
    carregar_dados,
    adicionar_informacao,
    listar_informacoes,
    pesquisar_por_tipo,
    editar_informacao,
    excluir_informacao
)

# Carrega os dados do arquivo JSON para a lista de informações.
informacoes = carregar_dados()

# codigo para o menu principal do nosso programa.
while True:
    print("=== Totem FlexMedia ===")
    print("1 - Cadastrar informação")
    print("2 - Listar informações cadastradas")
    print("3 - Pesquisar informações por tipo")
    print("4 - Editar informação")
    print("5 - Excluir informação")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_informacao(informacoes)
    elif opcao == "2":
        listar_informacoes(informacoes)
    elif opcao == "3":
        pesquisar_por_tipo(informacoes)
    elif opcao == "4":
        editar_informacao(informacoes)
    elif opcao == "5":
        excluir_informacao(informacoes)
    elif opcao == "0":
        print("\nSaindo do programa. Até mais!")
        break
    else:
        print("\nOpção inválida. Tente novamente.\n")