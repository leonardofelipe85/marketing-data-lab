"""
Marketing Data Lab

Sprint 1 - Missão 5

Objetivo:
Aprender a manipular listas em Python,
aplicando os conceitos ao contexto de
campanhas do Google Ads.
"""
campaign_names = [
    "Pesquisa - Marca",
    "Shopping - Canecas",
    "Display - Presente Dia dos Pais"
]

campaign_types = [
    "Rede de Pesquisa", 
    "Shopping", 
    "Display"
]

campaign_ctr = [
    4.2,
    2.8,
    3.4
]

# Adicionando uma nova campanha
campaign_names.append("Performance Max - Natal")
campaign_types.append("Performance Max")
campaign_ctr.append(3.1)

# Quantidade de campanhas
print(len(campaign_names)) 

# Primeira campanha
print(campaign_names[0])

# Última campanha
print(campaign_names[-1])

# Índice da campanha Display
print(campaign_names.index("Display - Presente Dia dos Pais"))

# CTR atual da campanha
indice = campaign_names.index("Display - Presente Dia dos Pais")
campaign_ctr[indice] = 3.8

# Alterando o CTR
campaign_ctr[2] = 3.8

# Conferindo a lista atualizada
print(campaign_ctr)

indice = campaign_names.index("Shopping - Canecas")

campaign_names.pop(indice)
campaign_types.pop(indice)
campaign_ctr.pop(indice)

print(len(campaign_names))
print(len(campaign_types))
print(len(campaign_ctr))
