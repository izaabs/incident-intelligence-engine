# Regras de decisão para classificar prioridade, substitui vários ifs espalhados pelo código

regras_prioridade = [
     {
        "erro": "timeout", # só considera crítico se for lento
        "tempo_min": 2000,
        "prioridade": "alta"
    },
    {
        "erro": "falha_pagamento", # sempre crítico
        "prioridade": "critica"
    },
    {
        "erro": "instabilidade",
        "prioridade": "media"
    }
]