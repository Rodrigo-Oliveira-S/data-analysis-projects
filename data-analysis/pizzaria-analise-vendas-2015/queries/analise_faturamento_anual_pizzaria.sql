-- Análise mês a mês da pizzaria.
-- Mês de Julho foi o que mais vendeu,
-- já o mês de Outubro foi o que menos teve venda.

select 
	to_char(o.date::date, 'YYYY-MM') as Mês,
	sum(od.quantity) as Quantidade,
	round(sum(od.quantity * p.price)::numeric, 2) as Faturamento
from order_details od 
join orders o on o.order_id = od.order_id 
join pizzas p on p.pizza_id = od.pizza_id 
join pizza_types pt on pt.pizza_type_id = p.pizza_type_id 
group by to_char(o.date::date, 'YYYY-MM')
order by Faturamento desc;

