# PDV — Ponto de Venda com Descontos Progressivos

## O que o código faz

Este programa simula um **Ponto de Venda (PDV)** que calcula o valor final de compras aplicando **descontos progressivos**. O sistema recebe o valor da compra e a idade do cliente, aplica automaticamente descontos por faixa etária (idosos 65+) e por valor elevado (acima de R$ 100), exibe o valor final formatado e, ao encerrar, apresenta um resumo completo de todas as compras do dia.

## Como ele faz

1. O código inicia um **loop** que solicita o valor da compra e a idade do cliente.
2. **Validação**: se o valor ou a idade forem negativos, exibe um aviso e pede novamente.
3. **Regra 1 — Desconto por idade**: verifica se a idade é **≥ 65 anos**. Se sim, aplica **20% de desconto** sobre o valor original.
4. **Regra 2 — Desconto por valor**: verifica se o valor **já com desconto de idade** é **maior que R$ 100**. Se sim, aplica **10% extra** sobre esse valor já descontado.
5. **Bônus — Desconto por quantidade**: se a quantidade de itens for **maior que 3**, aplica **5% extra**.
6. **Bônus — Cupom de fidelidade**: se o cupom digitado for `FIDELIDADE10`, aplica **10% extra**.
7. Cada compra é guardada numa **lista** usando `.append()`.
8. O loop termina quando o usuário digita **0** no valor da compra.
9. Ao encerrar, o programa exibe um **resumo do dia** com quantidade de compras, total bruto, total de descontos e total final.
10. **Bônus**: o resumo é salvo automaticamente no arquivo `resumo.txt`.

## Como rodar

```bash
python pdv.py
```

> Para encerrar o programa, digite `0` quando solicitado o valor da compra.

## Tabela de Casos de Teste

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---|------------|-------|----------------|----------------|----------------------|
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |

### Atenção aos casos-limite

- **Caso 5** (125.00, idade 70): `125 × 0.8 = 100.00`. Como o valor **não é maior** que 100 (é igual), os 10% **não** se aplicam. Resultado: **R$ 100.00**.
- **Caso 10** (200.00, idade 64): a idade é 64 (< 65), então **não** tem desconto por idade. Só o de valor (10%). Resultado: **R$ 180.00**.
- **Caso 7** (101.00, idade 30): sem desconto de idade. `101 > 100`, então 10% de desconto: `101 × 0.9 = 90.90`.

## Recursos Bônus Implementados

- ✅ **Desconto por quantidade**: se a quantidade de itens for > 3, aplica 5% extra.
- ✅ **Cupom de fidelidade**: se o cupom for `FIDELIDADE10`, aplica 10% extra.
- ✅ **Salvar histórico**: ao encerrar, grava o resumo no arquivo `resumo.txt`.

## Estrutura de Entrega

```
nivel_1/
├── pdv.py        ← código do PDV
├── README.md     ← esta documentação
└── resumo.txt    ← gerado automaticamente ao encerrar (se houver compras)
```
