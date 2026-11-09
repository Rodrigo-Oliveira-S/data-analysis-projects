-- Analisando as maiores notas, o Grand Theft Auto IV e Red Dead Redemption: Undead Nightmare seguem empatados, ambos com nota 10
-- Porém a divergencia entre o volume de cópias vendidas é muito grande
-- Grand Theft Auto IV com 21.66 milhões de cópias vendidas
-- Red Dead Redemption: Undead Nightmare com 2.29 milhões de cópias vendidas
-- Grand Theft Auto IV vende quase 20 vezes a mais que Red Dead Redemption: Undead Nightmare
-- Rockstar Games lidera no ranking de notas da metacritic
-- O gênero Action dominou tanto em notas quanto em vendas no top 10
-- Rockstar Games concentra metade dos jogos com as maiores notas do Metacritic

select 
	v.title as nome_jogo,
	v.genre as genero,
	v.publisher as empresa,
	v.critic_score as notas,
	round(sum(v.total_sales)::numeric, 2) as copias_vendidas
from vgchartz v 
where v.critic_score is not null 
	and v.total_sales is not null 
group by v.title, v.genre, v.publisher, v.critic_score 
order by v.critic_score desc 
limit 10;