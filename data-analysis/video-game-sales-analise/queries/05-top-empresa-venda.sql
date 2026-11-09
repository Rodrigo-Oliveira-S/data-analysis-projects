-- Empresa que mais vendeu: Activision (722.77 milhões de cópias)
-- A Rockstar Games, apesar de ter os jogos mais vendidos individualmente,
-- ficou em 7º lugar porque tem apenas 70 títulos — contra 685 da Activision.
-- É uma diferença de estratégia: quantidade (Activision) vs. concentração (Rockstar)

select 
	v.publisher as empresa,
	round(sum(v.total_sales)::numeric, 2) as copias_vendidas
from vgchartz v 
where v.total_sales is not null 
group by v.publisher 
order by copias_vendidas desc 
limit 10;