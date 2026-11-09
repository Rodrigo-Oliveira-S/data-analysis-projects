

    -- Kan-code é a empresa que mais adquire produtos, já somados US$ 217.560,00
    -- Eles compraram o produto GTK 500 de US$ 25.791,00 e depois só compraram produtos mais baratos.

    select
        sp.account as empresa,
        round(sum(sp.close_value)::numeric, 2) as faturamento
    from sales_pipeline sp
    join sales_teams st on st.sales_agent = sp.sales_agent
    join products p on p.product = sp.product
    join accounts a on a.account = sp.account
    group by sp.account
    order by faturamento desc
    limit 10;

    