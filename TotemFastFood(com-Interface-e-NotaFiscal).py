import tkinter as tk
from tkinter import messagebox
import random
import sys
import os
from datetime import datetime

# ================== DADOS ==================
cardapio = [
    (1, "X-Burger", 15),
    (2, "X-Salada", 18),
    (3, "X-Bacon", 20),
    (4, "X-Egg", 19),
    (5, "X-Tudo", 25),
    (6, "X-Frango", 17),
    (7, "Veggie Burger", 22),
    (8, "Fritas P", 8),
    (9, "Fritas M", 10),
    (10, "Fritas G", 12),
    (11, "Nuggets x7", 11),
    (12, "Onion Rings x10", 13),
    (13, "Sorvete", 10),
    (14, "Milkshake", 14),
    (15, "Sundae", 13),
]

pedidos = []
total = 0

# ================== NOVA FUNÇÃO ==================
def salvar_nota(resumo, cliente, numero):
    pasta = "notas_fiscais"

    if not os.path.exists(pasta):
        os.makedirs(pasta)

    data = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

    nome_arquivo = f"{cliente}_{numero}_{data}.txt"
    caminho = os.path.join(pasta, nome_arquivo)

    with open(caminho, "w", encoding="utf-8") as f:
        f.write(resumo)

# ================== FUNÇÕES ==================
def adicionar_item():
    global total

    escolha = entry_codigo.get()

    if not escolha.isdigit():
        messagebox.showerror("Erro", "Digite apenas números!")
        return

    escolha = int(escolha)

    for codigo, nome, preco in cardapio:
        if escolha == codigo:
            pedidos.append((nome, preco))
            total += preco
            atualizar_lista()
            entry_codigo.delete(0, tk.END)
            return

    messagebox.showerror("Erro", "Código inválido!")


def remover_item():
    global total

    try:
        index = lista.curselection()[0]
        nome, preco = pedidos.pop(index)
        total -= preco
        atualizar_lista()
    except:
        messagebox.showerror("Erro", "Selecione um item para remover!")


def atualizar_lista():
    lista.delete(0, tk.END)

    for nome, preco in pedidos:
        lista.insert(tk.END, f"{nome} — R$ {preco},00")

    label_total.config(text=f"TOTAL: R$ {total},00")


def finalizar_pedido():
    if not pedidos:
        messagebox.showwarning("Aviso", "Nenhum pedido feito!")
        return

    janela_pagamento()


def janela_pagamento():
    janela2 = tk.Toplevel()
    janela2.title("Pagamento")
    janela2.geometry("400x300")

    tk.Label(janela2, text="Escolha a forma de pagamento", font=("Arial", 12, "bold")).pack(pady=10)

    def pagar(forma):
        numero = random.randint(10, 9999)

        resumo = "\n" + "=" * 40 + "\n"
        resumo += "NOTA FISCAL\n"
        resumo += "=" * 40 + "\n"
        resumo += f"Cliente: {entry_nome.get()}\n"
        resumo += f"Número do pedido: {numero}\n"
        resumo += "-" * 40 + "\n"

        for nome, preco in pedidos:
            resumo += f"{nome} — R$ {preco},00\n"

        resumo += "-" * 40 + "\n"
        resumo += f"TOTAL: R$ {total},00\n"
        resumo += f"Pagamento: {forma}\n"
        resumo += "=" * 40 + "\n"
        resumo += "Obrigado pela compra! 🍔"

        # ✅ SALVAMENTO AUTOMÁTICO
        salvar_nota(resumo, entry_nome.get(), numero)

        if forma == "Dinheiro":
            messagebox.showinfo("Pagamento", "Efetue o pagamento no balcão")
        else:
            messagebox.showinfo("Pagamento", "Pagamento Aprovado")

        messagebox.showinfo("Nota Fiscal", resumo)
        sys.exit()

    tk.Button(janela2, text="Pix", width=20, command=lambda: pagar("Pix")).pack(pady=5)
    tk.Button(janela2, text="Cartão de débito", width=20, command=lambda: pagar("Cartão de débito")).pack(pady=5)
    tk.Button(janela2, text="Dinheiro", width=20, command=lambda: pagar("Dinheiro")).pack(pady=5)
    tk.Button(janela2, text="Voltar", width=20, command=janela2.destroy).pack(pady=10)


# ================== JANELA PRINCIPAL ==================
janela = tk.Tk()
janela.title("FastFood")
janela.state("zoomed")

for i in range(4):
    janela.columnconfigure(i, weight=1)

for i in range(10):
    janela.rowconfigure(i, weight=1)

# ================== INTERFACE ==================

titulo = tk.Label(janela, text="🍔 FAST FOOD", font=("Arial", 20, "bold"))
titulo.grid(row=0, column=0, columnspan=4, pady=10)

tk.Label(janela, text="Nome:").grid(row=1, column=0, sticky="e")
entry_nome = tk.Entry(janela)
entry_nome.grid(row=1, column=1, sticky="we", padx=5)

frame_cardapio = tk.Frame(janela, bd=2, relief="solid")
frame_cardapio.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

tk.Label(frame_cardapio, text="CARDÁPIO", font=("Arial", 12, "bold")).pack()

for codigo, nome, preco in cardapio:
    tk.Label(frame_cardapio, text=f"{codigo} - {nome} — R$ {preco},00").pack(anchor="w")

tk.Label(janela, text="Código do item:").grid(row=3, column=0, sticky="e")

entry_codigo = tk.Entry(janela)
entry_codigo.grid(row=3, column=1, sticky="we", padx=5)

frame_botoes = tk.Frame(janela)
frame_botoes.grid(row=4, column=0, columnspan=2, pady=10)

tk.Button(frame_botoes, text="Adicionar", width=15, command=adicionar_item).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text="Remover", width=15, command=remover_item).grid(row=0, column=1, padx=5)
tk.Button(frame_botoes, text="Finalizar Pedido", width=20, command=finalizar_pedido).grid(row=0, column=2, padx=5)

frame_pedidos = tk.Frame(janela, bd=2, relief="solid")
frame_pedidos.grid(row=2, column=2, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)

tk.Label(frame_pedidos, text="SEUS PEDIDOS", font=("Arial", 12, "bold")).pack()

lista = tk.Listbox(frame_pedidos)
lista.pack(fill="both", expand=True, padx=5, pady=5)

label_total = tk.Label(janela, text="TOTAL: R$ 0,00", font=("Arial", 12, "bold"))
label_total.grid(row=5, column=2, columnspan=2)

janela.mainloop()