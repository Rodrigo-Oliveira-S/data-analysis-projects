

    -- A empresa teve seu maior faturamento em dezembro de 2014, com US$ 214.665,34
    -- É notável que a empresa está em crescimento, porém é importante destacar que
    -- o faturamento só ficou acima da média a partir de fevereiro de 2014, quase 3 anos
    -- após o início das vendas.
    -- No começo, as variações de um mês para o outro eram grandes, depois de 1 ano estabilizou.

    with faturamento_mensal as (

    select
        to_char(oi.created_at::date, 'YYYY-MM') as data,
        round(sum(o.price_usd)::numeric, 2) as faturamento_mes_atual
    from order_items oi
    join orders o on o.order_id = oi.order_id
    where oi.created_at is not null 
        and o.price_usd is not null
    group by to_char(oi.created_at::date, 'YYYY-MM')
    order by to_char(oi.created_at::date, 'YYYY-MM') asc

    )

    select 
        data,
        lag(faturamento_mes_atual) over (order by data) as faturamento_mes_anterior,
        faturamento_mes_atual,
        round(
            ((faturamento_mes_atual - lag(faturamento_mes_atual) over (order by data)) 
            / lag(faturamento_mes_atual) over (order by data)) * 100, 2
            ) as variacao_percentual,
        round(avg(faturamento_mes_atual) over(), 2) as media_mes,
        case
            when faturamento_mes_atual > round(avg(faturamento_mes_atual) over(), 2) then 'Acima da Média'
            else 'Abaixo da Média'
        end as classificacao
    from faturamento_mensal
    order by data

    