# Marketing Data Lab — Sprint 1, Missão 6

## Dicionários + Funções: de dados soltos a um pequeno sistema de processamento

---

## Objetivo da missão

Organizar informações de campanhas do Google Ads em dicionários completos e transformar a lógica repetida de exibição, classificação e cálculo em funções reutilizáveis.

---

## Conceitos praticados

- Dicionários
- Listas de dicionários
- `append()`
- Alteração de valores
- `for`
- `if / elif / else`
- Funções
- Parâmetros
- `return`
- Acumuladores
- Reutilização de código

---

## Passo a passo

### 1. Ponto de partida: dados incompletos

As campanhas nasciam só com `nome`, `tipo` e `ctr`. O `orçamento` era adicionado depois, em linhas soltas:

```python
campaigns[0]["orçamento"] = 50.0
```

Problema: retrabalho, e risco de esquecer o campo em alguma campanha.

### 2. Dados completos desde a criação

Os quatro dicionários foram reescritos para já nascerem com todas as chaves (`nome`, `tipo`, `ctr`, `orçamento`) juntas.

> **Observação de precisão:** isso não é uma regra absoluta — é uma boa prática **quando você já conhece todos os dados no momento da criação**. Em programas reais (ex.: dados vindos de um CSV), é normal um dado chegar incompleto e ser enriquecido depois.

### 3. Iterar, classificar e calcular

Três blocos de código, cada um com seu próprio `for`, faziam:
- Exibir cada campanha (`nome`, CTR, orçamento formatado)
- Classificar por CTR (`if/elif/else`: Crítico / Atenção / Dentro da meta)
- Somar o orçamento total (acumulador com `+=`)

Cada bloco só existia daquele jeito específico, ali. Repetir a mesma lógica em outro lugar exigiria copiar e colar tudo de novo.

### 4. Identificar a lógica repetida

Pergunta-chave: e se essa mesma regra precisar rodar em outro lugar, ou mudar um dia? Copiar e colar significa ter que lembrar de atualizar **todos** os lugares onde o código foi duplicado.

### 5. Criar funções

Cada bloco virou uma função:

```python
def exibir_campanhas(campaigns):
    ...

def classificar_campanha(campaign):
    ...

def calcular_total(campaigns):
    ...
```

### 6. Parâmetros: o que entra

- `exibir_campanhas` e `calcular_total` recebem a **lista inteira**, porque exibição e soma total só fazem sentido olhando o conjunto.
- `classificar_campanha` recebe **uma campanha por vez**, porque a classificação é uma propriedade individual — e assim ela também funciona sozinha, fora da lista (ex.: uma campanha nova, antes de ser adicionada).

### 7. `return`: o que sai

- `classificar_campanha` e `calcular_total` usam `return` — devolvem um valor (texto ou número) para quem chamou a função decidir o que fazer com ele: imprimir, guardar, comparar, contar.
- `exibir_campanhas` usa `print` direto, sem `return` — ela produz um **efeito** (mostrar na tela), não um valor para reaproveitar.

> Essa é uma distinção útil de guardar: funções que **fazem algo** (efeito colateral, como imprimir) vs. funções que **calculam algo** (devolvem um valor com `return`).

### 8. Testar a função isoladamente

Antes de confiar que `classificar_campanha` funcionava dentro da lista inteira, ela foi testada sozinha, com uma campanha (`nova_campanha`) que nunca entrou em `campaigns`:

```python
nova_campanha = {"nome": "PMax - Testes", "tipo": "Performance Max",
                  "ctr": 3.6, "orçamento": 175.00}
print(classificar_campanha(nova_campanha))
```

> **Observação de precisão:** isso segue a ideia de testar uma unidade isoladamente, mas é um **teste manual isolado da função** — não um teste unitário automatizado (como os que ferramentas como `pytest` fariam). O conceito está certo; vale só a distinção de vocabulário.

### 9. Remover duplicação

Com as funções prontas e testadas, os três blocos manuais originais (que faziam a mesma coisa) foram apagados. Sobrou uma única fonte de verdade para cada lógica.

### 10. Separar definição e execução

O arquivo foi reorganizado: primeiro o bloco de funções (`def`s), depois o bloco de execução (as chamadas). Isso deixa claro onde as regras são definidas e onde elas são usadas — um padrão comum em código profissional.

---

## Código final

```python
"""
Marketing Data Lab

Sprint 1 - Missão 6

Objetivo:
Aprender a trabalhar com dicionários em Python,
organizando informações de campanhas do Google Ads
em estruturas de dados mais completas.
"""

# ==========================================
# CRIAÇÃO DAS CAMPANHAS
# ==========================================

campaign = {
    "nome": "Pesquisa - Marca",
    "tipo": "Rede de Pesquisa",
    "ctr": 4.2,
    "orçamento": 50.00
}

campaigns = [campaign]

campaigns.append(
    {
        "nome": "Shopping - Canecas",
        "tipo": "Shopping",
        "ctr": 2.8,
        "orçamento": 80.00
    }
)

campaigns.append(
    {
        "nome": "Display - Presente Dia dos Pais",
        "tipo": "Display",
        "ctr": 3.4,
        "orçamento": 120.00
    }
)

campaigns.append(
    {
        "nome": "YouTube - Feriado Prolongado 7 de Setembro",
        "tipo": "YouTube",
        "ctr": 2.7,
        "orçamento": 95.00
    }
)

# ==========================================
# ALTERAÇÃO DE DADOS
# ==========================================

campaigns[1]["ctr"] = 3.2

# ==========================================
# FUNÇÕES
# ==========================================

def exibir_campanhas(campaigns):
    for campaign in campaigns:
        print(
            f'{campaign["nome"]} - '
            f'CTR: {campaign["ctr"]}% - '
            f'Orçamento: R$ {campaign["orçamento"]:.2f}'
        )


def classificar_campanha(campaign):
    if campaign["ctr"] < 3.0:
        return f'{campaign["nome"]} - Crítico'
    elif campaign["ctr"] < 4.0:
        return f'{campaign["nome"]} - Atenção'
    else:
        return f'{campaign["nome"]} - CTR dentro da meta'


def calcular_total(campaigns):
    total_orçamento = 0
    for campaign in campaigns:
        total_orçamento += campaign["orçamento"]
    return total_orçamento

# ==========================================
# TESTE COM CAMPANHA ISOLADA
# ==========================================

nova_campanha = {
    "nome": "PMax - Testes",
    "tipo": "Performance Max",
    "ctr": 3.6,
    "orçamento": 175.00
}

print("--- Teste de Campanha Isolada ---")
print(classificar_campanha(nova_campanha))

# ==========================================
# EXECUÇÃO
# ==========================================

print("\n--- Lista Completa de Campanhas ---")
exibir_campanhas(campaigns)

print("\n--- Classificação das Campanhas ---")

for campaign in campaigns:
    status = classificar_campanha(campaign)
    print(status)

total = calcular_total(campaigns)

print(f'\nOrçamento Total: R$ {total:.2f}')
```