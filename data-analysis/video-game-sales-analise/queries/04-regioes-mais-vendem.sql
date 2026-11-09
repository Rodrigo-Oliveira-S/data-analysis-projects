-- América do Norte lidera com 3.345 milhões de cópias, quase o dobro da Europa/África (1.916M).
-- Japão (687M) e Resto do Mundo (651M) têm volumes bem menores.

select 
	round(sum(v.na_sales)::numeric, 2) as copias_america,
	round(sum(v.jp_sales)::numeric, 2) as copias_japao,
	round(sum(v.pal_sales)::numeric, 2) as copias_europa_africa,
	round(sum(v.other_sales)::numeric, 2) as copias_restante_mundo
from vgchartz v 