print("=" * 50)
print("MONITORAMENTO DE CAMPANHA")
print("=" * 50)


# ==========================================
# Monitoramento diário
# ==========================================

for day in range(1, 8):

    if day == 4:
        print(f"Dia {day}: Revisão das Campanhas.")

    else:
        print(f"Dia {day}: Campanha Monitorada com Sucesso. ")

print()  # linha em branco

# ==========================================
# Auditoria de CTR
# ==========================================

print("=" * 50)
print("AUDITORIA DE CTR")
print("=" * 50)

campaign_ctr = [2.8, 0.9, 3.5, 1.2, 4.1, 0.7]
excellent_campaigns = 0
good_campaigns = 0
attention_campaigns = 0
critical_campaigns = 0


for ctr in campaign_ctr:
    if ctr >= 4:
        classification = "Excelente"
        excellent_campaigns += 1

    elif ctr >= 2:
        classification = "Boa"
        good_campaigns += 1

    elif ctr >= 1:
        classification = "Atenção"
        attention_campaigns += 1

    else:
        classification = "Crítica"
        critical_campaigns += 1

    print(f"CTR {ctr:.1f}% -> {classification}")

print("=" * 50)
print("RESUMO DA AUDITORIA")
print("=" * 50)

print(f"{'Campanhas Excelentes':.<25} {excellent_campaigns}")
print(f"{'Campanhas Boas':.<25} {good_campaigns}")
print(f"{'Campanhas em Atenção':.<25} {attention_campaigns}")
print(f"{'Campanhas Críticas':.<25} {critical_campaigns}")

print()  # Em branco

print("=" * 50)
print("CONTROLE DE ORÇAMENTO")
print("=" * 50)

remaining_budget = 1000
daily_spend = 200
day = 1

while remaining_budget >= daily_spend:

    if remaining_budget >= 600:
        status = "Campanha Ativa"

    elif remaining_budget >= 400:
        status = "Atenção"

    else:
        status = "Crítico"

    print(f"{'Dia':.<25} {day}")
    print(f"{'Orçamento Restante':.<25} R$ {remaining_budget:.2f}")
    print(f"{'Status':.<25} {status}")
    print("-" * 50)

    remaining_budget -= daily_spend
    day += 1

print("Orçamento Encerrado.")

campaign_ctr = [4.5, 2.3, 0.8, 3.1, 1.5]

campaign_budgets = [1200, 800, 350, 950, 500]

print("=" * 50)
print("RELATÓRIO DE CAMPANHAS")
print("=" * 50)

for numero, (ctr, budget) in enumerate (zip(campaign_ctr, campaign_budgets), start=1): 

    if ctr >= 4:
        classification = "Excelente"
    elif ctr >=2: 
        classification = "Boa"
    elif ctr >= 1: 
        classification = "Atenção"
    else: 
        classification = "Crítica"

    
    if budget >= 1000: 
        budget_class = "Excelente"
    elif budget >= 700: 
        budget_class = "Bom" 
    elif budget >= 400: 
        budget_class = "Atenção"
    else:
        budget_class = "Crítico"

    print(f"Campanha {numero}")
    print(f"{'CTR':.<22} {ctr}%")
    print(f"{'Classificação':.<22} {classification}")
    print(f"{'Orçamento':.<22} R$ {budget:.2f}")
    print(f"{'Situação':.<22} {budget_class}")
    print("-" * 50)