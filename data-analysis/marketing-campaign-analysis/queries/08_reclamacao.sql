

	select
        count("ID") as qtde_clientes,
        case
            when "Complain" = 1 then 'Reclamaram'
            else 'Não reclamaram'
        end as reclamacao,
        round(count(*) / sum(count(*)) over() * 100, 2) as porcentagem_total
    from marketing_data
    group by "Complain"
    order by count("ID") desc;

	