def faturamento_total():
	return f"""
	
with 
        
faturamento_geral as (      
	select
        	count(distinct s."Order Number") as qtde_pedidos,
        	sum(s."Quantity") as qtde_vendas,
        	round(sum(s."Quantity" * p."Unit Price USD")::numeric, 2) as faturamento_bruto,
        	round(sum(s."Quantity" * p."Unit Cost USD")::numeric, 2) as custo_total,
        	round(sum(s."Quantity" * (p."Unit Price USD" - p."Unit Cost USD"))::numeric, 2) as faturamento_liquido
    	from 
        	"Sales" s
    	join 
        	"Products" p on p."ProductKey" = s."ProductKey"
    	)
    	select
        	qtde_pedidos,
        	qtde_vendas,
        	faturamento_bruto,
        	custo_total,
        	faturamento_liquido,
        	round(sum(faturamento_bruto / qtde_pedidos)::numeric, 2) as ticket_medio
    	from 
        	faturamento_geral
    	group by
        	qtde_pedidos,
        	qtde_vendas,
        	faturamento_bruto,
        	custo_total,
        	faturamento_liquido;
	"""

def faturamento_desempenho():
	return f"""

    with 
        faturamento_geral as (      
    select
        to_char(s."Order Date"::date, 'YYYY-MM') as data,
        round(sum(s."Quantity" * p."Unit Price USD")::numeric, 2) as faturamento_bruto,
        round(sum(s."Quantity" * p."Unit Cost USD")::numeric, 2) as custo_total,
        round(sum(s."Quantity" * (p."Unit Price USD" - p."Unit Cost USD"))::numeric, 2) as faturamento_liquido
    from 
        "Sales" s
    join 
        "Products" p on p."ProductKey" = s."ProductKey"
    group by
        to_char(s."Order Date"::date, 'YYYY-MM')
    )
    select
        data,
        faturamento_bruto,
        custo_total,
        faturamento_liquido,
        round(avg(faturamento_liquido) over(), 2) as media_mes
    from
        faturamento_geral
    order by 
        faturamento_bruto desc;

	"""

def produto_top(mes):
	return f"""

    select
        p."Product Name" as produtos,
        round(sum(s."Quantity" * (p."Unit Price USD" - p."Unit Cost USD"))::numeric, 2) as faturamento_liquido
    from "Sales" s
    join "Products" p on p."ProductKey" = s."ProductKey"
    where to_char(s."Order Date"::date, 'YYYY-MM') = '{mes}'
    group by p."Product Name"
    order by faturamento_liquido desc
    limit 1;
    """

def top_produtos(mes):
	return f"""

    select
        p."Product Name" as produtos,
        round(sum(s."Quantity" * (p."Unit Price USD" - p."Unit Cost USD"))::numeric, 2) as faturamento_liquido
    from "Sales" s
    join "Products" p on p."ProductKey" = s."ProductKey"
    where to_char(s."Order Date"::date, 'YYYY-MM') = '{mes}'
    group by p."Product Name"
    order by faturamento_liquido desc
    limit 5;
    """

def top_pais(mes):
	return f"""

    select
        "Country" as compras_pais,
        round(sum(s."Quantity" * (p."Unit Price USD" - p."Unit Cost USD"))::numeric, 2) as faturamento_liquido
    from "Sales" s
    join "Products" p on p."ProductKey" = s."ProductKey"
    join "Customers" c on c."CustomerKey" = s."CustomerKey"
    where to_char(s."Order Date"::date, 'YYYY-MM') = '{mes}'
    group by "Country"
    order by faturamento_liquido desc
    limit 5;
    """


def top_moedas(mes):
	return f"""

    select
        "Currency Code" as moeda_utilizada,
        round(sum(s."Quantity" * p."Unit Price USD")::numeric, 2) as faturamento_bruto
    from "Sales" s
    join "Products" p on p."ProductKey" = s."ProductKey"
    join "Customers" c on c."CustomerKey" = s."CustomerKey"
    where to_char(s."Order Date"::date, 'YYYY-MM') = '{mes}'
    group by "Currency Code"
    order by faturamento_bruto desc
    limit 5;
    """

def margem_mes(mes):
	return f"""

    select
        to_char(s."Order Date"::date, 'YYYY-MM') as data,
        round(
            (
                (
                    sum(s."Quantity" * (p."Unit Price USD" - p."Unit Cost USD"))
                    /
                    sum(s."Quantity" * p."Unit Price USD")
                )::numeric * 100
            ), 2
        ) as margem
    from "Sales" s
    join "Products" p on p."ProductKey" = s."ProductKey"
    where to_char(s."Order Date"::date, 'YYYY-MM') = '{mes}'
    group by data;
    """

def margem_desempenho():
	return f"""

    select
        to_char(s."Order Date"::date, 'YYYY-MM') as data,
        round(
            (
                (
                    sum(s."Quantity" * (p."Unit Price USD" - p."Unit Cost USD"))
                    /
                    sum(s."Quantity" * p."Unit Price USD")
                )::numeric * 100
            ), 2
        ) as margem
    from "Sales" s
    join "Products" p on p."ProductKey" = s."ProductKey"
    group by data
    order by data asc;
    """

def margem_categoria(mes):
	return f"""

    select
        p."Category" as categoria,
        round(
            (
                (
                    sum(s."Quantity" * (p."Unit Price USD" - p."Unit Cost USD"))
                    /
                    sum(s."Quantity" * p."Unit Price USD")
                )::numeric * 100
            ), 2
        ) as margem
    from "Sales" s
    join "Products" p on p."ProductKey" = s."ProductKey"
    where to_char(s."Order Date"::date, 'YYYY-MM') = '{mes}'
    group by categoria
    order by margem desc;
    """
