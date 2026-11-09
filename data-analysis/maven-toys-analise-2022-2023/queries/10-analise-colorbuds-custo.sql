-- Analisando o faturamento dos brinquedos que mais vendem, conseguimos ver que o Colorbuds trás mais rentabilidade,
-- para a empresa, com um volume quase 3x maior que o segundo lugar.
-- Já o Lego Bricks provavelmente tem muita fama, pois mesmo caro vende bastante, trás muitos números,
-- mas gera pouco lucro líquido.
-- Sendo assim, o brinquedo mais lucrativo (Colorbuds) não é nem o mais caro nem o mais barato.
-- Seu preço está na média, mas sua margem de lucro (53%) é o que faz a diferença.


select 
	p."Product_Name" as produto,
	replace(p."Product_Price", '$', ' ') as preco_final,
	replace(p."Product_Cost", '$', ' ') as preco_custo,
	round(sum(s."Units" * replace(p."Product_Price", '$', ' ')::numeric)::numeric, 2) as faturamento_bruto,
	round(sum(s."Units" * (replace(p."Product_Price", '$', ' ')::numeric - replace(p."Product_Cost", '$', ' ')::numeric))::numeric, 2) as faturamento_liquido
from sales s 
join products p on s."Product_ID" = p."Product_ID"
join stores s1 on s1."Store_ID" = s."Store_ID"
group by preco_final, preco_custo, produto 
order by faturamento_bruto desc;