"""
Marketing Data Lab

Sprint 1 - Missão 2

Objetivo:
Registrar informações de uma campanha de marketing
e calcular seus principais indicadores de desempenho.
"""

campaign_name = "Pesquisa - Canecas Personalizadas para Empresas"

platform = "Google Ads"

daily_budget = 50.00

clicks = 135

conversions = 8

active_campaign = "Ativa"

# Calculo das Métricas 


# Indicadores de Desempenho 

cpc = daily_budget / clicks
conversion_rate = (conversions / clicks) * 100
cost_per_conversion = daily_budget / conversions

# Controle de Orçamento 

monthly_budget = 3000.00
spent = 1845.00
remaining_budget = monthly_budget - spent


print("=" * 50)
print("MARKETING DATA LAB")
print("=" * 50)

print(f"{'Campanha':.<20} {campaign_name}") 
print(f"{'Plataforma':.<20} {platform}")
print(f"{'Orçamento Diário':.<20} R$ {daily_budget:.2f}")
print(f"{'Cliques':.<20} {clicks}")
print(f"{'Conversões':.<20} {conversions}")
print(f"{'Status':.<20} {active_campaign}")

print("=" * 50)  # Separador entre os dados e as métricas

print(f"{'CPC':.<20} R$ {cpc:.2f}")
print(f"{'Taxa Conversão':.<20} {conversion_rate:.2f}%")
print(f"{'Custo/Conversão':.<20} R$ {cost_per_conversion:.2f}")

print("=" * 50)
print("CONTROLE ORÇAMENTÁRIO")
print("=" * 50)

print(f"{'Orçamento Mensal':.<20} R$ {monthly_budget:.2f}")
print(f"{'Valor Gasto':.<20} R$ {spent:.2f}")
print(f"{'Saldo Restante':.<20} R$ {remaining_budget:.2f}")


