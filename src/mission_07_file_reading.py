# Marketing Data Lab — Sprint 5, Missão 7

## Manipulação de Arquivos: introdução à leitura de dados externos

# ==========================================

# OBJETIVO

# ==========================================

# Aprender a ler dados armazenados em arquivos externos e utilizá-los
# dentro de programas Python, começando pela leitura de arquivos de
# texto e evoluindo para formatos estruturados como CSV, JSON e Excel.


# ==========================================

# FUNÇÕES

# ==========================================

def carregar_campanhas(caminho_arquivo):
    campaigns = []

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas[1:]:
        dados = linha.strip().split(",")

        campaign = {
            "nome": dados[0],
            "tipo": dados[1],
            "ctr": float(dados[2]),
            "orçamento": float(dados[3])
        }

        campaigns.append(campaign)

    return campaigns


def calcular_total_orcamento(campaigns):
    total_orcamento = 0

    for campaign in campaigns:
        total_orcamento += campaign["orçamento"]

    return total_orcamento


def classificar_campanha(campaign):
    if campaign["ctr"] < 3.0:
        return f'{campaign["nome"]} - Crítico'
    elif campaign["ctr"] < 4.0:
        return f'{campaign["nome"]} - Atenção'
    else:
        return f'{campaign["nome"]} - CTR dentro da meta'


def calcular_ctr_medio(campaigns):
    total_ctr = 0

    for campaign in campaigns:
        total_ctr += campaign["ctr"]

    return total_ctr / len(campaigns)

def campanha_maior_orcamento(campaigns):
    maior = campaigns[0]

    for campaign in campaigns:
        if campaign["orçamento"] > maior["orçamento"]:
            maior = campaign

    return maior

def campanha_maior_ctr(campaings):
    maior = campaigns[0]

    for campaign in campaigns: 
        if campaign["ctr"] > maior["ctr"]: 
            maior = campaign

    return maior 

def campanha_menor_ctr(campaings): 
    menor = campaigns[0]

    for campaing in campaigns:
        if campaign["ctr"] < menor["ctr"]: 
            menor = campaign

    return menor 

# ==========================================

# EXECUÇÃO

# ==========================================

campaigns = carregar_campanhas("datasets/campaings.csv")


print("\n--- Lista Completa de Campanhas ---")

for campaign in campaigns:
    print(f"{'Campanha':.<20} {campaign['nome']}")
    print(f"{'Tipo':.<20} {campaign['tipo']}")
    print(f"{'CTR':.<20} {campaign['ctr']:.2f}%")
    print(f"{'Orçamento':.<20} R$ {campaign['orçamento']:.2f}")
    print()


total = calcular_total_orcamento(campaigns)

print(f"{'Orçamento Total':.<20} R$ {total:.2f}")


print("\n--- Classificação das Campanhas ---")

for campaign in campaigns:
    status = classificar_campanha(campaign)
    print(f"{'Status':.<20} {status}")
    print()


ctr_medio = calcular_ctr_medio(campaigns)

print(f"{'CTR Médio':.<20} {ctr_medio:.2f}%")

maior_orcamento = campanha_maior_orcamento(campaigns)

print("\n--- Maior Orçamento ---")
print(f"{'Campanha':.<20} {maior_orcamento['nome']}")
print(f"{'Orçamento':.<20} R$ {maior_orcamento['orçamento']:.2f}")

maior_ctr = campanha_maior_ctr(campaigns)

print("\n--- Maior CTR ---")
print(f"{'Campanha':.<20} {maior_ctr['nome']}")
print(f"{'CTR':.<20} {maior_ctr['ctr']:.2f}%")

menor_ctr = campanha_menor_ctr(campaigns)

print("\n--- Menor CTR ---")
print(f"{'Campanha':.<20} {menor_ctr['nome']}")
print(f"{'CTR':.<20} {menor_ctr['ctr']:.2f}%")