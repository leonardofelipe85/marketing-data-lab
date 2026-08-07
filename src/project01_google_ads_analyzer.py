"""
Marketing Data Lab

Projeto 1 - Google Ads Campaign Analyzer

Objetivo:
Desenvolver um sistema para análise de campanhas do Google Ads,
aplicando os conceitos estudados em Python, como estruturas de
repetição, funções, organização de código e geração de relatórios.

Status:
🚧 Em desenvolvimento
"""

#Nome da campanha = 
#Tipo da campanha = 
#Investimento = 
#CTR
#CPC
#Conversões
#CPA

def classify_ctr(ctr):
    if ctr >=4: 
        return "Excelente"
    elif ctr>=2:
        return "Boa"
    elif ctr >= 1: 
        return "Atenção"
    else: 
        return "Crítico"

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

print("=" * 50)
print("RELATÓRIO DE CAMPANHAS")
print("=" * 50)

for i, (nome, tipo, ctr) in enumerate (zip(campaign_names, campaign_types, campaign_ctr), start=1): 


    classification = classify_ctr(ctr)

    print(f"{'Campanha':.<25} {i}")
    print(f"{'Nome':.<25} {nome}")
    print(f"{'Tipo':.<25} {tipo}")
    print(f"{'CTR':.<25} {ctr:.1f}%")
    print(f"{'Classificação':.<25} {classification}")
    print("-" * 50)