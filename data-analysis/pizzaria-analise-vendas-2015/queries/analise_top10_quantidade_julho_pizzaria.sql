select 
	pt.name as Sabores,
	sum(od.quantity) as quantidade_vendida 
from order_details od 
join orders o on o.order_id = od.order_id 
join pizzas p on p.pizza_id = od.pizza_id 
join pizza_types pt on pt.pizza_type_id = p.pizza_type_id
where o.date >= '2015-07-01'
	and o.date <= '2015-07-31'
group by pt.name 
order by quantidade_vendida desc
limit 10;