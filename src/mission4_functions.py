"""
Marketing Data Lab

Sprint 1 - Missão 4

Objetivo:
Aprender a criar funções (def),
organizar o código e reutilizar lógica.
"""
def classify_ctr(ctr):
    if ctr >=4: 
        return "Excelente"
    elif ctr>=2:
        return "Boa"
    elif ctr >= 1: 
        return "Atenção"
    else: 
        return "Crítico"

resultado = classify_ctr(3.5)
print(resultado)

# ==========================================
# Testes da função
# ==========================================

print(classify_ctr(5))
print(classify_ctr(2.5))
print(classify_ctr(1.2))
print(classify_ctr(0.5))


campaign_names = [
    "Rede de Display", 
    "Performance Max", 
    "YouTube",
    "Rede de Pesquisa", 
    "Google Shopping", 
    ]

campaign_ctr = [
    4.5,
    2.3,
    0.8,
    3.1,
    1.5
]
print("=" * 50)
print("RELATÓRIO DE CTR")
print("=" * 50)

for i, (nome,ctr) in enumerate(
    zip(campaign_names, campaign_ctr), start=1
): 
    classification = classify_ctr(ctr)
    print(f"{'Campanha':.<25} {i}")

    print(f"{'Nome':.<25} {nome}")
    print(f"{'CTR':.<25} {ctr:.1f}%")
    print(f"{'Classificação':.<25} {classification}")
    print("-" * 50)






















