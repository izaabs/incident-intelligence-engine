# 🚨 Incident Intelligence Engine

Sistema em Python para classificação inteligente de incidentes, com priorização automática, sugestão de ação e análise inicial de causa raiz.

---

## 🎯 Objetivo

Simular um fluxo real de tratamento de incidentes, transformando dados brutos em decisões operacionais.

O projeto foi desenvolvido com foco em:
- Automação de processos
- Pensamento orientado a eventos (event-driven)
- Introdução a conceitos de SRE (Site Reliability Engineering)

---

## ⚙️ Funcionalidades

- 📥 Recebimento de incidentes simulados  
- 🧠 Classificação de prioridade baseada em regras  
- 🎯 Definição automática de ações  
- 🔍 Identificação inicial de possível causa raiz  
- 📊 Geração de saída estruturada  

---

## 🧠 Lógica do Sistema

O projeto utiliza um modelo baseado em regras (rule-based system), onde:

- As regras são configuráveis (`regras.py`)
- O sistema interpreta essas regras dinamicamente
- Evita uso de lógica linear rígida (vários `if` espalhados)

---

## 📂 Estrutura do Projeto

incident-intelligence-engine/
│
├── main.py # pipeline principal
├── regras.py # regras de decisão
└── README.md

---

## ▶️ Como executar

```bash
python main.py
```

---

## 🧪 Exemplo de uso

Entrada:
-Incidentes com erro, tempo de resposta e sistema

Saída:
- Prioridade atribuída
- Ação recomendada
- Possível causa

---

## 🚀 Conceitos aplicados

- Event-driven architecture
- Processamento de eventos
- Rule-based decision system
- Root Cause Analysis (RCA)
- Pensamento SRE

---

## 🔮 Próximos passos

- Integração com AWS (Lambda / S3)
- Automação baseada em eventos reais
- Substituição de regras por Machine Learning
- Criação de API para classificação

---

## 👩‍💻 Autora

Izabelli Ribeiro
