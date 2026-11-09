

	select 
        	count(*) as qtde_clientes,
        	case
            		when "EstimatedSalary" < 50000 then 'Baixa Renda'
            		when "EstimatedSalary" between 50000 and 100000 then 'Média Renda'
            		when "EstimatedSalary" between 100000 and 150000 then 'Alta Renda'
            		else 'Elite'
        	end as categoria_renda,
        	round((count(*) / sum(count(*)) over()) * 100, 2) as porcentagem_do_total
    	from bank_churn
    	where "IsActiveMember" = 1
    	group by
        	case
            		when "EstimatedSalary" < 50000 then 'Baixa Renda'
            		when "EstimatedSalary" between 50000 and 100000 then 'Média Renda'
            		when "EstimatedSalary" between 100000 and 150000 then 'Alta Renda'
            		else 'Elite'
        	end
    	order by count(*) desc

	