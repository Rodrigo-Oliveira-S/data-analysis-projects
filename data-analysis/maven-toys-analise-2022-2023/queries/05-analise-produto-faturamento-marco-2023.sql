-- Seguindo o mês de março, na loja Maven Toys Cuidad de México 2.
-- O produto ColorBuds foi o que mais teve um faturamento relevante.
-- O Barrel O' Slime superou as expectativas de quantidades, vendendo quase 2 vezes mais que o segundo lugar.


select 
	p."Product_Name" as produto,
	sum(s."Units") as quantidade,
	round(sum(s."Units" * replace(p."Product_Price", '$', ' ')::numeric)::numeric, 2) as faturamento_bruto,
	round(sum(s."Units" * (replace(p."Product_Price", '$', ' ')::numeric - replace(p."Product_Cost", '$', ' ')::numeric))::numeric, 2) as faturamento_Liquido
from sales s 
join stores s1 on s1."Store_ID" = s."Store_ID"
join products p on p."Product_ID" = s."Product_ID"
where s."Date"::date between '2023-03-01' 
	and '2023-03-31'
	and s1."Store_City" = 'Cuidad de Mexico'
group by produto
order by faturamento_liquido desc;