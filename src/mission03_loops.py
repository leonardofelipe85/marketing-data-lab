print("=" * 50)
print("MONITORAMENTO DE CAMPANHA")
print("=" * 50)


# ==========================================
# Monitoramento diário
# ==========================================

for day in range(1,8): 

    if day == 4: 
        print(f"Dia {day}: Revisão das Campanhas.")

    else: 
        print(f"Dia {day}: Campanha Monitorada com Sucesso. ")

print() # linha em branco 

# ==========================================
# Auditoria de CTR
# ==========================================

print("=" * 50)
print("AUDITORIA DE CTR")
print("=" * 50)

campaing_ctr = [2.8, 0.9, 3.5, 1.2, 4.1, 0.7]
healthy_campaings = 0
review_campaings = 0


for ctr in campaing_ctr: 
    if ctr >=2:
        print(f"CTR {ctr:.1f}% -> Campanha Saudável.")
        healthy_campaings += 1

    else: 
        print(f"CTR {ctr:.1f}% -> Revisar Campanha.")
        review_campaings += 1 

print("=" * 50)
print("RESUMO DA AUDITORIA")
print("=" * 50)

print(f"{'Campanhas Saudáveis':.<25} {healthy_campaings}")
print(f"{'Campanhas para Revisão':.<25} {review_campaings}")

print() # Em branco 

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






        