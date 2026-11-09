-- O produto Colorbuds, que liderou as vendas em Março de 2023 na Ciudad de Mexico,
-- apresentou desempenho superior em outros meses.
-- Teve picos expressivos em Abril e Maio de 2022, com faturamento quase o dobro.
-- Em Março de 2023, apesar de ser o segundo melhor mês da loja de brinquedos,
-- foi um dos piores meses para o Colorbuds.
-- Ou seja, o produto vende o ano inteiro, mas está em declínio constante.


select 
	to_char(s."Date"::date, 'YYYY-MM') as data_venda,
	p."Product_Name" as produto,	
	round(sum(s."Units" * replace(p."Product_Price", '$', ' ')::numeric)::numeric, 2) as faturamento_bruto,
	round(sum(s."Units" * (replace(p."Product_Price", '$', ' ')::numeric - replace(p."Product_Cost", '$', ' ')::numeric))::numeric, 2) as faturamento_Liquido
from sales s 
join stores s1 on s1."Store_ID" = s."Store_ID"
join products p on p."Product_ID" = s."Product_ID"
where p."Product_Name" = 'Colorbuds'
	and s1."Store_City" = 'Cuidad de Mexico'
group by data_venda, produto
having round(sum(s."Units" * replace(p."Product_Price", '$', ' ')::numeric)::numeric, 2) >= 7420.05
order by faturamento_liquido desc;