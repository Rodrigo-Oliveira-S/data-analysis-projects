# Script de análise - CRM Sales Opportunities

mes = '2017-03'

# Importação dos dados

import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(
    f'postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}'
    f'@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/crm_sales_opportunities'
)

# 1. Faturamento mês a mês quanto foi

with engine.connect() as conn:
    query = f"""

    select
        to_char(sp.close_date::date, 'YYYY-MM') as data_fechamento,
        round(sum(sp.close_value)::numeric, 2) as faturamento
    from sales_pipeline sp
    join sales_teams st on st.sales_agent = sp.sales_agent
    join products p on p.product = sp.product
    join accounts a on a.account = sp.account
    where to_char(sp.close_date::date, 'YYYY-MM') = '{mes}'
        and sp.close_date is not null
        and sp.close_date != ''
    group by to_char(sp.close_date::date, 'YYYY-MM')
    order by to_char(sp.close_date::date, 'YYYY-MM');

    """

    resultado = conn.execute(text(query))
    df = pd.DataFrame(resultado.fetchall(), columns = resultado.keys())

df.to_csv('01-faturamento-geral.csv', index=False)

# 2. Qual empresa mais compra

with engine.connect() as conn:
    query = f"""

    select
        sp.account as empresa,
        round(sum(sp.close_value)::numeric, 2) as faturamento
    from sales_pipeline sp
    join sales_teams st on st.sales_agent = sp.sales_agent
    join products p on p.product = sp.product
    join accounts a on a.account = sp.account
    where to_char(sp.close_date::date, 'YYYY-MM') = '{mes}'
        and sp.close_date is not null
        and sp.close_date != ''
    group by sp.account
    order by faturamento desc
    limit 10;

    """

    resultado = conn.execute(text(query))
    df = pd.DataFrame(resultado.fetchall(), columns = resultado.keys())

df.to_csv('02-faturamento-empresa.csv', index=False)

# 3. Qual sede mais compra os produtos

with engine.connect() as conn:
    query = f"""

    select
        a.office_location as sede_da_empresa,
        round(sum(sp.close_value)::numeric, 2) as faturamento
    from sales_pipeline sp
    join sales_teams st on st.sales_agent = sp.sales_agent
    join products p on p.product = sp.product
    join accounts a on a.account = sp.account
    where to_char(sp.close_date::date, 'YYYY-MM') = '{mes}'
        and sp.close_date is not null
        and sp.close_date != ''
    group by a.office_location
    order by faturamento desc
    limit 5;

    """

    resultado = conn.execute(text(query))
    df = pd.DataFrame(resultado.fetchall(), columns = resultado.keys())

df.to_csv('03-sede-mais-compra.csv', index=False)

# 4. Top 10 representantes de vendas por faturamento

with engine.connect() as conn:
    query = f"""

    select
        sp.sales_agent as representante_de_vendas,
        round(sum(sp.close_value)::numeric, 2) as faturamento
    from sales_pipeline sp
    join sales_teams st on st.sales_agent = sp.sales_agent
    join products p on p.product = sp.product
    join accounts a on a.account = sp.account
    where to_char(sp.close_date::date, 'YYYY-MM') = '{mes}'
        and sp.close_date is not null
        and sp.close_date != ''
    group by sp.sales_agent
    order by faturamento desc
    limit 10;

    """

    resultado = conn.execute(text(query))
    df = pd.DataFrame(resultado.fetchall(), columns = resultado.keys())

df.to_csv('04-top10-representante-vendas-faturamento.csv', index=False)

# 5. Top 10 gerentes de vendas por faturamento

with engine.connect() as conn:
    query = f"""

    select
        st.manager as gerente_de_vendas,
        round(sum(sp.close_value)::numeric, 2) as faturamento
    from sales_pipeline sp
    join sales_teams st on st.sales_agent = sp.sales_agent
    join products p on p.product = sp.product
    join accounts a on a.account = sp.account
    where to_char(sp.close_date::date, 'YYYY-MM') = '{mes}'
        and sp.close_date is not null
        and sp.close_date != ''
    group by st.manager
    order by faturamento desc
    limit 10;

    """

    resultado = conn.execute(text(query))
    df = pd.DataFrame(resultado.fetchall(), columns = resultado.keys())

