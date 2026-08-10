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