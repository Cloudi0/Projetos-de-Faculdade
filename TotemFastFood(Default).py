import tkinter as tk
from tkinter import messagebox
import random
import sys
import os

# ================== DADOS ==================
cardapio = [
    ("🍔 Burgers", [
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

pedidos = []
total = 0
cliente_nome = ""

# ================== SALVAR ==================
def salvar_nota(resumo):
    pasta = "Banco_de_Dados"
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    caminho = os.path.join(pasta, "Notas_Fiscais.txt")

    with open(caminho, "a", encoding="utf-8") as f:
        f.write(resumo + "\n\n")

# ================== FUNÇÕES ==================
def adicionar_item(nome, preco):
    global total
    pedidos.append((nome, preco))
    total += preco
    atualizar_lista()

def remover_item(event=None):
    global total

    selecionado = lista.curselection()

    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um item para remover.")
        return

    index = selecionado[0]
    nome, preco = pedidos.pop(index)
    total -= preco
    atualizar_lista()

def limpar_pedido():
    global total
    pedidos.clear()
    total = 0
    atualizar_lista()

def atualizar_lista():
    lista.delete(0, tk.END)
    for nome, preco in pedidos:
        lista.insert(tk.END, f"{nome} — R$ {preco},00")
    label_total.config(text=f"TOTAL: R$ {total},00")

def finalizar_pedido():
    if not pedidos:
        messagebox.showwarning("Aviso", "Você ainda não escolheu nenhum item.")
        return
    janela_pagamento()

# ================== PAGAMENTO ==================
def janela_pagamento():
    janela2 = tk.Toplevel()
    janela2.title("Pagamento")
    janela2.geometry("400x350")
    janela2.configure(bg="#b71c1c")

    tk.Label(janela2, text="Escolha como deseja pagar",
             font=("Arial", 16, "bold"),
             bg="#b71c1c", fg="white").pack(pady=10)

    def pagar(forma, parcelas=1):
        numero = random.randint(1000, 9999)

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
            resumo += f"Parcelado em {parcelas}x\n"

        resumo += "=" * 40 + "\n"

        salvar_nota(resumo)
        messagebox.showinfo("Nota Fiscal", resumo)
        sys.exit()

    tk.Button(janela2, text="Cartão de Crédito",
              font=("Arial", 12, "bold"),
              width=25, bg="#2e7d32", fg="white",
              command=lambda: pagar("Crédito")).pack(pady=5)

    tk.Button(janela2, text="Cartão de Débito",
              font=("Arial", 12, "bold"),
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

    if nome == "":
        messagebox.showerror("Erro", "Por favor, digite seu nome.")
        return

    cliente_nome = nome
    tela_inicio.destroy()
    abrir_sistema()

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

    janela = tk.Tk()
    janela.title("FastFood")
    janela.state("zoomed")
    janela.configure(bg="#b71c1c")

    tk.Label(janela, text=f"Olá, {cliente_nome}!",
             font=("Arial", 16, "bold"),
             bg="#b71c1c", fg="white").pack(pady=5)

    tk.Label(janela, text="👉 Passo 1: Clique nos itens do cardápio para adicionar",
             font=("Arial", 12),
             bg="#b71c1c", fg="white").pack()

    frame = tk.Frame(janela, bg="#b71c1c")
    frame.pack(fill="both", expand=True)

    # CARDÁPIO
    frame_cardapio = tk.Frame(frame, bg="#ff9800", bd=3, relief="solid")
    frame_cardapio.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    tk.Label(frame_cardapio, text="CARDÁPIO",
             font=("Arial", 16, "bold"),
             bg="#ff9800").pack()

    for categoria, itens in cardapio:
        tk.Label(frame_cardapio, text=f"\n{categoria}",
                 font=("Arial", 13, "bold"),
                 bg="#ff9800").pack(anchor="w")

        for nome, preco in itens:
            tk.Button(frame_cardapio,
                      text=f"{nome} — R$ {preco},00",
                      font=("Arial", 12),
                      width=25,
                      command=lambda n=nome, p=preco: adicionar_item(n, p)
                      ).pack(anchor="w", pady=2)

    # PEDIDOS
    frame_pedidos = tk.Frame(frame, bg="white", bd=3, relief="solid")
    frame_pedidos.pack(side="right", fill="both", expand=True, padx=10)

    tk.Label(frame_pedidos, text="SEU PEDIDO",
             font=("Arial", 15, "bold"),
             bg="white").pack()

    lista = tk.Listbox(frame_pedidos, font=("Arial", 13))
    lista.pack(fill="both", expand=True)

    # 🔥 NOVO: remover com duplo clique
    lista.bind("<Double-Button-1>", remover_item)

    tk.Button(frame_pedidos, text="Remover item selecionado",
              bg="#c62828", fg="white",
              font=("Arial", 12, "bold"),
              command=remover_item).pack(pady=5)

    # 🔥 NOVO: limpar pedido
    tk.Button(frame_pedidos, text="Limpar Pedido",
              bg="#616161", fg="white",
              font=("Arial", 12, "bold"),
              command=limpar_pedido).pack(pady=5)

    label_total = tk.Label(frame_pedidos,
                           text="TOTAL: R$ 0,00",
                           font=("Arial", 14, "bold"),
                           bg="white")
    label_total.pack(pady=5)

    tk.Label(janela, text="👉 Passo 2: Revise seu pedido | Passo 3: Clique em finalizar",
             font=("Arial", 12),
             bg="#b71c1c", fg="white").pack(pady=5)

    tk.Button(janela, text="Finalizar Pedido",
              bg="#2e7d32", fg="white",
              font=("Arial", 14, "bold"),
              width=25, height=2,
              command=finalizar_pedido).pack(pady=10)

    janela.mainloop()

tela_inicio.mainloop()
