-- Aqui eu quero ver dentro da categoria Classic, que é a categoria mais vendida, qual pizza vende mais.
-- E nesse ponto dá pra perceber que a The Classic Deluxe Pizza está ganhando com uma vantagem na frente.
-- Pode ser a pizza padrão da categoria Classic.

select 
	pt.name as sabores,
	sum(od.quantity) as quantidade_vendida,
	round(sum(od.quantity * p.price)::numeric, 2) as faturamento 
from order_details od 
join orders o on o.order_id = od.order_id 
join pizzas p on p.pizza_id = od.pizza_id 
join pizza_types pt on pt.pizza_type_id = p.pizza_type_id
where o.date >= '2015-07-01'
	and o.date <= '2015-07-31'
	and pt.category = 'Classic'
group by pt.name
order by faturamento desc;

