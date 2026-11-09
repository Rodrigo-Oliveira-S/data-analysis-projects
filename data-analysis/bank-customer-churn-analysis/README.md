# Análise de Desempenho - Bank Customer Churn

Informações da conta para 10.000 clientes em um banco europeu, incluindo detalhes sobre sua pontuação de crédito, 
saldo, produtos e se eles se agitaram.

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

**1. Volume total de saldo dos clientes por país**

O volume total de depósitos no banco é de US$ 390.834.299,47 divididos 
entre os países da França, com 2591 clientes ativos, Alemanha com 
1248 clientes ativos e Espanha com 1312 clientes ativos. 
Pela diferença dos valores entre França, com US$ 157.560.234,28 no 
banco, e a Alemanha com US$ 149.603.510,41 conseguimos ver que a 
Alemanha com quase 50% de clientes à menos, 
possui um saldo próximo a França, isso mostra que os saldos dos clientes 
da Alemanha podem ser bem altos.

**2. Qual a porcentagem do total de clientes que mais usam produtos do banco**

Apenas 0.56% dos clientes usam 4 produtos do banco, seguidos de 
2.19% que usam 3 serviços, 47.49% usam 2 serviços bancários e 
49.76% utilizam apenas 1 serviço bancário. No geral quase todos os 
clientes do banco utilizam entre 1 ou 2 serviços.

**3. Faixa de idade dos clientes ativos no banco**

A maioria, com 92.2% são clientes adultos, entre 24 e 65 anos de 
idade. Clientes abaixo de 24 anos, considerados jovens são 3.3% 
do total, e os clientes idosos, com mais de 65 anos, estão 
entre os 4.5% do total de clientes.

**4. Os clientes desse banco são novos ou são clientes antigos**

3279 clientes têm mais de 3 anos de relacionamento com o banco, 
representando 63.66% do total de clientes do banco. 1653 clientes 
têm entre 1 a 3 anos de conta ativa e representam 32.09% do total, 
e apenas 219 clientes são novos, têm menos de 1 ano, representando 
4.25% do total de clientes deste banco.

**5. Qual o perfil de renda dos clientes desse banco**

Estão divididos bem categoricamente entre as faixas de renda 
principais. 25.68% são de alta renda (US$ 100-150k), 
25.47% são de média renda (US$ 50-100k), 24.69% tem renda mais baixa
(Abaixo de US$ 50k) e a elite 24.15% (Acima de US$ 150k). Sendo assim 
o banco tem uma variação boa de clientes, captando entre ricos 
e o varejo.

**6. Porcentagem do total de clientes que cancelaram o serviço**

Dos clientes ativos do banco, 20,37% cancelaram a conta. 
A análise mostra que a maioria desses clientes eram adultos, 
tinham mais de 3 anos de conta, residem na França e usavam poucos 
produtos do banco. Mesmo com essa desistência, a França ainda lidera 
o ranking com mais depósitos em conta.

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
