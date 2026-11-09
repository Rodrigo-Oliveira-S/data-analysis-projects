

	select
        "Country" as localidade_cliente,
        round((
            sum("MntWines"::numeric + "MntFruits"::numeric 
            + "MntMeatProducts"::numeric + "MntFishProducts"::numeric 
            + "MntSweetProducts"::numeric + "MntGoldProds")::numeric
            ), 2) as gasto_total
    from marketing_data
    where to_char("Dt_Customer"::date, 'YYYY-MM') = '2012-08'
    group by "Country"
    order by gasto_total desc;

	