

	select
        	count(*) as clientes,
	        "NumOfProducts" as qtde_produtos,
        	round((count(*) / sum(count(*)) over()) * 100, 2) as porcentagem_do_total
	from bank_churn
        where "IsActiveMember" = 1
        group by "NumOfProducts"
        order by "NumOfProducts" desc

	