# Análise de Consumo - Marketing Campaign Results

Dados de campanha de marketing de 2.240 clientes da Maven Marketing, 
incluindo perfis de clientes, preferências de produtos, 
desempenho do canal e sucesso da campanha.

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

**1. Qual o total de vendas da empresa**

Essa empresa teve 33291 compras, sendo 12970 compras em suas lojas físicas, e 9150 pela web. 
Foram as maiores vendas em quantidade, pois o somatório das vendas por catálogo e com desconto não superaram as vendas presenciais.

**2. A empresa está em crescimento**

A empresa está em crescimento? Não está, as variações percentuais mostram que desde o início das vendas a empresa se mantém instável, 
com variações bem laterais e com momentos de grandes quedas. 
O único mês que ela se superou foi no segundo mês, em agosto de 2012 
com uma quantidade de 2026 vendas. Fora isso ela se manteve bem próximo à média.

**3. Valor gasto nos produtos**

O gasto maior foi em vinho, US$ 680.816,00 e em carne US$ 373.968,00 nos últimos 2 anos.

**4. Qual campanha os clientes mais compram**

A maioria das compras ocorrem na quarta campanha, seguindo um fluxo da terceira até a quinta com bastante compra. A segunda campanha foi a pior de todas.

**5. Qual o país mais consome esses produtos**

A Espanha lidera com um consumo de US$ 662.220,00 e o segundo colocado, a Arábia Saudita com um consumo de US$ 211.071,00. A Espanha gasta quase 3 vezes mais que a Arabia Saudita.

**6. Tempo de relacionamento dos clientes com a empresa**

Temos quase 50% de clientes com mais de 1 ano de conta ativa, e pouco menos de 50% tem conta a menos de 1 ano.

**7. Faixa etária dos clientes**

2112 dos clientes têm entre 24 e 65 anos, representando 94.29% do total de clientes.

**8. Quantos clientes estão insatisfeitos**

A empresa recebeu menos de 1% de reclamação do total de clientes dela, sendo considerável um nível de satisfação muito bom.

## Estrutura do Projeto

- `dashboard/` - Insights visualizados no Metabase, organizados com capa e dashboard
- `data/` - CSVs extraídos das consultas SQL
- `python/`
  - `analysis.ipynb` - Análise completa feita no Jupyter Notebook
  - `database.py` - Conexão com o banco de dados
  - `pipeline.py` - Estrutura completa para análises futuras
  - `quality_checks.py` - Verificação de qualidade dos arquivos gerados
  - `queries.py` - Todas as consultas SQL usadas na análise
- `queries/` - Consultas SQL usadas na análise
- `raw/` - CSVs originais, como vieram da fonte de dados
