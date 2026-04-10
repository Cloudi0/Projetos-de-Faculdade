import sys
import random

print("=" * 40)
print("Bem-Vindo ao FastFood".upper())
print("=" * 40)

def confirmacao():
    while True:
        continuar = input("Deseja continuar? [S/N]: ").lower()

        if continuar == "s":
            return True
        elif continuar == "n":
            print("Ate Mais :)")
            sys.exit()
        else:
            print("Resposta inválida! Digite apenas S ou N")

resultado = confirmacao()

while True:
    usuario = input("Digite seu nome: ")
    if len(usuario) <= 20:
        print("Nome válido")
        break
    else:
        print("Nome muito grande (máx 10 caracteres)")

print("\n")
print("=" * 40)
print(f"olá {usuario}, faça seu pedido".upper())
print("=" * 40)
print("\n")

lanches = [
    (1, "X-Burger", 15),
    (2, "X-Salada", 18),
    (3, "X-Bacon", 20),
    (4, "X-Egg", 19),
    (5, "X-Tudo", 25),
    (6, "X-Frango", 17),
    (7, "Veggie Burger", 22)
]

print("-" * 40)
print("LANCHES")
print("-" * 40)
for codigo, nome, preco in lanches:
    print(f"{codigo} - {nome} — R$ {preco},00")

acompanhamentos = [
    (8, "Fritas P", 8),
    (9, "Fritas M", 10),
    (10, "Fritas G", 12),
    (11, "Nuggets x7", 11),
    (12, "Onion Rings x10", 13)
]

print("-" * 40)
print("ACOMPANHAMENTOS")
print("-" * 40)
for codigo, nome, preco in acompanhamentos:
    print(f"{codigo} - {nome} — R$ {preco},00")

sobremesas = [
    (13, "Sorvete", 10),
    (14, "Milkshake", 14),
    (15, "Sundae", 13),
]

print("-" * 40)
print("SOBREMESAS")
print("-" * 40)
for codigo, nome, preco in sobremesas:
    print(f"{codigo} - {nome} — R$ {preco},00")

cardapio = lanches + acompanhamentos + sobremesas

total = 0
pedidos = []

while True:
    escolha = input("\nQual a sua escolha?(ou digite 0 para sair)...: ")

    if not escolha.isdigit():
        print("Digite apenas números!")
        continue

    escolha = int(escolha)

    if escolha == 0:
        break

    encontrado = False

    for codigo, nome, preco in cardapio:
        if escolha == codigo:
            pedidos.append((nome, preco))
            total += preco

            print(f"\nVocê escolheu: {nome} — R$ {preco},00")
            print(f"Total atual: R$ {total},00")

            encontrado = True

            while True:
                opcao = input("\nDigite [1] Continuar pedindo, [2] Pagar ou [3] Remover item?(ou Digite 0 para sair) ")

                if opcao == "1":
                    break

                elif opcao == "0":
                    print("Tenha um Bom Dia :)")
                    sys.exit()

                elif opcao == "2":
                    print("\n" + "=" * 40)
                    print("RESUMO DO PEDIDO")
                    print("=" * 40)

                    for nome_pedido, preco_pedido in pedidos:
                        print(f"{nome_pedido} — R$ {preco_pedido},00")

                    print("-" * 40)
                    print(f"TOTAL: R$ {total},00")

                    # ESCOLHA DE PAGAMENTO
                    while True:
                        print("\nFormas de pagamento:")
                        print("[1] Pix")
                        print("[2] Cartão de débito")
                        print("[3] Dinheiro")
                        print("[4] Voltar para o cardápio")

                        pagamento = input("Escolha a forma de pagamento: ")

                        if pagamento == "1":
                            forma = "Pix"
                            print("\nPagamento Aprovado".upper())
                            break
                        elif pagamento == "2":
                            forma = "Cartão de débito"
                            print("\nPagamento Aprovado".upper())
                            break
                        elif pagamento == "3":
                            forma = "Dinheiro"
                            print("\nEfetue o Pagamento no Balcao ao Lado".upper())
                            break
                        elif pagamento == "4":
                            break  # volta pro menu anterior
                        else:
                            print("Opção inválida!")

                    # SE ESCOLHER VOLTAR, RETORNA AO CARDÁPIO
                    if pagamento == "4":
                        continue

                    numero_chamada = random.randint(10, 9999)

                    # NOTA FISCAL
                    print("\n" + "=" * 40)
                    print("NOTA FISCAL")
                    print("=" * 40)
                    print(f"Cliente: {usuario}")
                    print(f"Número do pedido: {numero_chamada}")
                    print("-" * 40)

                    for nome_pedido, preco_pedido in pedidos:
                        print(f"{nome_pedido} — R$ {preco_pedido},00")

                    print("-" * 40)
                    print(f"TOTAL: R$ {total},00")
                    print(f"Pagamento: {forma}")
                    print("=" * 40)
                    print("Obrigado pela compra! 🍔")

                    sys.exit()

                elif opcao == "3":
                    if len(pedidos) == 0:
                        print("Nenhum item para remover!")
                        continue

                    print("\nSeus pedidos:")
                    for i, (nome_pedido, preco_pedido) in enumerate(pedidos):
                        print(f"{i} - {nome_pedido} — R$ {preco_pedido},00")

                    remover = input("Digite o número do item que deseja remover: ")

                    if not remover.isdigit():
                        print("Digite apenas números!")
                        continue

                    remover = int(remover)

                    if 0 <= remover < len(pedidos):
                        nome_removido, preco_removido = pedidos.pop(remover)
                        total -= preco_removido
                        print(f"{nome_removido} removido com sucesso!")
                        print(f"Total atual: R$ {total},00")
                    else:
                        print("Item inválido!")

                else:
                    print("Opção inválida!")

            break

    if not encontrado:
        print("Código inválido!")
