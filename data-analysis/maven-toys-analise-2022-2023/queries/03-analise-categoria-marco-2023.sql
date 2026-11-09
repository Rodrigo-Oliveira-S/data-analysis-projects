-- A categoria Toys foi a que mais trouxe rentabilidade para a loja no mês que a loja mais vendeu.
-- Porém a categoria Art & Crafts foi a que mais vendeu em quantidade nesse período.
-- O faturamento bruto tem uma diferença entre eles de US$ 97.351,70 já o faturamento líquido a diferença é de US$ 3.914.
-- Uma diferença bem próxima de faturamento líquido.
-- A categoria Arte & Crafts deve ter uma margem de lucro mais alta, para alcançar esse valor.


select 
	p."Product_Category" as categoria,
	sum(s."Units") as quantidade,
	round(sum(s."Units" * replace(p."Product_Price", '$', ' ')::numeric)::numeric, 2) as faturamento_bruto,
	round(sum(s."Units" * (replace(p."Product_Price", '$', ' ')::numeric - replace(p."Product_Cost", '$', ' ')::numeric))::numeric, 2) as faturamento_Liquido
from sales s 
join stores s1 on s1."Store_ID" = s."Store_ID"
join products p on p."Product_ID" = s."Product_ID"
where s."Date"::date between '2023-03-01' 
	and '2023-03-31'
group by categoria
order by faturamento_liquido desc;
