
	
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
	