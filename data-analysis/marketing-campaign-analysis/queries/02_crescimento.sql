

	with total_vendas_qtde as (
    
    	select
        to_char("Dt_Customer"::date, 'YYYY-MM') as mes_compras,
        sum("NumDealsPurchases") as compras_desconto,
        sum("NumWebPurchases") as compras_web,
        sum("NumCatalogPurchases") as compras_catalogo,
        sum("NumStorePurchases") as compras_loja,
        sum("NumDealsPurchases") + sum("NumWebPurchases") + sum("NumCatalogPurchases") + sum("NumStorePurchases") as total_vendas
    	from marketing_data
    	group by to_char("Dt_Customer"::date, 'YYYY-MM')
    	order by to_char("Dt_Customer"::date, 'YYYY-MM') asc

    )

    select
        mes_compras,
        compras_desconto,
        compras_web,
        compras_catalogo,
        compras_loja,
        total_vendas,
        round(
            ((total_vendas - lag(total_vendas) over(order by mes_compras))
            / lag(total_vendas) over(order by mes_compras)) * 100, 2
            ) as variacao_percentual,
        round(avg(total_vendas) over()) as media_mes,
        case
            when total_vendas > round(avg(total_vendas) over()) then 'Acima da Média'
            else 'Abaixo da Média'
        end as classificação
    from total_vendas_qtde;

	