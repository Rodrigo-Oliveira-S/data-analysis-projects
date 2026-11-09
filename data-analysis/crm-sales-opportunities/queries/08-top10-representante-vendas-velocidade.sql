

    -- A representante de vendas que vende mais rápido é a Rosie Papadopoulos, com uma média de 41 dias pra fechar negócio.
    -- Ela não aparece nem no top 10 quantidades vendidas, nem no top 10 faturamento.
    -- Em segundo lugar aparece a Cecily Lampkin, com uma média de 42 dias para fechar negócio.
    -- Já em terceiro lugar, com uma média de 44 dias, temos o Elease Gluck, e ele sim aparece em 7° lugar no top 10 faturamento.
    -- Isso mostra que ele, aparentemente trás bons faturamentos e também vende rápido.
    -- Marty Freudenburg que aqui ficou em 6° demorando uma média de 48 dias pra vender, no ranking de faturamento está em 9° lugar, e
    -- também merece uma atenção, pois também trás boas vendas e mais rápido.

    select
        sp.sales_agent as representante_de_vendas,
        round(avg(sp.close_date::date - sp.engage_date::date), 0) as media_de_dias
    from sales_pipeline sp
    join sales_teams st on st.sales_agent = sp.sales_agent
    join products p on p.product = sp.product
    join accounts a on a.account = sp.account
    where sp.deal_stage = 'Won'
        and sp.close_date is not null
        and sp.close_date !=''
        and sp.engage_date is not null
        and sp.engage_date !=''
    group by sp.sales_agent
    order by media_de_dias asc
    limit 10;

    