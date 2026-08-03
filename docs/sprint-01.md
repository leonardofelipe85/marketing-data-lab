# Sprint 1 - Fundamentos do Python

## Missão 1 - Variáveis e Tipos de Dados

### Objetivo

Construir o primeiro programa do Marketing Data Lab registrando informações de uma campanha de marketing.

### Conceitos estudados

- Variáveis
- Tipos de dados (`str`, `int`, `float` e `bool`)
- Função `print()`
- f-strings
- Formatação de texto
- Formatação de valores monetários (`:.2f`)
- Alinhamento de colunas (`:.<20`)

### Aplicação prática

Desenvolvimento de um relatório de campanha contendo:

- Nome da campanha
- Plataforma
- Orçamento diário
- Cliques
- Conversões
- Status

### Aprendizados

- O tipo de um dado depende do seu significado, não apenas da sua aparência.
- Um código de produto pode ser uma `string`.
- Variáveis devem possuir nomes claros e descritivos.
- A apresentação dos dados também faz parte da qualidade do software.

---

# Missão 2 - Operadores e Métricas

### Objetivo

Transformar dados da campanha em indicadores de desempenho.

### Métricas implementadas

- CPC (Custo por Clique)
- Taxa de Conversão
- Custo por Conversão

### Fórmulas

```python
cpc = daily_budget / clicks

conversion_rate = (conversions / clicks) * 100

cost_per_conversion = daily_budget / conversions
```

### Conceitos estudados

- Operador de divisão (`/`)
- Operador de multiplicação (`*`)
- Uso de variáveis em cálculos
- Reutilização de resultados
- Formatação de números (`:.2f`)

### Próximos desafios

- Operadores matemáticos restantes
- Tratamento de divisão por zero
- Estruturas condicionais (`if`)
- Comparação entre campanhas


## Diário de Bordo

Nesta sprint ficou claro que aprender através de um projeto faz muito mais sentido do que apenas assistir a vídeos.

Os conceitos de variáveis e tipos de dados foram assimilados com facilidade porque foram aplicados em um cenário real de Marketing.

Também ficou evidente a importância de organizar o código desde o início, utilizando Git, documentação e commits pequenos.

## Erros encontrados

### String literal is unterminated

Causa:
A docstring (`"""`) não havia sido fechada.

Aprendizado:
Quando esse erro aparecer, verificar primeiro:

- fechamento de aspas (")
- fechamento de aspas simples (')
- fechamento de docstrings (""")


Problema
        ↓
Quero aumentar o orçamento.

Dados
        ↓
monthly_budget
budget_increase

Operação
        ↓
+

Resultado
        ↓
new_budget

Exibição
        ↓
print()

