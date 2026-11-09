# Análise de Vendas - Fuzzy Factory (2012-2015)

mes = '2014-07'

# Importação dos dados

import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(
    f'postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}'
    f'@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/db_fuzzy_factory'
)

# 1. Qual o faturamento da empresa

with engine.connect() as conn:
    query = f"""

    with faturamento_mensal as (

        select
            to_char(oi.created_at::date, 'YYYY-MM') as data,
            round(sum(o.price_usd)::numeric, 2) as faturamento_mes_atual
        from order_items oi
        join orders o on o.order_id = oi.order_id
        where oi.created_at is not null
            and o.price_usd is not null
        group by to_char(oi.created_at::date, 'YYYY-MM')

    ),

    com_media as (
        select
            data,
            faturamento_mes_atual,
            lag(faturamento_mes_atual) over (order by data) as faturamento_mes_anterior,
            round(avg(faturamento_mes_atual) over(), 2) as media_geral
        from faturamento_mensal
    )

        select
            data,
            faturamento_mes_anterior,
            faturamento_mes_atual,
            round(
                ((faturamento_mes_atual - faturamento_mes_anterior)
                / faturamento_mes_anterior) * 100, 2
                ) AS variacao_percentual,
                media_geral as media_mes,
            case
                when faturamento_mes_atual > media_geral then 'Acima da Média'
                else 'Abaixo da Média'
            end as classificacao
        from com_media
        where data = '{mes}'
        order by data

    """
    resultado = conn.execute(text(query))
    df = pd.DataFrame(resultado.fetchall(), columns = resultado.keys())

df.to_csv('01_faturamento_total.csv', index=False)

# 2. Através de qual mídia os produtos mais vendem

with engine.connect() as conn:
    query = f"""

    with midia as (

    select
        to_char(oi.created_at::date, 'YYYY-MM') as data,
        case
            when utm_source = 'gsearch' then 'Google Ads'
            when utm_source = 'bsearch' then 'Bing Ads'
            when utm_source = 'socialbook' then 'Facebook Ads'
            when utm_source is null then 'Tráfego Direto'
            else utm_source
        end as origem_trafego,
        round(sum(o.price_usd)::numeric, 2) as faturamento
    from orders o
    join website_sessions ws on ws.website_session_id = o.website_session_id
    join order_items oi on oi.order_id = o.order_id
    join products p on p.product_id = oi.product_id
    group by origem_trafego, data
    )

    select
        origem_trafego,
        faturamento,
        round((faturamento / sum(faturamento) over()) * 100, 2) as percentual_do_total
    from midia
    where data = '{mes}'
    order by faturamento desc;

    """
    resultado = conn.execute(text(query))
    df = pd.DataFrame(resultado.fetchall(), columns = resultado.keys())

df.to_csv('02_midia.csv', index=False)

# 3. Qual produto traz lucro líquido para a empresa

with engine.connect() as conn:
    query = f"""

    select
        to_char(oi.created_at::date, 'YYYY-MM') as data,
        p.product_name as produto,
        round(sum(oi.price_usd - oi.cogs_usd)::numeric, 2) as lucro_liquido
    from orders o
    join website_sessions ws on ws.website_session_id = o.website_session_id
    join order_items oi on oi.order_id = o.order_id
    join products p on p.product_id = oi.product_id
    where to_char(oi.created_at::date, 'YYYY-MM') = '{mes}'
    group by p.product_name, to_char(oi.created_at::date, 'YYYY-MM')
    order by lucro_liquido desc;
    """
    resultado = conn.execute(text(query))
    df = pd.DataFrame(resultado.fetchall(), columns = resultado.keys())

df.to_csv('03_produto_lucro.csv', index=False)

# 4. Qual produto tem mais vendas em quantidade

