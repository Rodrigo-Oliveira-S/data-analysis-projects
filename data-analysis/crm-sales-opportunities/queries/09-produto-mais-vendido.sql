

    -- O produto GTX Plus Pro é o que mais trouxe faturamento (US$ 2.629.651,00) pois é o segundo produto mais caro (US$ 5.482), porém
    -- o GTX Basic foi o que mais vendeu em quantidade, com 1436 produtos vendidos, e talvez seja pelo seu preço ser o penúltimo mais barato,
    -- custando US$ 550, e por isso na ordem de faturamento ficou em 4° lugar, com US$ 499.263,00 em vendas.

    select 
        p.product as produtos,
        p.sales_price as preco,
        round(sum(sp.close_value)::numeric, 2) as faturamento,
        count(sp.close_value) as quantidade_vendida
    from sales_pipeline sp
    join sales_teams st on st.sales_agent = sp.sales_agent
    join products p on p.product = sp.product
    join accounts a on a.account = sp.account
    group by p.product, p.sales_price
    order by faturamento desc
    limit 10;

    