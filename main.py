# Objetivo:
# Criar um sistema que:
# recebe incidentes, classifica prioridade, sugere ação, indica possível causa

import pandas as pd
from regras import regras_prioridade

# Passo 1 - Criar dados simulados
incidentes = [
    {"id": 1, "erro": "timeout", "tempo": 3000, "sistema": "API_A"},
    {"id": 2, "erro": "falha_pagamento", "tempo": 500, "sistema": "API_B"},
    {"id": 3, "erro": "instabilidade", "tempo": 1500, "sistema": "API_A"},
]


# Passo 2 - Classificar prioridade - "motor de decisão"
def classificar_prioridade(incidente):
    for regra in regras_prioridade: # percorre todas as regras existentes

        if incidente["erro"] == regra["erro"]:  # verifica se o erro do incidente bate com a regra

            if "tempo_min" in regra:

                if incidente["tempo"] >= regra["tempo_min"]:  # se o tempo for maior que o mínimo exigido
                    return regra["prioridade"]
            else:
                return regra["prioridade"] # regra sem condição adicional
            
    return "baixa" # caso nenhuma regra seja atendida


# Passo 3 - Definir ação
def definir_acao(prioridade):
    if prioridade == "critica":
        return "escalar imediatamente" 
    
    elif prioridade == "alta":
        return "investigar urgente"
    
    elif prioridade == "media":
        return "monitorar e investigar"
    
    else: # prioridade baixa
        return "acompanhar"
    

# Passo 4 - Identificar causa raiz (simulação)
def identificar_causa(incidente):
    if incidente["erro"] == "timeout" and incidente["sistema"] == "API_A":
        return "possível sobrecarga"
    
    elif incidente["erro"] == "falha_pagamento":
        return "falha na integração"
    
    else:
        return "causa desconhecida"
    

# Passo 5 - Pipeline principal
resultados = []

# (entrada → processamento → saída)
# pipeline de dados simplificado

for inc in incidentes:

    prioridade = classificar_prioridade(inc)
    acao = definir_acao(prioridade)
    causa = identificar_causa(inc)

    inc["prioridade"] = prioridade
    inc["acao"] = acao
    inc["causa"] = causa

    resultados.append(inc)


# Passo 6 - Mostrar resultados
for r in resultados:
    print(f"Incidente {r['id']}: Prioridade={r['prioridade']}, Ação={r['acao']}, Causa={r['causa']}")


# Passo 7 - Salvar CSV
df = pd.DataFrame(resultados)
df.to_csv("output.csv", index=False)