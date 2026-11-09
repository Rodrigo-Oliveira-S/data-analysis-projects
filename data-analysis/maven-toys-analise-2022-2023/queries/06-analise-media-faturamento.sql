-- Média bruta de cada mês foi de US$ 687.836,78
-- Já a média liquida de cada mês foi de US$ 191.144,24


select 
	round(avg(faturamento_bruto), 2) as media_bruto,
	round(avg(faturamento_liquido), 2) as media_liquido
from (

select 
	to_char(s."Date"::date, 'YYYY-MM') as data_venda,
	round(sum(s."Units" * replace(p."Product_Price", '$', ' ')::numeric)::numeric, 2) as faturamento_bruto,
	round(sum(s."Units" * (replace(p."Product_Price", '$', ' ')::numeric - replace(p."Product_Cost", '$', ' ')::numeric))::numeric, 2) as faturamento_Liquido
from sales s 
join stores s1 on s1."Store_ID" = s."Store_ID"
join products p on p."Product_ID" = s."Product_ID"
group by to_char(s."Date"::date, 'YYYY-MM')

) sub;