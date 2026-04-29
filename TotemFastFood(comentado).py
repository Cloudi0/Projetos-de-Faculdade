import tkinter as tk  # import → importa biblioteca tkinter (interface gráfica)
from tkinter import messagebox  # import específico → janelas de aviso (popup)
import random  # gera números aleatórios (random.randint)
import sys  # controla o sistema (sys.exit encerra programa)
import os  # manipula arquivos e pastas

# ================== DADOS ==================
cardapio = [  # lista → estrutura que armazena vários dados
    ("🍔 Burgers", [  # tupla → (categoria, lista de itens)
        ("X-Burger", 15),
        ("X-Salada", 18),
        ("X-Bacon", 20),
        ("X-Egg", 19),
        ("X-Tudo", 25),
        ("X-Frango", 17),
        ("Veggie Burger", 22),
    ]),
    ("🍟 Acompanhamentos", [
        ("Fritas P", 8),
        ("Fritas M", 10),
        ("Fritas G", 12),
        ("Nuggets x7", 11),
        ("Onion Rings x10", 13),
    ]),
    ("🍨 Sobremesas", [
        ("Sorvete", 10),
        ("Milkshake", 14),
        ("Sundae", 13),
    ])
]

pedidos = []  # lista → armazena os pedidos do cliente
total = 0  # variável numérica → soma total do pedido
cliente_nome = ""  # string → nome do cliente

# ================== SALVAR ==================
def salvar_nota(resumo):
    pasta = "Banco_de_Dados"

    if not os.path.exists(pasta):
        # os.path.exists() → verifica se pasta existe
        os.makedirs(pasta)
        # os.makedirs() → cria pasta

    caminho = os.path.join(pasta, "Notas_Fiscais.txt")
    # os.path.join() → monta caminho do arquivo

    with open(caminho, "a", encoding="utf-8") as f:
        # open() → abre arquivo
        # "a" → modo append (não apaga conteúdo antigo)
        # with → fecha automaticamente

        f.write(resumo + "\n\n")
        # write() → escreve no arquivo

# ================== FUNÇÕES ==================
def adicionar_item(nome, preco):
    global total  # global → permite alterar variável fora da função

    pedidos.append((nome, preco))
    # append() → adiciona item na lista

    total += preco
    # "+=" → soma valor ao total

    atualizar_lista()
    # chama função

def remover_item(event=None):
    global total

    selecionado = lista.curselection()
    # curselection() → retorna índice selecionado

    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um item para remover.")
        # showwarning() → mostra aviso
        return

    index = selecionado[0]
    # pega posição do item

    nome, preco = pedidos.pop(index)
    # pop() → remove item da lista

    total -= preco
    # "-=" → subtrai valor

    atualizar_lista()

def limpar_pedido():
    global total

    pedidos.clear()
    # clear() → limpa lista

    total = 0

    atualizar_lista()

def atualizar_lista():
    lista.delete(0, tk.END)
    # delete() → limpa lista visual

    for nome, preco in pedidos:
        # for → percorre lista
        lista.insert(tk.END, f"{nome} — R$ {preco},00")
        # insert() → adiciona item na interface

    label_total.config(text=f"TOTAL: R$ {total},00")
    # config() → altera texto

def finalizar_pedido():
    if not pedidos:
        messagebox.showwarning("Aviso", "Você ainda não escolheu nenhum item.")
        return

    janela_pagamento()

