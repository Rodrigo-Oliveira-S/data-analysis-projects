-- Aqui temos por dia, cada quantidade vendida e qual o faturamento por mês.
-- Esse é o mês de Julho, o mês que mais teve vendas no ano.

select 
	o.date as Data_venda,
	sum(od.quantity) as Quantidade,
	round(sum(od.quantity * p.price)::numeric, 2) as Faturamento
from order_details od 
join orders o on o.order_id = od.order_id 
join pizzas p on p.pizza_id = od.pizza_id 
join pizza_types pt on pt.pizza_type_id = p.pizza_type_id
where o.date >= '2015-07-01'
	and o.date <= '2015-07-31'
group by o.date
order by Data_venda;
