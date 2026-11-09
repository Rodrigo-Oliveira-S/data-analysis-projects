

    select
        "Country" as compras_pais,
        round(sum(s."Quantity" * (p."Unit Price USD" - p."Unit Cost USD"))::numeric, 2) as faturamento_liquido
    from "Sales" s
    join "Products" p on p."ProductKey" = s."ProductKey"
    join "Customers" c on c."CustomerKey" = s."CustomerKey"
    where to_char(s."Order Date"::date, 'YYYY-MM') = '2019-12'
    group by "Country"
    order by faturamento_liquido desc
    limit 5;
    