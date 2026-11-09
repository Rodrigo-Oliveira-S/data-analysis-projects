

    -- Celia Rouche é a gerente que mais vende, trazendo US$ 1.259.786,00 de faturamento.
    -- A melhor representante de vendas desse time é a Vicki Laflamme, que faturou US$ 289.370,00
    -- Mesmo sendo a gerente com o melhor time de vendedores, os vendedores que mais faturam não são do grupo dela.
    -- O representante de vendas James Ascencio, que é o segundo melhor vendedor geral, trabalha na equipe do Summer Sewald,
    -- que é o segundo melhor gerente de de vendas.
    -- O terceiro melhor gerente de vendas, o Melvin Marxen, tem no seu time o Darcel Schlecht, que é o representante,
    -- de vendas que mais gera lucro total dos representantes de vendas em geral.

    select
        st.manager as gerente_de_vendas,
        round(sum(sp.close_value)::numeric, 2) as faturamento
    from sales_pipeline sp
    join sales_teams st on st.sales_agent = sp.sales_agent
    join products p on p.product = sp.product
    join accounts a on a.account = sp.account
    group by st.manager
    order by faturamento desc
    limit 10;

    