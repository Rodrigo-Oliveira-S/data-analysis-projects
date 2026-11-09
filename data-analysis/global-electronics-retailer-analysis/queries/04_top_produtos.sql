

    select
        p."Product Name" as produtos,
        round(sum(s."Quantity" * (p."Unit Price USD" - p."Unit Cost USD"))::numeric, 2) as faturamento_liquido
    from "Sales" s
    join "Products" p on p."ProductKey" = s."ProductKey"
    where to_char(s."Order Date"::date, 'YYYY-MM') = '2019-12'
    group by p."Product Name"
    order by faturamento_liquido desc
    limit 5;
    