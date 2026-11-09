

    -- A campanha que o The Original Mr. Fuzzy foi mais vendido é chamada de Campanha Genérica,
    -- Com 17192 quantidades vendidas, e trazendo US$ 524.356,00 de lucro líquido.
    -- Isso significa que a empresa está conquistando clientes que não conheciam a marca.

    select
        p.product_name as produto,
        case 
            when utm_campaign = 'nonbrand' then 'Campanha Genérica'
            when utm_campaign = 'brand' then 'Marca'
            when utm_campaign is null then 'Sem Campanha'
            when utm_campaign = 'desktop_targeted' then 'Segmentada Desktop'
            when utm_campaign = 'pilot' then 'Piloto'
            else utm_campaign
        end as campanha,
        count(*) as quantidade_vendida,
        round(sum(oi.price_usd - oi.cogs_usd)::numeric, 2) as lucro_liquido        
    from orders o
    join website_sessions ws on ws.website_session_id = o.website_session_id
    join order_items oi on oi.order_id = o.order_id
    join products p on p.product_id = oi.product_id
    where p.product_name = 'The Original Mr. Fuzzy'
    group by p.product_name, ws.utm_campaign
    order by quantidade_vendida desc;

    