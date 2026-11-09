-- o gênero que mais vende no mundo todo é Sports (1.18 bilhões de cópias)
-- O gênero Sports lidera em vendas na América do Norte (607.47 milhões de cópias) e Resto do mundo (128.19 milhões de cópias).
-- No Japão o Role-Playing é mais famoso, com 130.56 milhões de cópias vendidas desse gênero.
-- Já na Europa e África a briga foi boa, mas por pouco Action venceu com 342.52 milhões de cópias,
-- deixando Sports em segundo lugar.

select 
	v.genre as genero,
	round(sum(v.na_sales)::numeric, 2) as america_norte,
	round(sum(v.jp_sales)::numeric, 2) as japao,
	round(sum(v.pal_sales)::numeric, 2) as europa_africa,
	round(sum(v.other_sales)::numeric, 2) as resto_mundo,
	round(sum(v.total_sales)::numeric, 2) as total
from vgchartz v 
where v.total_sales is not null 
group by v.genre 
order by total desc