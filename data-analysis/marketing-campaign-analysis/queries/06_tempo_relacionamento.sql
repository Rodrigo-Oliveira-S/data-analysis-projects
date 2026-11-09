

	with tempo as (

    select
        "ID" as identificacao_cliente,
        (select max("Dt_Customer"::date) from marketing_data) - "Dt_Customer"::date as dias_relacionamento
    from marketing_data
    group by "ID", "Dt_Customer"
    order by dias_relacionamento desc

    )

    select
        count("identificacao_cliente") as qtde_clientes,
        case
            when dias_relacionamento < 365 then 'Menos de 1 ano'
            else 'Mais de 1 ano'
        end as tempo_relacionamento
    from tempo
    group by
        case
            when dias_relacionamento < 365 then 'Menos de 1 ano'
            else 'Mais de 1 ano'
        end;

	