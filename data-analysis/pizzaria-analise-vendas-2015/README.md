## Pizzaria — Análise de Vendas (2015)

Análise de vendas de uma pizzaria durante o ano de 2015.

## Ferramentas: 

- PostgreSQL 
- Excel 
- Power Query

## O que analisei

- Faturamento mensal e sazonalidade ao longo do ano
- Melhor mês (julho) em detalhes: vendas diárias e dia da semana
- Top 10 sabores mais vendidos (quantidade vs faturamento)
- Categorias mais lucrativas e drill-down na categoria Classic

## Principais descobertas

- Julho foi o melhor mês (férias + inverno); outubro foi o pior
- Sexta-feira é o dia mais lucrativo em julho (R$ 14.306,85)
- Pizzas de frango lideram faturamento; Classic domina em volume
- Hawaiian é a mais vendida, mas fica em 5º em faturamento

## Estrutura

- `dados/` — CSVs extraídos (anual e julho)
- `queries/` — Consultas SQL usadas na análise
- `dashboard.xlsx` — Planilha com tabelas, gráficos e KPIs
- `dashboard-anual.png` — Visão geral do ano
- `dashboard-julho.png` — Detalhamento do melhor mês
