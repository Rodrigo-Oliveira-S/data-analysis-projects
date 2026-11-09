

    -- The Original Mr. Fuzzy é lider absoluto nas vendas, com US$ 738.893,00 de lucro líquido.
    -- 3x mais que o segundo lugar, o The Forever Love Bear que faturou US$ 217.350,00.

    select
        p.product_name as produto,
        round(sum(oi.price_usd - oi.cogs_usd)::numeric, 2) as lucro_liquido
    from products p
    join order_items oi on oi.product_id = p.product_id
    group by p.product_name
    order by lucro_liquido desc;

    