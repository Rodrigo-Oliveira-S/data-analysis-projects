

	select
        	"Geography" as pais_do_cliente,
        	count("IsActiveMember") as clientes_ativos,
        	round(sum("Balance")::numeric, 2) as total_depositos
	from bank_churn
	where "IsActiveMember" = 1
        group by "Geography", "IsActiveMember"
        order by round(sum("Balance")::numeric, 2) desc
        limit 10;

	