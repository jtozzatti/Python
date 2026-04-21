#importamos a biblioteca json para trabalhar com arquivos JSON, que é onde vamos salvar nossos dados.
import json
 
#definimos o nome de uma variável ARQUIVO para armazenar o nome do arquivo JSON onde os dados serão salvos.
ARQUIVO = "dados.json"

#essa funçao vai salvar os dados da lista no arquivo JSON.
def salvar_dados(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)
 
#essa função vai carregar os dados do arquivo dados.json quando o programa inicia
def carregar_dados():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("\nAtenção: arquivo de dados corrompido. Iniciando com lista vazia.\n")
        return []
 
#essa função vai adicionar uma nova informação à lista e salvar automaticamente.
def adicionar_informacao(lista):
    print("\n--- Cadastrar Informação ---")
 
    titulo = input("Digite o título: ").strip()
    while titulo == "":
        titulo = input("O título não pode estar vazio. Digite novamente: ").strip()
 
    tipo = input("Digite o tipo (educativo, cultural ou lazer): ").strip().lower()
    while tipo not in ["educativo", "cultural", "lazer"]:
        tipo = input("Tipo inválido. Digite (educativo, cultural ou lazer): ").strip().lower()
 
    descricao = input("Digite a descrição: ").strip()
    while descricao == "":
        descricao = input("A descrição não pode estar vazia. Digite novamente: ").strip()
 
    lista.append({
        "titulo": titulo,
        "tipo": tipo,
        "descricao": descricao
    })
 
    salvar_dados(lista)
    print("\nInformação cadastrada com sucesso!\n")
 
 
#essa funçao vai listar todas as informações cadastradas, mostrando o título, tipo e descrição de cada uma.
def listar_informacoes(lista):
    if not lista:
        print("\nNenhuma informação cadastrada.\n")
    else:
        print("\n--- Informações Cadastradas ---")
        for i, info in enumerate(lista, start=1):
            print(f"{i}. Título: {info['titulo']}")
            print(f"   Tipo:    {info['tipo']}")
            print(f"   Descrição: {info['descricao']}\n")
 
#essa função vai permitir ao usuário pesquisar as informações por tipo, mostrando apenas as do tipo escolhido.
def pesquisar_por_tipo(lista):
    tipo = input("Digite o tipo para pesquisar (educativo, cultural ou lazer): ").strip().lower()
    if tipo not in ["educativo", "cultural", "lazer"]:
        print("\nTipo inválido.\n")
        return
 
    encontrados = [info for info in lista if info["tipo"] == tipo]
    if encontrados:
        print(f"\n--- Informações do tipo '{tipo}' ---")
        for i, info in enumerate(encontrados, start=1):
            print(f"{i}. Título: {info['titulo']}")
            print(f"   Descrição: {info['descricao']}\n")
    else:
        print(f"\nNenhuma informação do tipo '{tipo}' encontrada.\n")
 
#essa função vai permitir ao usuário editar um registro já cadastrado.
def editar_informacao(lista):
    if not lista:
        print("\nNenhuma informação cadastrada para editar.\n")
        return
 
    listar_informacoes(lista)
 
    try:
        indice = int(input("Digite o número do registro que deseja editar: ")) - 1
        if indice < 0 or indice >= len(lista):
            print("\nNúmero inválido.\n")
            return
    except ValueError:
        print("\nEntrada inválida. Digite um número.\n")
        return
 
    registro = lista[indice]
    print(f"\n--- Editando: {registro['titulo']} ---")
    print("(Pressione Enter para manter o valor atual)\n")
 
    novo_titulo = input(f"Título atual [{registro['titulo']}]: ").strip()
    if novo_titulo != "":
        registro["titulo"] = novo_titulo
 
    while True:
        novo_tipo = input(f"Tipo atual [{registro['tipo']}] (educativo, cultural ou lazer): ").strip().lower()
        if novo_tipo == "":
            break  # mantém o valor atual
        elif novo_tipo in ["educativo", "cultural", "lazer"]:
            registro["tipo"] = novo_tipo
            break
        else:
            print("Tipo inválido. Digite (educativo, cultural ou lazer) ou pressione Enter para manter.")
 
    nova_descricao = input(f"Descrição atual [{registro['descricao']}]: ").strip()
    if nova_descricao != "":
        registro["descricao"] = nova_descricao
 
    salvar_dados(lista)
    print("\nInformação atualizada com sucesso!\n")
 
 

#nessa funçao o usuário pode excluir um registro da lista, mas antes de excluir, o programa pede ao usario uma confirmação para evitar exclusões acidentais.
def excluir_informacao(lista):
    if not lista:
        print("\nNenhuma informação cadastrada para excluir.\n")
        return
 
    listar_informacoes(lista)
 
    try:
        indice = int(input("Digite o número do registro que deseja excluir: ")) - 1
        if indice < 0 or indice >= len(lista):
            print("\nNúmero inválido.\n")
            return
    except ValueError:
        print("\nEntrada inválida. Digite um número.\n")
        return
 
    registro = lista[indice]
    confirmacao = input(f"Tem certeza que deseja excluir '{registro['titulo']}' ? (s/n): ").strip().lower()
 
    if confirmacao == "s":
        lista.pop(indice)
        salvar_dados(lista)
        print("\nInformação excluída com sucesso!\n")
    else:
        print("\nExclusão cancelada.\n")