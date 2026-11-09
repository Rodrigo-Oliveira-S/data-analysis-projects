-- O Faturamento bruto e líquido em cada ano.
-- Um ponto interessante é que mesmo com 9 meses de venda, 2023 quase empata com 2022 em faturamento, sendo 2022 de janeiro a dezembro.
-- Ou seja, provável que com os meses de outubro, novembro e dezembro 2023 passaria o faturamento.


select 
	to_char(s."Date"::date, 'YYYY') as data_venda,
	sum(s."Units") as quantidade,
	round(sum(s."Units" * replace(p."Product_Price", '$', ' ')::numeric)::numeric, 2) as faturamento_bruto,
	round(sum(s."Units" * (replace(p."Product_Price", '$', ' ')::numeric - replace(p."Product_Cost", '$', ' ')::numeric))::numeric, 2) as faturamento_Liquido
from sales s 
join stores s1 on s1."Store_ID" = s."Store_ID"
join products p on p."Product_ID" = s."Product_ID"
group by data_venda
order by data_venda desc;