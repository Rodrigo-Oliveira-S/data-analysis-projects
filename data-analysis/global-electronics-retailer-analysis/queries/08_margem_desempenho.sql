

    select
        to_char(s."Order Date"::date, 'YYYY-MM') as data,
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
    group by data
    order by data asc;
    
