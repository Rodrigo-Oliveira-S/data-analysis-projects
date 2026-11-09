

    -- O escritório da região Oeste é o que mais fatura, vendendo US$ 2.447.825,00
    -- A gerente de vendas que trabalha nesse escritório é a Celia Rouche, que tem a melhor equipe em faturamento.
    -- Summer Sewald sendo o gerente segundo melhor em faturamento também trabalha nesse escritório.
    -- Isso acaba explicando o por que essa região é a que mais vende.

    select
        st.regional_office as escritorio_regional,
        round(sum(sp.close_value)::numeric, 2) as faturamento
    from sales_pipeline sp
    join sales_teams st on st.sales_agent = sp.sales_agent
    join products p on p.product = sp.product
    join accounts a on a.account = sp.account
    group by st.regional_office
    order by faturamento desc
    limit 10;

    