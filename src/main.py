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

campaign_days = 20 

total_leads = 1250

leads_per_week = 100

# ========================================================
# Cálculo das Métricas 
# ========================================================

# Indicadores de Desempenho 

cpc = daily_budget / clicks
conversion_rate = (conversions / clicks) * 100
cost_per_conversion = daily_budget / conversions

# Controle de Orçamento 

monthly_budget = 3000.00
spent = 1845.00
remaining_budget = monthly_budget - spent
budget_increase = 500.00
new_budget = monthly_budget + budget_increase
total_budget = daily_budget * campaign_days

# Distribuição de Leads 

complete_weeks = total_leads // leads_per_week
remaining_leads = total_leads % leads_per_week
weeks_needed = total_leads / leads_per_week

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

if cpc <= 1:
    print(f"{'Análise':.<20} Excelente CPC")

elif cpc <= 2:
    print(f"{'Análise':.<20} CPC Aceitável") 

else: 
    print(f"{'Análise':.<20} CPC Elevado")

print("=" * 50)
print("CONTROLE ORÇAMENTÁRIO")
print("=" * 50)

print(f"{'Orçamento Mensal':.<20} R$ {monthly_budget:.2f}")
print(f"{'Valor Gasto':.<20} R$ {spent:.2f}")
print(f"{'Saldo Restante':.<20} R$ {remaining_budget:.2f}")
print(f"{'Aumento':.<20} R$ {budget_increase:.2f}")
print(f"{'Novo Orçamento':.<20} R$ {new_budget:.2f}")
print(f"{'Dias da Campanha':.<20} {campaign_days}")
print(f"{'Orçamento Total':.<20} R$ {total_budget:.2f}")

print("=" * 50)
print("PLANEJAMENTO COMERCIAL")
print("=" * 50)

print(f"{'Leads Totais':.<20} {total_leads}")
print(f"{'Leads/Semana':.<20} {leads_per_week}")
print(f"{'Semanas (Média)':.<20} {weeks_needed:.2f}")
print(f"{'Semanas Completas':.<20} {complete_weeks}")
print(f"{'Leads Restantes':.<20} {remaining_leads}")


