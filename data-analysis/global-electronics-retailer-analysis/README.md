# Análise de Desempenho - Global Electronics Retailer

Dados de vendas para um varejista de eletrônicos global fictício, incluindo tabelas contendo informações sobre transações, produtos, clientes, lojas e taxas de câmbio.

## Ferramentas

- Podman (containers, redes e volumes)
- PostgreSQL
- Python (Jupyter Notebook, pandas, SQLAlchemy)
- Metabase

## Metodologia

1. **Armazenamento:** Dados brutos carregados no PostgreSQL via Python (pandas + SQLAlchemy).
2. **Processamento:** Consultas SQL modulares organizadas em `queries.py`, executadas via Jupyter Notebook.
3. **Qualidade:** Testes automatizados com `quality_checks.py` validam consistência dos dados.
4. **Visualização:** Dashboard interativo no Metabase com KPIs e segmentações.
5. **Automação:** Pipeline reprodutível com script Python e CI/CD via GitHub Actions.

## Análise e Descobertas

**1. Faturamento Líquido Total**

Faturamento Líquido Total de US$ 32,6 M.
O melhor mês foi Dezembro de 2019 com um Faturamento Líquido de US$ 1.435.548,24

**2. Ticket Médio do Faturamento Líquido Total**

Ticket Médio de US$ 2.117,89

**3. Produto que mais vendeu no mês**

O produto mais vendido no melhor mês da empresa foi o Adventure Works Desktop PC2.33 XD233 Black, vendido em Dezembro de 2019, somando US$ 22.678,25 em vendas nesse mês.

**4. Qual país mais comprou no mês**

O País que mais trouxe lucro para a empresa no melhor mês foi os EUA com US$ 742.893,25, seguido por Reino Unido, Canadá, Alemanha e Austrália.

**5. Qual moeda foi mais utilizada nas compras no mês**

A moeda mais usada para transacionar mercadorias foi o Dólar Americano (USD) movimentando US$ 1.282.986,92 apenas no período de um mês, de Dezembro de 2019, que foi o melhor mês.

**6. Margem de Lucro das vendas no mês**

A margem de lucro desse mês que foi o melhor, foi de 57.95%

## Estrutura do Projeto

- `dashboard/` - Insights visualizados no Metabase, organizados com gráficos no dashboard
- `data/` - CSVs extraídos das consultas SQL
- `python/`
  - `analysis.ipynb` - Análise completa feita no Jupyter Notebook
  - `database.py` - Conexão com o banco de dados
  - `data_import.py` - Importação dos CSVs para o banco de dados
  - `pipeline.py` - Estrutura completa para análises futuras
  - `quality_checks.py` - Verificação de qualidade dos arquivos gerados
  - `queries.py` - Todas as consultas SQL usadas na análise
- `queries/` - Consultas SQL usadas na análise
- `raw/` - CSVs originais, como vieram da fonte de dados