with engine.connect() as conn:
    query = f"""

    select
        to_char(oi.created_at::date, 'YYYY-MM') as data,
        p.product_name as produto,
        count(*) as quantidade_vendida
    from orders o
    join website_sessions ws on ws.website_session_id = o.website_session_id
    join order_items oi on oi.order_id = o.order_id
    join products p on p.product_id = oi.product_id
    where to_char(oi.created_at::date, 'YYYY-MM') = '{mes}'
    group by p.product_name, to_char(oi.created_at::date, 'YYYY-MM')
    order by quantidade_vendida desc;

    """
    resultado = conn.execute(text(query))
    df = pd.DataFrame(resultado.fetchall(), columns = resultado.keys())

df.to_csv('04_venda_quantidade.csv', index=False)

# 5. O produto que mais traz lucro líquido, é mais vendido através de qual campanha

with engine.connect() as conn:
    query = f"""

    select
        to_char(oi.created_at::date, 'YYYY-MM') as data,
        p.product_name as produto,
        case
            when utm_campaign = 'nonbrand' then 'Campanha Genérica'
            when utm_campaign = 'brand' then 'Marca'
            when utm_campaign is null then 'Sem Campanha'
            when utm_campaign = 'desktop_targeted' then 'Segmentada Desktop'
            when utm_campaign = 'pilot' then 'Piloto'
            else utm_campaign
        end as campanha,
        count(*) as quantidade_vendida,
        round(sum(oi.price_usd - oi.cogs_usd)::numeric, 2) as lucro_liquido
    from orders o
    join website_sessions ws on ws.website_session_id = o.website_session_id
    join order_items oi on oi.order_id = o.order_id
    join products p on p.product_id = oi.product_id
    where p.product_name = 'The Original Mr. Fuzzy'
        and to_char(oi.created_at::date, 'YYYY-MM') = '{mes}'
    group by p.product_name, ws.utm_campaign, to_char(oi.created_at::date, 'YYYY-MM')
    order by quantidade_vendida desc;

    """
    resultado = conn.execute(text(query))
    df = pd.DataFrame(resultado.fetchall(), columns = resultado.keys())

df.to_csv('05_produto_campanha.csv', index=False)

# 6. Qual produto teve mais reembolso

with engine.connect() as conn:
    query = f"""

    select
        to_char(oi.created_at::date, 'YYYY-MM') as data,
        p.product_name as produto,
        round(sum(oir.refund_amount_usd)::numeric, 2) as total_reembolso
    from order_item_refunds oir
    join order_items oi on oi.order_id = oir.order_id
    join products p on p.product_id = oi.product_id
    where to_char(oi.created_at::date, 'YYYY-MM') = '{mes}'
    group by p.product_name, to_char(oi.created_at::date, 'YYYY-MM')
    order by total_reembolso desc
    limit 10;

    """
    resultado = conn.execute(text(query))
    df = pd.DataFrame(resultado.fetchall(), columns = resultado.keys())

df.to_csv('06_produto_reembolso.csv', index=False)

# 7. Através de qual dispositivo existe mais vendas (mobile/desktop)

with engine.connect() as conn:
    query = f"""

    select *
    from (

    select
        to_char(oi.created_at::date, 'YYYY-MM') as data,
        ws.device_type as dispositivo,
        p.product_name as produto,
        count(*) as quantidade_vendida,
        round(sum(oi.price_usd - oi.cogs_usd)::numeric, 2) as lucro_liquido,
        rank() over (partition by ws.device_type order by round(sum(oi.price_usd - oi.cogs_usd)::numeric, 2) desc) as ranking
    from orders o
    join website_sessions ws on ws.website_session_id = o.website_session_id
    join order_items oi on oi.order_id = o.order_id
    join products p on p.product_id = oi.product_id
    where to_char(oi.created_at::date, 'YYYY-MM') = '{mes}'
    group by p.product_name, ws.device_type, to_char(oi.created_at::date, 'YYYY-MM')
    limit 60

    )

    where ranking <= 3

    """
    resultado = conn.execute(text(query))
    df = pd.DataFrame(resultado.fetchall(), columns = resultado.keys())

df.to_csv('07_dispositivo.csv', index=False)
