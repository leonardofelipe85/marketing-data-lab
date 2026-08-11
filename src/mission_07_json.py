# Marketing Data Lab — Sprint 5, Missão 7

## Manipulação de Arquivos: leitura de dados em formato JSON

#---

## Objetivo da missão

#Aprender a ler dados estruturados em formato JSON e utilizá-los dentro de
#programas Python, comparando essa abordagem com a leitura de arquivos CSV
#feita anteriormente — reaproveitando as mesmas funções de classificação
#e cálculo de orçamento, sem alterá-las.

import json 

from mission_07_file_reading import calcular_total_orcamento, classificar_campanha 

def carregar_campanhas_json(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados

caminho = "datasets/campaings.json"
campaigns = carregar_campanhas_json(caminho)
print(campaigns)

total = calcular_total_orcamento(campaigns)
print(f"Orçamento Total: R$ {total:.2f}")

for campaign in campaigns:
    status = classificar_campanha(campaign)
    print(status)