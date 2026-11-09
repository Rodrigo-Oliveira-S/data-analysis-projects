-- Neste cenário temos as top 10 mais vendidas por faturamento
-- As pizzas por sabor que mais trouxe lucro para a pizzaria.

select 
	pt.name as Sabores,
	round(sum(od.quantity * p.price)::numeric, 2) as Faturamento
from order_details od 
join orders o on o.order_id = od.order_id 
join pizzas p on p.pizza_id = od.pizza_id 
join pizza_types pt on pt.pizza_type_id = p.pizza_type_id
where o.date >= '2015-07-01'
	and o.date <= '2015-07-31'
group by pt.name 
order by Faturamento desc
limit 10;