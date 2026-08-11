# Marketing Data Lab — Sprint 5, Missão 7

## Manipulação de Arquivos: introdução à leitura de dados externos

#---

## Objetivo da missão

#Aprender a ler dados armazenados em arquivos externos e utilizá-los dentro de programas Python, 
#começando pela leitura de arquivos de texto e evoluindo para formatos estruturados como CSV,
#JSON e Excel.


# ==========================================

# LEITURA DE ARQUIVOS

# ==========================================

def carregar_campanhas(caminho_arquivo): 
    campaings = []

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas[1:]: 
        dados = (linha.strip().split(","))

        campaing = {
        "nome": dados[0],
        "tipo": dados[1],
        "ctr": float(dados[2]),
        "orçamento":float(dados[3])
    }

        campaings.append(campaing)

    return campaings 

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


#========================================
#EXECUÇÃO 
#========================================

campaigns = carregar_campanhas("datasets/campaings.csv")

print(campaigns)

total = calcular_total_orcamento(campaigns)

print(f"Orçamento Total: R$ {total:.2f}")

for campaing in campaigns: 
    status = classificar_campanha(campaing)
    print(status)

      
