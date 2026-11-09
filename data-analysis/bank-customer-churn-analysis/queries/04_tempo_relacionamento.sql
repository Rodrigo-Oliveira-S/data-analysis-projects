

	select 
        	count(*) as qtde_clientes,
        	case
            		when "Tenure" < 1 then 'Até 1 ano'
            		when "Tenure" between 1 and 3 then 'De 1 a 3 anos'
            		else 'Mais de 3 anos'
        	end as tempo_relacionamento,
        	round((count(*) / sum(count(*)) over()) * 100, 2) as porcentagem_do_total
    	from bank_churn
    	where "IsActiveMember" = 1
    	group by
        	case
            		when "Tenure" < 1 then 'Até 1 ano'
            		when "Tenure" between 1 and 3 then 'De 1 a 3 anos'
            		else 'Mais de 3 anos'
        	end
    	order by count(*) desc

	