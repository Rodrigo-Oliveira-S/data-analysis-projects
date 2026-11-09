

    -- Estados Unidos liderou com folga em compras de hardwares, gastando US$ 5.519.293,00
    -- Em segundo a Coréia gastando US$ 124.574,00
    -- A diferença de uma pra outra é muito grande, quase 50 vezes mais que os EUA adquire.
    -- EUA investiu muito no produto GTX Plus Pro, que custa US$ 5.482 sendo ele o segundo produto mais caro.

    select
        a.office_location as sede_da_empresa,
        round(sum(sp.close_value)::numeric, 2) as faturamento
    from sales_pipeline sp
    join sales_teams st on st.sales_agent = sp.sales_agent
    join products p on p.product = sp.product
    join accounts a on a.account = sp.account
    group by a.office_location
    order by faturamento desc
    limit 5;

    