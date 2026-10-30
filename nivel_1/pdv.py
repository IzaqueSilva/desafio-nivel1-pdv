historico = []

print("=" * 50)
print("   BEM-VINDO AO PDV — PONTO DE VENDA")
print("=" * 50)
print("Digite 0 no valor da compra para encerrar.\n")

while True:

    valor_str = input("Valor da compra (R$): ")
    valor = float(valor_str)

    if valor == 0:
        break

    while valor < 0:
        print("⚠  Valor inválido! O valor não pode ser negativo.")
        valor_str = input("Valor da compra (R$): ")
        valor = float(valor_str)
        if valor == 0:
            break

    if valor == 0:
        break

    idade_str = input("Idade do cliente: ")
    idade = int(idade_str)

    while idade < 0:
        print("⚠  Idade inválida! A idade não pode ser negativa.")
        idade_str = input("Idade do cliente: ")
        idade = int(idade_str)

    qtd_str = input("Quantidade de itens: ")
    qtd = int(qtd_str)

    while qtd < 1:
        print("⚠  Quantidade inválida! Deve ser pelo menos 1.")
        qtd_str = input("Quantidade de itens: ")
        qtd = int(qtd_str)

    cupom = input("Cupom de desconto (ou ENTER para pular): ").strip()

    valor_original = valor
    desconto_total = 0.0

    if idade >= 65:
        desconto_idade = valor * 0.20
        valor = valor - desconto_idade
        desconto_total = desconto_total + desconto_idade

    if valor > 100:
        desconto_valor = valor * 0.10
        valor = valor - desconto_valor
        desconto_total = desconto_total + desconto_valor

    if qtd > 3:
        desconto_qtd = valor * 0.05
        valor = valor - desconto_qtd
        desconto_total = desconto_total + desconto_qtd

    if cupom.upper() == "FIDELIDADE10":
        desconto_cupom = valor * 0.10
        valor = valor - desconto_cupom
        desconto_total = desconto_total + desconto_cupom

    valor_final = round(valor, 2)
    desconto_total = round(desconto_total, 2)

    print("-" * 40)
    print(f"  Valor original:   R$ {valor_original:.2f}")
    print(f"  Desconto total:   R$ {desconto_total:.2f}")
    print(f"  Valor final:      R$ {valor_final:.2f}")
    print("-" * 40)
    print()

    compra = {
        "valor_original": valor_original,
        "idade": idade,
        "quantidade": qtd,
        "cupom": cupom,
        "desconto": desconto_total,
        "valor_final": valor_final
    }
    historico.append(compra)

print("\n" + "=" * 50)
print("   RESUMO DO DIA")
print("=" * 50)

quantidade_compras = len(historico)

if quantidade_compras == 0:
    print("Nenhuma compra registrada hoje.")
else:
    total_bruto = 0.0
    total_descontos = 0.0
    total_final = 0.0

    for compra in historico:
        total_bruto = total_bruto + compra["valor_original"]
        total_descontos = total_descontos + compra["desconto"]
        total_final = total_final + compra["valor_final"]

    print(f"  Compras registradas:  {quantidade_compras}")
    print(f"  Total bruto:          R$ {total_bruto:.2f}")
    print(f"  Total de descontos:   R$ {total_descontos:.2f}")
    print(f"  Total final:          R$ {total_final:.2f}")
    print("=" * 50)

    arquivo = open("nivel_1/resumo.txt", "w", encoding="utf-8")
    arquivo.write("RESUMO DO DIA\n")
    arquivo.write("=" * 40 + "\n\n")

    for j, c in enumerate(historico):
        arquivo.write(f"Compra {j + 1}:\n")
        arquivo.write(f"  Valor original: R$ {c['valor_original']:.2f}\n")
        arquivo.write(f"  Idade: {c['idade']}\n")
        arquivo.write(f"  Quantidade: {c['quantidade']}\n")
        arquivo.write(f"  Cupom: {c['cupom'] if c['cupom'] else '(nenhum)'}\n")
        arquivo.write(f"  Desconto: R$ {c['desconto']:.2f}\n")
        arquivo.write(f"  Valor final: R$ {c['valor_final']:.2f}\n")
        arquivo.write("-" * 30 + "\n")

    arquivo.write(f"\nCompras registradas: {quantidade_compras}\n")
    arquivo.write(f"Total bruto:         R$ {total_bruto:.2f}\n")
    arquivo.write(f"Total de descontos:  R$ {total_descontos:.2f}\n")
    arquivo.write(f"Total final:         R$ {total_final:.2f}\n")
    arquivo.close()

    print("\n📄 Resumo salvo em 'resumo.txt'.")

print("\nObrigado por usar o PDV. Até a próxima! 👋")
