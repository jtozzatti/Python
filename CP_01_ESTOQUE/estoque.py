class Produto:
    
    def __init__(self, nome:str, codigo:int, categoria:str, quantidade:int, preco:float, descricao:str, fornecedor:str):
        try:
            if not isinstance(nome, str) or nome == "":
                raise ValueError("Nome inválido")

            if not isinstance(codigo, int):
                raise ValueError("Código deve ser inteiro")

            if quantidade < 0:
                raise ValueError("Quantidade não pode ser negativa")

            if preco < 0:
                raise ValueError("Preço não pode ser negativo")

            self.nome = nome
            self.codigo = codigo
            self.categoria = categoria
            self.quantidade = quantidade
            self.preco = preco
            self.descricao = descricao
            self.fornecedor = fornecedor

        except Exception as e:
            print(f"Erro ao criar produto: {e}")
            raise

    def info(self):
        try:
            print(f'nome:{self.nome}\ncodigo: {self.codigo}\ncategoria: {self.categoria}\nquantidade: {self.quantidade}\npreço: {self.preco}\ndescricao: {self.descricao}\nfornecedor: {self.fornecedor}')
        except Exception as e:
            print(f"Erro ao exibir produto: {e}")



class Estoque:
    
    def __init__(self):
        self.produtos = {}

    def exibir_estoque(self):
        try:
            if not self.produtos:
                print("O estoque está vazio.")
                return
            
            print("\n===== ESTOQUE =====")
            for produto in self.produtos.values():
                    print(f"Nome: {produto.nome}")
                    print(f"Código: {produto.codigo}")
                    print(f"Categoria: {produto.categoria}")
                    print(f"Quantidade: {produto.quantidade}")
                    print(f"Preço: R$ {produto.preco}")
                    print(f"Fornecedor: {produto.fornecedor}")
                    print("---------------------------")
        except Exception as e:
            print(f"Erro ao exibir estoque: {e}")

    def cadastrar_produto(self, produto):
        try:
            if produto.codigo in self.produtos:
                raise ValueError("Já existe um produto com esse código")

            self.produtos[produto.codigo] = produto
            print("Produto Cadastrado com Sucesso")
        except Exception as e:
            print(f"Erro ao cadastrar produto: {e}")

    def adicionar_estoque(self, codigo, quantidade):
        try:
            if quantidade <= 0:
                raise ValueError("Quantidade deve ser positiva")

            if codigo not in self.produtos:
                raise KeyError("Produto não encontrado")

            self.produtos[codigo].quantidade += quantidade
            print("Estoque atualizado")
        except Exception as e:
            print(f"Erro ao adicionar estoque: {e}")

    def remover_estoque(self , codigo, quantidade):
        try:
            if quantidade <= 0:
                raise ValueError("Quantidade deve ser positiva")

            if codigo not in self.produtos:
                raise KeyError("Produto não encontrado")

            produto = self.produtos[codigo]

            if produto.quantidade < quantidade:
                raise ValueError("Estoque insuficiente")

            produto.quantidade -= quantidade
            print("Produto removido do estoque.")
        except Exception as e:
            print(f"Erro ao remover estoque: {e}")


    def atualizar_estoque(self , codigo, nova_quantidade):
        try:
            if nova_quantidade < 0:
                raise ValueError("Quantidade não pode ser negativa")

            if codigo not in self.produtos:
                raise KeyError("Produto não encontrado")

            self.produtos[codigo].quantidade = nova_quantidade
            print("Quantidade atualizada")
        except Exception as e:
            print(f"Erro ao atualizar estoque: {e}")

    def alerta_estoque_baixo(self, limite):
        try:
            print("Produtos com estoque baixo:")
            for produto in self.produtos.values():
                if produto.quantidade <= limite:
                    print(f"{produto.nome} - Quantidade: {produto.quantidade}")
        except Exception as e:
            print(f"Erro no alerta de estoque: {e}")