df.to_csv('05-top10-gerente-vendas-faturamento.csv', index=False)

# 6. Qual escritório regional tem mais vendas

with engine.connect() as conn:
    query = f"""

    select
        st.regional_office as escritorio_regional,
        round(sum(sp.close_value)::numeric, 2) as faturamento
    from sales_pipeline sp
    join sales_teams st on st.sales_agent = sp.sales_agent
    join products p on p.product = sp.product
    join accounts a on a.account = sp.account
    where to_char(sp.close_date::date, 'YYYY-MM') = '{mes}'
        and sp.close_date is not null
        and sp.close_date != ''
    group by st.regional_office
    order by faturamento desc
    limit 10;

    """

    resultado = conn.execute(text(query))
    df = pd.DataFrame(resultado.fetchall(), columns = resultado.keys())

df.to_csv('06-escritorio-regional-vendas.csv', index=False)

# 7. Top 10 representantes de vendas por quantidade vendida

with engine.connect() as conn:
    query = f"""

    select
        sp.sales_agent AS representante_de_vendas,
        count(sp.opportunity_id) AS quantidade_de_vendas
    from sales_pipeline sp
    join sales_teams st on st.sales_agent = sp.sales_agent
    join products p on p.product = sp.product
    join accounts a on a.account = sp.account
    where to_char(sp.close_date::date, 'YYYY-MM') = '{mes}'
        and sp.deal_stage = 'Won'
        and sp.close_date is not null
        and sp.close_date != ''
    group by sp.sales_agent
    order by quantidade_de_vendas desc
    limit 10;

    """

    resultado = conn.execute(text(query))
    df = pd.DataFrame(resultado.fetchall(), columns = resultado.keys())

df.to_csv('07-top10-representante-vendas-quantidade.csv', index=False)

# 8. Top 10 Representantes de vendas que venderam mais rápido

with engine.connect() as conn:
    query = f"""

    select
        sp.sales_agent as representante_de_vendas,
        round(avg(sp.close_date::date - sp.engage_date::date), 0) as media_de_dias
    from sales_pipeline sp
    join sales_teams st on st.sales_agent = sp.sales_agent
    join products p on p.product = sp.product
    join accounts a on a.account = sp.account
    where to_char(sp.close_date::date, 'YYYY-MM') = '{mes}'
        and sp.deal_stage = 'Won'
        and sp.close_date is not null
        and sp.close_date !=''
        and sp.engage_date is not null
        and sp.engage_date !=''
    group by sp.sales_agent
    order by media_de_dias asc
    limit 10;

    """

    resultado = conn.execute(text(query))
    df = pd.DataFrame(resultado.fetchall(), columns = resultado.keys())

df.to_csv('08-top10-representante-vendas-velocidade.csv', index=False)

# 9. Produto mais vendido

with engine.connect() as conn:
    query = f"""

    select
        p.product as produtos,
        p.sales_price as preco,
        round(sum(sp.close_value)::numeric, 2) as faturamento,
        count(sp.close_value) as quantidade_vendida
    from sales_pipeline sp
    join sales_teams st on st.sales_agent = sp.sales_agent
    join products p on p.product = sp.product
    join accounts a on a.account = sp.account
    where to_char(sp.close_date::date, 'YYYY-MM') = '{mes}'
        and sp.close_date is not null
        and sp.close_date != ''
    group by p.product, p.sales_price
    order by faturamento desc
    limit 10;

    """

    resultado = conn.execute(text(query))
    df = pd.DataFrame(resultado.fetchall(), columns = resultado.keys())

df.to_csv('09-produto-mais-vendido.csv', index=False)