# ================== PAGAMENTO ==================
def janela_pagamento():
    # === INTERFACE ===
    janela2 = tk.Toplevel()
    janela2.title("Pagamento")
    janela2.geometry("400x350")
    janela2.configure(bg="#b71c1c")

    # === INTERFACE ===
    tk.Label(janela2, text="Escolha como deseja pagar",
             font=("Arial", 16, "bold"),
             bg="#b71c1c", fg="white").pack(pady=10)

    def pagar(forma, parcelas=1):
        numero = random.randint(1000, 9999)
        # randint() → gera número aleatório

        resumo = "\n" + "=" * 40 + "\n"
        resumo += "NOTA FISCAL\n"
        resumo += "=" * 40 + "\n"
        resumo += f"Cliente: {cliente_nome}\n"
        resumo += f"Pedido: {numero}\n"
        resumo += "-" * 40 + "\n"

        for nome, preco in pedidos:
            resumo += f"{nome} — R$ {preco},00\n"

        resumo += "-" * 40 + "\n"
        resumo += f"TOTAL: R$ {total},00\n"
        resumo += f"Pagamento: {forma}\n"

        if parcelas > 1:
            valor_parcela = total / parcelas
            # "/" → divisão
            resumo += f"Parcelado em {parcelas}x de R$ {valor_parcela:.2f}\n"

        resumo += "=" * 40 + "\n"

        salvar_nota(resumo)
        # chama função salvar

        messagebox.showinfo("Nota Fiscal", resumo)
        # showinfo() → mostra mensagem

        sys.exit()
        # exit() → encerra programa

    def escolher_parcelas():
        # === INTERFACE ===
        janela_parcelas = tk.Toplevel(janela2)
        janela_parcelas.title("Parcelamento")
        janela_parcelas.geometry("300x250")
        janela_parcelas.configure(bg="#b71c1c")

        # === INTERFACE ===
        tk.Label(janela_parcelas, text="Escolha as parcelas",
                 font=("Arial", 14, "bold"),
                 bg="#b71c1c", fg="white").pack(pady=10)

        for i in [1, 2, 3]:
            # for → percorre lista
            tk.Button(janela_parcelas,
                      text=f"{i}x",
                      font=("Arial", 12, "bold"),
                      width=15,
                      bg="#2e7d32", fg="white",
                      command=lambda p=i: pagar("Crédito", p)
                      # lambda → função rápida
                      ).pack(pady=5)

    # === INTERFACE ===
    tk.Button(janela2, text="Cartão de Crédito",
              font=("Arial", 12, "bold"),
              width=25, bg="#2e7d32", fg="white",
              command=escolher_parcelas).pack(pady=5)

    tk.Button(janela2, text="Cartão de Débito",
              font=("Arial", 12, " bold"),
              width=25, bg="#2e7d32", fg="white",
              command=lambda: pagar("Débito")).pack(pady=5)

    tk.Button(janela2, text="Pix",
              font=("Arial", 12, "bold"),
              width=25, bg="#2e7d32", fg="white",
              command=lambda: pagar("Pix")).pack(pady=5)

    tk.Button(janela2, text="Dinheiro",
              font=("Arial", 12, "bold"),
              width=25, bg="#2e7d32", fg="white",
              command=lambda: pagar("Dinheiro")).pack(pady=5)

# ================== TELA INICIAL ==================
def iniciar_sistema():
    global cliente_nome

    nome = entry_nome_inicio.get().strip()
    # get() → pega texto
    # strip() → remove espaços

    if nome == "":
        messagebox.showerror("Erro", "Por favor, digite seu nome.")
        return

    cliente_nome = nome

    tela_inicio.destroy()
    # destroy() → fecha janela

    abrir_sistema()

# === INTERFACE ===
tela_inicio = tk.Tk()
tela_inicio.title("Bem-vindo")
tela_inicio.geometry("400x200")
tela_inicio.configure(bg="#b71c1c")

tk.Label(tela_inicio, text="Digite seu nome para começar",
         font=("Arial", 16, "bold"),
         bg="#b71c1c", fg="white").pack(pady=20)

entry_nome_inicio = tk.Entry(tela_inicio, font=("Arial", 12))
entry_nome_inicio.pack(pady=10)

tk.Button(tela_inicio, text="Entrar",
          bg="#2e7d32", fg="white",
          font=("Arial", 12, "bold"),
          width=15,
          command=iniciar_sistema).pack(pady=10)

