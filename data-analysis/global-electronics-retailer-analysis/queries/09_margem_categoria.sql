

    select
        p."Category" as categoria,
        round(
            (
                (
                    sum(s."Quantity" * (p."Unit Price USD" - p."Unit Cost USD"))
                    /
                    sum(s."Quantity" * p."Unit Price USD")
                )::numeric * 100
            ), 2
        ) as margem
    from "Sales" s
    join "Products" p on p."ProductKey" = s."ProductKey"
    where to_char(s."Order Date"::date, 'YYYY-MM') = '2019-12'
    group by categoria
    order by margem desc;
    