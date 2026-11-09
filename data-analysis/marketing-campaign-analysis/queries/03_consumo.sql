

	select
        round(sum("MntWines")::numeric, 2) as vinhos,
        round(sum("MntFruits")::numeric, 2) as frutas,
        round(sum("MntMeatProducts")::numeric, 2) as carne,
        round(sum("MntFishProducts")::numeric,2) as peixe,
        round(sum("MntSweetProducts")::numeric,2) as doces,
        round(sum("MntGoldProds")::numeric, 2) as ouro
    from marketing_data;

	