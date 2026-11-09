-- Aqui eu analiso mês a mês o faturamento desse período da loja de brinquedos.
-- Verificando o faturamento em ordem decrescente, o melhor mês foi  dezembro de 2022
-- O segundo melhor mês foi março de 2023.
-- Tanto pelo Faturamento liquido quanto bruto, dezembro e março lideram.
-- Dezembro é mais normal ter vendas maiores, já março nem tanto, pois não tem data comemorativa.


select 
	to_char(s."Date"::date, 'YYYY-MM') as data_venda,
	sum(s."Units") as quantidade,
	round(sum(s."Units" * replace(p."Product_Price", '$', ' ')::numeric)::numeric, 2) as faturamento_bruto,
	round(sum(s."Units" * (replace(p."Product_Price", '$', ' ')::numeric - replace(p."Product_Cost", '$', ' ')::numeric))::numeric, 2) as faturamento_Liquido
from sales s 
join stores s1 on s1."Store_ID" = s."Store_ID"
join products p on p."Product_ID" = s."Product_ID"
group by data_venda
order by faturamento_liquido desc;
