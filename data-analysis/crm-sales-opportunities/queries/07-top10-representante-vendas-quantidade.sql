

    -- Anna Snelling é a representante que mais vendeu em quantidade totalizando 208 vendas.
    -- Em faturamento geral ela ficou em 4° lugar, com de US$ 275.056,00.
    -- Ficando em segundo lugar o Darcel Schlecht, que no top 10 faturamento ficou em 1° lugar.
    -- Uma coisa fica mais nítido, Anna Snelling vende mais vezes, porém produtos mais baratos, já
    -- o Darcel Schlecht vende menos vezes, porém produtos mais caros.

    select
        sp.sales_agent AS representante_de_vendas,
        count(sp.opportunity_id) AS quantidade_de_vendas
    from sales_pipeline sp
    join sales_teams st on st.sales_agent = sp.sales_agent
    join products p on p.product = sp.product
    join accounts a on a.account = sp.account
    where sp.deal_stage = 'Won'
    group by sp.sales_agent
    order by quantidade_de_vendas desc
    limit 10;

    