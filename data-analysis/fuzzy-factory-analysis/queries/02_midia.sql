

    -- 65% dos compradores totais da Fuzzy Factory vem pelo Google search, trazendo US$ 1.276.144,89
    -- em faturamento.

    with midia as (

    select 
        case 
            when utm_source = 'gsearch' then 'Google Ads'
            when utm_source = 'bsearch' then 'Bing Ads'
            when utm_source = 'socialbook' then 'Facebook Ads'
            when utm_source is null then 'Tráfego Direto'
            else utm_source
        end as origem_trafego,       
        round(sum(o.price_usd)::numeric, 2) as faturamento
    from orders o
    join website_sessions ws on ws.website_session_id = o.website_session_id
    group by origem_trafego
    )

    select
        origem_trafego,
        faturamento,
        round((faturamento / sum(faturamento) over()) * 100, 2) as percentual_do_total
    from midia
    order by faturamento desc;

    