

	select 
        	count(*) as qtde_clientes,
        	case
            		when "Exited" = 0 then 'Não'
            		else 'Sim'
        	end as conta_cancelada,
        	round((count(*) / sum(count(*)) over()) * 100, 2) as porcentagem_do_total
    	from bank_churn
    	group by "Exited"
    	order by count(*) desc

	