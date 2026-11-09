

    -- Darcel Schlecht é o representante de vendas que mais trás lucro, com US$ 380.085,00 em vendas.
    -- O produto que ele mais vendeu foi o GTX Plus Pro de US$ 5.482. 
    -- Somando apenas com esse produto US$ 176.844,00 em vendas.
    -- US$ 310.473,00 em vendas para os EUA.
    -- Em segundo lugar o James Ascencio, vendendo US$ 315.852,00 e o produto que ele mais vendeu foi o GTX Plus Pro,
    -- trazendo US$ 241.420,00 em faturamento, vendendo até melhor esse produto do que o Darcel Schlecht.
    -- James Ascencio vendeu US$ 283.294,00 para os EUA, ou seja, os 2 melhores vendedores, vendem para a sede que mais compra.

    select
        sp.sales_agent as representante_de_vendas,
        round(sum(sp.close_value)::numeric, 2) as faturamento
    from sales_pipeline sp
    join sales_teams st on st.sales_agent = sp.sales_agent
    join products p on p.product = sp.product
    join accounts a on a.account = sp.account
    group by sp.sales_agent
    order by faturamento desc
    limit 10;

    