

	select
        sum("NumDealsPurchases") as compras_desconto,
        sum("NumWebPurchases") as compras_web,
        sum("NumCatalogPurchases") as compras_catalogo,
        sum("NumStorePurchases") as compras_loja,
        sum(
            "NumDealsPurchases" + "NumWebPurchases" + "NumCatalogPurchases" + "NumStorePurchases"
            ) as total
    from marketing_data;

	