# ================== SISTEMA PRINCIPAL ==================
def abrir_sistema():
    global lista, label_total

    # === INTERFACE ===
    janela = tk.Tk()
    janela.title("FastFood")
    janela.geometry("1000x700")
    janela.minsize(800, 600)
    janela.configure(bg="#b71c1c")

    # === INTERFACE ===
    janela.rowconfigure(2, weight=1)
    janela.columnconfigure(0, weight=1)

    # === INTERFACE ===
    tk.Label(janela, text=f"Olá, {cliente_nome}!",
             font=("Arial", 16, "bold"),
             bg="#b71c1c", fg="white").grid(row=0, column=0, pady=5)

    # === INTERFACE ===
    tk.Label(janela, text="👉 Passo 1: Clique nos itens do cardápio",
             font=("Arial", 12),
             bg="#b71c1c", fg="white").grid(row=1, column=0)

    # === INTERFACE ===
    frame = tk.Frame(janela, bg="#b71c1c")
    frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(0, weight=1)

    # === INTERFACE ===
    frame_cardapio = tk.Frame(frame, bg="#ff9800", bd=3, relief="solid")
    frame_cardapio.grid(row=0, column=0, sticky="nsew", padx=5)

    # === INTERFACE ===
    canvas = tk.Canvas(frame_cardapio, bg="#ff9800")
    scrollbar = tk.Scrollbar(frame_cardapio, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg="#ff9800")

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    # bind() → associa evento à função

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # === INTERFACE ===
    tk.Label(scroll_frame, text="CARDÁPIO",
             font=("Arial", 16, "bold"),
             bg="#ff9800").pack()

    for categoria, itens in cardapio:
        # for → percorre categorias do cardápio
        tk.Label(scroll_frame, text=f"\n{categoria}",
                 font=("Arial", 13, "bold"),
                 bg="#ff9800").pack(anchor="w")

        for nome, preco in itens:
            # for → percorre itens
            tk.Button(scroll_frame,
                      text=f"{nome} — R$ {preco},00",
                      font=("Arial", 11),
                      width=25,
                      command=lambda n=nome, p=preco: adicionar_item(n, p)
                      # lambda → cria função rápida
                      ).pack(anchor="w", pady=2)

    # === INTERFACE ===
    frame_pedidos = tk.Frame(frame, bg="white", bd=3, relief="solid")
    frame_pedidos.grid(row=0, column=1, sticky="nsew", padx=5)

    frame_pedidos.rowconfigure(1, weight=1)
    frame_pedidos.columnconfigure(0, weight=1)

    # === INTERFACE ===
    tk.Label(frame_pedidos, text="SEU PEDIDO",
             font=("Arial", 15, "bold"),
             bg="white").grid(row=0, column=0)

    lista = tk.Listbox(frame_pedidos, font=("Arial", 12))
    lista.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    lista.bind("<Double-Button-1>", remover_item)
    # bind() → evento de duplo clique

    # === INTERFACE ===
    tk.Button(frame_pedidos, text="Remover item",
              bg="#c62828", fg="white",
              font=("Arial", 11, "bold"),
              command=remover_item).grid(row=2, column=0, pady=2)

    tk.Button(frame_pedidos, text="Limpar Pedido",
              bg="#616161", fg="white",
              font=("Arial", 11, "bold"),
              command=limpar_pedido).grid(row=3, column=0, pady=2)

    label_total = tk.Label(frame_pedidos,
                           text="TOTAL: R$ 0,00",
                           font=("Arial", 13, "bold"),
                           bg="white")
    label_total.grid(row=4, column=0, pady=5)

    # === INTERFACE ===
    frame_bottom = tk.Frame(janela, bg="#b71c1c")
    frame_bottom.grid(row=3, column=0, sticky="ew")

    tk.Label(frame_bottom,
             text="👉 Passo 2: Revise | Passo 3: Finalize",
             font=("Arial", 12),
             bg="#b71c1c", fg="white").pack()

    tk.Button(frame_bottom, text="Finalizar Pedido",
              bg="#2e7d32", fg="white",
              font=("Arial", 14, "bold"),
              width=25,
              height=2,
              command=finalizar_pedido).pack(pady=10)

    janela.mainloop()
    # mainloop() → mantém o programa rodando

tela_inicio.mainloop()
# inicia o programa
