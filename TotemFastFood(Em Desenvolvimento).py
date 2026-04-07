import sys

print("=" * 40)
print("Bem-Vindo ao FastFood".upper())
print("=" * 40)

# criando um confirmacao
def confirmacao():
    while True:
        # criando variavel(continuar) com input para permitir a digitação
        continuar = input("Deseja continuar? [S/N]: ").lower()

        if continuar == "s":
            return True
        elif continuar == "n":
            print("Ate Mais :)")
            sys.exit()
        else:
            print("Resposta inválida! Digite apenas S ou N")

# criando variavel(resultado)
resultado = confirmacao()

while True:
    # criando variavel(usuario)
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

# criando variavel(cardapio)
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
                opcao = input("\nDeseja [1] Continuar pedindo ou [2] Pagar? ")

                if opcao == "1":
                    break
                elif opcao == "2":
                    print("\n" + "=" * 40)
                    print("RESUMO DO PEDIDO")
                    print("=" * 40)

                    for nome_pedido, preco_pedido in pedidos:
                        print(f"{nome_pedido} — R$ {preco_pedido},00")

                    print("-" * 40)
                    print(f"TOTAL: R$ {total},00")
                    print("Obrigado pela compra! 🍔")
                    sys.exit()
                else:
                    print("Opção inválida!")

            break

    if not encontrado:
        print("Código inválido!")