

    -- The Original Mr. Fuzzy lidera também em quantidades, vendendo 24226 produtos.
    -- O segundo lugar, The Forever Love Bear vendeu 5796 quantidades, 
    -- muito abaixo do primeiro lugar.

    select
        p.product_name as produto,
        count(*) as quantidade_vendida
    from products p
    join order_items oi on oi.product_id = p.product_id
    group by p.product_name
    order by quantidade_vendida desc;

    