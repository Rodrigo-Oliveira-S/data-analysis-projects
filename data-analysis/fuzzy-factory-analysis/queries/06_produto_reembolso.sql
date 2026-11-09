

    -- Por ser o produto mais vendido, The Original Mr. Fuzzy também é o produto que mais teve reembolso
    -- US$ 69.361,92 foi reembolsado.

    select 
        p.product_name as produto,
        round(sum(oir.refund_amount_usd)::numeric, 2) as total_reembolso
    from order_item_refunds oir
    join order_items oi on oi.order_id = oir.order_id
    join products p on p.product_id = oi.product_id
    group by p.product_name
    order by total_reembolso desc
    limit 10;

    