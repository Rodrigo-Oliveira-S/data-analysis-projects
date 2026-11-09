

	select
        count("ID") as qtde_clientes,
        case
            when extract(year from "Dt_Customer"::date) - "Year_Birth" between 18 and 23 then 'Jovens'
            when extract(year from "Dt_Customer"::date) - "Year_Birth" between 24 and 65 then 'Adultos'
            else 'Idosos'
        end as faixa_etaria,
        round(count(*) / sum(count(*)) over() * 100, 2) as porcentagem_total
    from marketing_data
    group by
        case
            when extract(year from "Dt_Customer"::date) - "Year_Birth" between 18 and 23 then 'Jovens'
            when extract(year from "Dt_Customer"::date) - "Year_Birth" between 24 and 65 then 'Adultos'
            else 'Idosos'
        end
    order by qtde_clientes desc;

	