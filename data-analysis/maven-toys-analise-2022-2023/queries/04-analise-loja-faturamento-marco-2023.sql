-- Maven Toys Cuidad de Mèxico 2 foi a loja que mais vendeu no mês.


select 
	s1."Store_Name" as loja,
	sum(s."Units") as quantidade,
	round(sum(s."Units" * replace(p."Product_Price", '$', ' ')::numeric)::numeric, 2) as faturamento_bruto,
	round(sum(s."Units" * (replace(p."Product_Price", '$', ' ')::numeric - replace(p."Product_Cost", '$', ' ')::numeric))::numeric, 2) as faturamento_Liquido
from sales s 
join stores s1 on s1."Store_ID" = s."Store_ID"
join products p on p."Product_ID" = s."Product_ID"
where s."Date"::date between '2023-03-01' 
	and '2023-03-31'
	and s1."Store_City" = 'Cuidad de Mexico'
group by loja
order by faturamento_liquido desc;
