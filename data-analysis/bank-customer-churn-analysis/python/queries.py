def volume_total_saldo():
	return """

	select
        	"Geography" as pais_do_cliente,
        	count("IsActiveMember") as clientes_ativos,
        	round(sum("Balance")::numeric, 2) as total_depositos
	from bank_churn
	where "IsActiveMember" = 1
        group by "Geography", "IsActiveMember"
        order by round(sum("Balance")::numeric, 2) desc
        limit 10;

	"""

def clientes_mais_produtos():
	return """

	select
        	count(*) as clientes,
	        "NumOfProducts" as qtde_produtos,
        	round((count(*) / sum(count(*)) over()) * 100, 2) as porcentagem_do_total
	from bank_churn
        where "IsActiveMember" = 1
        group by "NumOfProducts"
        order by "NumOfProducts" desc

	"""

def faixa_etaria_clientes():
	return """

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

	"""

def tempo_relacionamento():
	return """

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

	"""

def categoria_renda():
	return """

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

	"""

def porcentagem_cancelamento():
	return """

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

	"""
