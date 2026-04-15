# 📊 Sistema de Classificação de Leads

Projeto desenvolvido em Python com o objetivo de automatizar a análise e priorização de leads comerciais, reduzindo o tempo de processamento manual e aumentando a eficiência do time de vendas.

## 🚀 Funcionalidades

- Leitura de leads a partir de arquivo JSON, podendo ser adaptável a qualquer instante.
- Validação de dados (evita erros de entrada)
- Classificação automática de leads:
  - 🔥 Quente
  - 🟡 Morno
  - ❄️ Frio
- Geração de relatório automático (`resultado.txt`)
- Sistema interativo via terminal
- Cadastro de novos leads

## 💡 Objetivo

Simular um cenário real de operação comercial onde leads são recebidos e precisam ser analisados e priorizados rapidamente.

O sistema automatiza essa decisão, permitindo:

- Redução de erros humanos
- Aumento de produtividade
- Priorização eficiente de atendimento
- Geração de insights para o time comercial

## 🧠 Lógica de Classificação

- Alta renda + alto interesse → 🔥 Quente
- Renda média → 🟡 Morno
- Baixa renda → ❄️ Frio

## 🛠️ Tecnologias

- Python
- JSON

## ▶️ Como executar

```bash
python main.py