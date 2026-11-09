def total_vendas():
	return """

	select
        sum("NumDealsPurchases") as compras_desconto,
        sum("NumWebPurchases") as compras_web,
        sum("NumCatalogPurchases") as compras_catalogo,
        sum("NumStorePurchases") as compras_loja,
        sum(
            "NumDealsPurchases" + "NumWebPurchases" + "NumCatalogPurchases" + "NumStorePurchases"
            ) as total
    from marketing_data;

	"""

def vendas_mes(mes):
        return f"""

	select
        sum("NumDealsPurchases") as compras_desconto,
        sum("NumWebPurchases") as compras_web,
        sum("NumCatalogPurchases") as compras_catalogo,
        sum("NumStorePurchases") as compras_loja,
        sum(
            "NumDealsPurchases" + "NumWebPurchases" + "NumCatalogPurchases" + "NumStorePurchases"
        ) as total
    	from marketing_data
    	where to_char("Dt_Customer"::date, 'YYYY-MM') = '{mes}';

	"""

def crescimento():
	return """

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

	"""

def consumo():
	return """

	select
        round(sum("MntWines")::numeric, 2) as vinhos,
        round(sum("MntFruits")::numeric, 2) as frutas,
        round(sum("MntMeatProducts")::numeric, 2) as carne,
        round(sum("MntFishProducts")::numeric,2) as peixe,
        round(sum("MntSweetProducts")::numeric,2) as doces,
        round(sum("MntGoldProds")::numeric, 2) as ouro
    from marketing_data;

	"""

def campanha(mes):
	return f"""

        select
        sum("AcceptedCmp1") as primeira_campanha,
        sum("AcceptedCmp2") as segunda_campanha,
        sum("AcceptedCmp3") as terceira_campanha,
        sum("AcceptedCmp4") as quarta_campanha,
        sum("AcceptedCmp5") as quinta_campanha
    from marketing_data
    where to_char("Dt_Customer"::date, 'YYYY-MM') = '{mes}';

	"""

def pais(mes):
	return f"""

	select
        "Country" as localidade_cliente,
        round((
            sum("MntWines"::numeric + "MntFruits"::numeric 
            + "MntMeatProducts"::numeric + "MntFishProducts"::numeric 
            + "MntSweetProducts"::numeric + "MntGoldProds")::numeric
            ), 2) as gasto_total
    from marketing_data
    where to_char("Dt_Customer"::date, 'YYYY-MM') = '{mes}'
    group by "Country"
    order by gasto_total desc;

	"""

def tempo_relacionamento():
	return """

	with tempo as (

    select
        "ID" as identificacao_cliente,
        (select max("Dt_Customer"::date) from marketing_data) - "Dt_Customer"::date as dias_relacionamento
    from marketing_data
    group by "ID", "Dt_Customer"
    order by dias_relacionamento desc

    )

    select
        count("identificacao_cliente") as qtde_clientes,
        case
            when dias_relacionamento < 365 then 'Menos de 1 ano'
            else 'Mais de 1 ano'
        end as tempo_relacionamento
    from tempo
    group by
        case
            when dias_relacionamento < 365 then 'Menos de 1 ano'
            else 'Mais de 1 ano'
        end;

	"""

def faixa_etaria():
	return """

	select
        count("ID") as qtde_clientes,
        case
            when extract(year from "Dt_Customer"::date) - "Year_Birth" between 18 and 23 then 'Jovens'
            when extract(year from "Dt_Customer"::date) - "Year_Birth" between 24 and 65 then 'Adultos'
            else 'Idosos'
        end as faixa_etaria,
        round(count(*) / sum(count(*)) over() * 100, 2) as porcentagem_total
    from marketing_data
    group by
        case
            when extract(year from "Dt_Customer"::date) - "Year_Birth" between 18 and 23 then 'Jovens'
            when extract(year from "Dt_Customer"::date) - "Year_Birth" between 24 and 65 then 'Adultos'
            else 'Idosos'
        end
    order by qtde_clientes desc;

	"""
def reclamacao():
	return """

	select
        count("ID") as qtde_clientes,
        case
            when "Complain" = 1 then 'Reclamaram'
            else 'Não reclamaram'
        end as reclamacao,
        round(count(*) / sum(count(*)) over() * 100, 2) as porcentagem_total
    from marketing_data
    group by "Complain"
    order by count("ID") desc;

	"""
