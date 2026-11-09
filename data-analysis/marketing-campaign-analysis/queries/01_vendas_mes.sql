

	select
        sum("NumDealsPurchases") as compras_desconto,
        sum("NumWebPurchases") as compras_web,
        sum("NumCatalogPurchases") as compras_catalogo,
        sum("NumStorePurchases") as compras_loja,
        sum(
            "NumDealsPurchases" + "NumWebPurchases" + "NumCatalogPurchases" + "NumStorePurchases"
        ) as total
    	from marketing_data
    	where to_char("Dt_Customer"::date, 'YYYY-MM') = '2013-08';

	