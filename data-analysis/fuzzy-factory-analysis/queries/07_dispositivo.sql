

    -- As vendas do The Original Mr. Fuzzy lideram através do Desktop, 
    -- faturando US$ 638.822,50 e com 20945 em quantidades vendidas.
    -- Já pelo Mobile o mesmo produto também é o mais vendido, porém pelo
    -- faturamento de US$ 100.070,50.

    select *
    from (

    select
        ws.device_type as dispositivo,
        p.product_name as produto,
        count(*) as quantidade_vendida,
        round(sum(oi.price_usd - oi.cogs_usd)::numeric, 2) as lucro_liquido,
        rank() over (partition by ws.device_type order by round(sum(oi.price_usd - oi.cogs_usd)::numeric, 2) desc) as ranking
    from orders o
    join website_sessions ws on ws.website_session_id = o.website_session_id
    join order_items oi on oi.order_id = o.order_id
    join products p on p.product_id = oi.product_id
    group by p.product_name, ws.device_type
    limit 60

    )

    where ranking <= 3

    