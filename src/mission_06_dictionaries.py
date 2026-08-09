"""
Marketing Data Lab

Sprint 1 - Missão 6

Objetivo:
Aprender a trabalhar com dicionários em Python,
organizando informações de campanhas do Google Ads
em estruturas de dados mais completas.
"""

# Criação da primeira campanha

campaign = {
    "nome": "Pesquisa - Marca",
    "tipo": "Rede de Pesquisa",
    "ctr": 4.2, 
    "orçamento": 50.00
    }

# Criação da lista de campanhas

campaigns = [campaign]

# Adicionando novas campanhas

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
#campaigns[1]["nome"]
#print(campaigns[1]["nome"])

# Alterando informações de uma campanha

campaigns[1]["ctr"] = 3.2

# Exibindo todas as campanhas

for campaign in campaigns:  
    print(f'{campaign["nome"]} - '
        f'CTR: {campaign["ctr"]}% - '
        f'Orçamento: R$ {campaign["orçamento"]:.2f}')


# Classificando as campanhas de acordo com o CTR

for campaign in campaigns: 
    if campaign["ctr"] < 3.0: 
        print(f'{campaign["nome"]} - Crítico')
    elif campaign["ctr"] <4.0: 
        print(f'{campaign["nome"]} - Atenção')
    else: 
        print(f'{campaign["nome"]} - CTR dentro da meta')


# Calculando o orçamento total das campanhas


total_orçamento = 0

for campaign in campaigns:
    total_orçamento += campaign["orçamento"]
print(f'Orçamento Total: R$ {total_orçamento:.2f}')