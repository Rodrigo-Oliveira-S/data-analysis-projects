

    -- Junho de 2017 foi o melhor mês, com US$ 884.971,00 em vendas.
    -- Março de 2017 ficou em segundo lugar com US$ 757.706,00 em vendas.
    -- Dezembro que é um mês de presentes, teve menos pedidos que Julho e Março.

    select 
        to_char(sp.close_date::date, 'YYYY-MM') as data_fechamento,
        round(sum(sp.close_value)::numeric, 2) as faturamento
    from sales_pipeline sp
    join sales_teams st on st.sales_agent = sp.sales_agent
    join products p on p.product = sp.product
    join accounts a on a.account = sp.account
    where sp.close_date is not null
        and sp.close_date != ''
    group by to_char(sp.close_date::date, 'YYYY-MM')
    order by to_char(sp.close_date::date, 'YYYY-MM');

    