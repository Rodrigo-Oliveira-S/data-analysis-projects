

	select 
        	count(*) as qtde_clientes,
        	case
            		when "Age" between 18 and 23 then 'Jovens'
            		when "Age" between 24 and 65 then 'Adultos'
            		else 'Idosos'
        	end as faixa_etaria,
        	round((count(*) / sum(count(*)) over()) * 100, 2) as porcentagem_do_total
    	from bank_churn
    	where "IsActiveMember" = 1
    	group by 
        	case
            		when "Age" between 18 and 23 then 'Jovens'
            		when "Age" between 24 and 65 then 'Adultos'
            		else 'Idosos'
        	end
    	order by count(*) desc

	