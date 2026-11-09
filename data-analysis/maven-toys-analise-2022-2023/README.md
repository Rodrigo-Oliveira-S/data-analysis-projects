# Maven Toys — Análise de Desempenho (2022-2023)

Análise de vendas e rentabilidade de uma rede de lojas de brinquedos no México, entre janeiro de 2022 e setembro de 2023.

## Ferramentas

PostgreSQL | Excel | Power Query

## O que analisei

- Faturamento bruto e líquido por mês, trimestre e ano
- O mês mais atípico (Março/2023) com drill-down por categoria, loja e produto
- Margem de lucro por produto e categoria
- Crescimento da rede em 2023 comparado a 2022
- Sazonalidade do produto mais lucrativo

## Principais descobertas

- Março/2023 foi um mês atípico — sem data comemorativa, quase empatou com Dezembro/2022 em lucro líquido
- Colorbuds é o produto mais lucrativo (US$ 834.944), com margem de 53% — quase 3x mais que o segundo colocado
- Art & Crafts quase empata com Toys no lucro líquido, mesmo vendendo menos unidades
- Em apenas 9 meses, 2023 já atingiu 83% do lucro de 2022 inteiro
- O produto mais vendido não é o mais caro nem o mais barato — está na faixa de preço médio com margem alta

## Estrutura

- `dados/` — CSVs extraídos das consultas SQL
- `queries/` — Consultas SQL usadas na análise
- `dashboard/` — Planilha com capa, dados brutos, análises de apoio e dashboard final