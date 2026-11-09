-- Analisando por cópias vendidas, o Grand Theft Auto V lidera, sendo o jogo mais vendido pela Rockstar Games
-- Call of Duty aparece com várias versões no Top 10, mostrando que a franquia
-- mantém relevância ao longo de diferentes lançamentos e gerações de consoles.

select 
	v.title as nome_jogo,
	v.genre as genero,
	v.publisher as empresa,
	round(sum(v.total_sales)::numeric, 2) as copias_vendidas
from vgchartz v 
where v.critic_score is not null 
	and v.total_sales is not null 
group by v.title, v.publisher, v.genre 
order by copias_vendidas desc 
limit 10;