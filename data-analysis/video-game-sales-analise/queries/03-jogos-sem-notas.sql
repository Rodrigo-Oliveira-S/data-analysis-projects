-- Temos 57.338 jogos sem notas. 
-- O dataset contém 64.016 registros, mas apenas 10,4% possuem nota do Metacritic.
-- As análises de nota consideram apenas esse subconjunto.

select 
	count(*) as total_jogos,
	count(v.critic_score) as jogos_com_nota,
	count(*) - count(v.critic_score) as jogos_sem_nota
from vgchartz v 