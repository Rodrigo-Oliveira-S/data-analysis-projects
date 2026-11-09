

    with 
        faturamento_geral as (      
    select
        to_char(s."Order Date"::date, 'YYYY-MM') as data,
        round(sum(s."Quantity" * p."Unit Price USD")::numeric, 2) as faturamento_bruto,
        round(sum(s."Quantity" * p."Unit Cost USD")::numeric, 2) as custo_total,
        round(sum(s."Quantity" * (p."Unit Price USD" - p."Unit Cost USD"))::numeric, 2) as faturamento_liquido
    from 
        "Sales" s
    join 
        "Products" p on p."ProductKey" = s."ProductKey"
    group by
        to_char(s."Order Date"::date, 'YYYY-MM')
    )
    select
        data,
        faturamento_bruto,
        custo_total,
        faturamento_liquido,
        round(avg(faturamento_liquido) over(), 2) as media_mes
    from
        faturamento_geral
    order by 
        faturamento_bruto desc;

	