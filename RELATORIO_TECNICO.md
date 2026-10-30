# Relatório Técnico: Resolução do Desafio Nível 1 — PDV com Descontos Progressivos

---

## 1. Visão Geral do Problema
O objetivo do desafio foi criar a lógica central de um **PDV (Ponto de Venda)** capaz de registrar múltiplas compras consecutivas, aplicar descontos progressivos (em cascata) segundo regras de negócio bem definidas, validar entradas do operador, manter um histórico acumulado e gerar relatórios analíticos (tanto no terminal quanto persistido em disco).

---

## 2. Decisões Arquiteturais e de Design

### 2.1. Aderência às Restrições Didáticas
O enunciado impôs restrições claras para avaliar o domínio dos fundamentos de lógica de programação:
* **Sem uso de funções (`def`)**: Todo o fluxo foi implementado de forma sequencial e estruturada.
* **Sem blocos de captura de exceção (`try/except`)**: A validação e o fluxo de controle apoiaram-se estritamente em estruturas de repetição (`while`) e condicionais (`if/else`).

### 2.2. Modelo de Execução e Loop Principal
* **Loop Indefinido (`while True`)**: Foi adotado um loop infinito que simula uma sessão contínua de caixa. O término ocorre apenas quando a condição de parada é satisfeita: entrada de valor igual a `0`.
* **Saída Segura e Precoce (`break`)**: O valor `0` é testado logo no início e também durante loops de validação secundários, permitindo que o operador encerre o caixa mesmo se tiver digitado incorretamente um valor negativo antes.

### 2.3. Lógica de Descontos em Cascata (Progressivos)
A ordem de aplicação e a base de cálculo foram cruciais para atender aos casos de teste:
1. **Regra 1 (Idade $\ge$ 65 anos)**: Aplica-se $20\%$ de abatimento sobre o valor original.
2. **Regra 2 (Valor residual $> 100$)**: Aplica-se $10\%$ extra **sobre o valor já recalculado** pela regra de idade. Caso o valor residual seja exatamente igual ou menor que $100$ (como no caso-limite de R$ 125,00 com cliente de 70 anos), os 10% **não** se aplicam.
3. **Bônus — Quantidade de Itens ($> 3$)**: Aplica-se $5\%$ sobre o saldo remanescente.
4. **Bônus — Cupom de Fidelidade (`FIDELIDADE10`)**: Se informado, aplica-se mais $10\%$ sobre o valor residual. Tratado com `.strip()` e `.upper()` para normalização de formato.
5. **Precisão Numérica**: Uso de `round(valor, 2)` para evitar distorções de ponto flutuante do padrão IEEE 754.

### 2.4. Estrutura de Dados e Persistência em Memória
* **Histórico em Lista (`list`)**: Cada transação finalizada é encapsulada em um **dicionário (`dict`)** contendo:
  * `valor_original`, `idade`, `quantidade`, `cupom`, `desconto`, `valor_final`.
* O uso de dicionários garante semântica clara e legibilidade na recuperação de campos (`compra["valor_final"]`), eliminando a fragilidade de índices numéricos de listas aninhadas.

### 2.5. Processamento Final e Persistência em Disco
* **Acumuladores via `for`**: Para o cálculo do resumo do dia (faturamento bruto, descontos e faturamento líquido), foi utilizado o loop `for compra in historico:`, atendendo rigorosamente à recomendação de código pythônico e ao enunciado de bônus.
* **Persistência em Arquivo (`resumo.txt`)**: Uso de `open("nivel_1/resumo.txt", "w", encoding="utf-8")` com iteração indexada via `enumerate()` para gerar um cupom detalhado transação por transação, garantindo a correta serialização com formatação monetária padrão (`:.2f`).

---

## 3. Ferramentas Utilizadas

| Ferramenta | Utilidade no Projeto |
|---|---|
| **Python 3.12+** | Interpretador da linguagem de desenvolvimento da aplicação. |
| **Git** | Sistema de controle de versão distribuído para rastreamento de commits e histórico de alterações. |
| **GitHub** | Plataforma remota para hospedagem do repositório, documentação pública e entrega. |
| **PowerShell / Terminal** | Ambiente de execução CLI para validação dos casos de teste manuais e comandos Git. |
| **Markdown** | Formatação das especificações técnicas, documentação de uso e tabela de casos de teste no [README.md](file:///c:/Desafio%20nivel1/README.md). |

---

## 4. Estrutura Final do Repositório

```text
desafio-nivel1-pdv/
├── README.md           ← Documentação principal renderizada na home do GitHub
└── nivel_1/
    ├── pdv.py          ← Script funcional do PDV
    ├── README.md       ← Documentação interna exigida pela estrutura de entrega
    └── resumo.txt      ← Arquivo gerado automaticamente ao fechar o caixa com vendas
```
