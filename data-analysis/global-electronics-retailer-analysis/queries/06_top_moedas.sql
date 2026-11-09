

    select
        "Currency Code" as moeda_utilizada,
        round(sum(s."Quantity" * p."Unit Price USD")::numeric, 2) as faturamento_bruto
    from "Sales" s
    join "Products" p on p."ProductKey" = s."ProductKey"
    join "Customers" c on c."CustomerKey" = s."CustomerKey"
    where to_char(s."Order Date"::date, 'YYYY-MM') = '2019-12'
    group by "Currency Code"
    order by faturamento_bruto desc
    limit 5;
    