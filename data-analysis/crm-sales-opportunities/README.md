## Análise de Performance de Vendas - CRM Sales Opportunities (2017)

Dados de pipeline de vendas B2B de uma empresa fictícia que vende hardware de computador, incluindo informações sobre contas, produtos, equipes de vendas e oportunidades de vendas.

## Ferramentas

- PostgreSQL
- Python (Jupyter Notebook)
- Excel
- Power Query

## Metodologia

- Armazenamento: Ingestão de dados brutos no PostgreSQL.

- Processamento e Análise: Conexão via SQLAlchemy, manipulação e extração de insights usando Python (Pandas) dentro do Jupyter Notebook.

- Visualização: Exportação dos dados tratados para o Excel para construção do Dashboard.

## Escopo da análise

1. Faturamento mês a mês quanto foi

2. Qual empresa mais compra

3. Qual sede mais compra os produtos

4. Top 10 representantes de vendas por faturamento

5. Top 10 gerentes de vendas por faturamento

6. Qual escritório regional tem mais vendas

7. Top 10 representantes de vendas por quantidade vendida

8. Top 10 Representantes de vendas que venderam mais rápido

9. Produto mais vendido

## Principais descobertas

1. Junho de 2017 foi o melhor mês, com US$ 884.971,00 em vendas. Março de 2017 ficou em segundo lugar com US$ 757.706,00 em vendas. Dezembro que é um mês de presentes, teve menos pedidos que Julho e Março.

2. Kan-code é a empresa que mais adquire produtos, já somados US$ 217.560,00. Eles compraram o produto GTK 500 de US$ 25.791,00 e depois só compraram produtos mais baratos.

3. Estados Unidos liderou com folga em compras de hardwares gastando US$ 5.519.293,00 e em segundo a Coréia gastando US$ 124.574,00. A diferença de uma pra outra é muito grande, quase 50 vezes mais que os EUA adquire. EUA investiu muito no produto GTX Plus Pro, que custa US$ 5.482 sendo ele o segundo produto mais caro.

4. Darcel Schlecht é o representante de vendas que mais traz lucro, com US$ 380.085,00 em vendas. O produto que ele mais vendeu foi o GTX Plus Pro de US$ 5.482, somando apenas com esse produto US$ 176.844,00 em vendas e também US$ 310.473,00 em vendas para os EUA. 
Em segundo lugar o James Ascencio, vendendo US$ 315.852,00 e o produto que ele mais vendeu foi o GTX Plus Pro, trazendo US$ 241.420,00 em faturamento, vendendo até melhor esse produto do que o Darcel Schlecht. James Ascencio vendeu US$ 283.294,00 para os EUA, ou seja, os 2 melhores vendedores, vendem para a sede que mais compra.

5. Celia Rouche é a gerente que mais vende, trazendo US$ 1.259.786,00 de faturamento. A melhor representante de vendas desse time é a Vicki Laflamme, que faturou US$ 289.370,00. Mesmo sendo a gerente com o melhor time de vendedores, os vendedores que mais faturam não são do grupo dela. 
O representante de vendas James Ascencio, que é o segundo melhor vendedor geral, trabalha na equipe do Summer Sewald, que é o segundo melhor gerente de vendas. 
O terceiro melhor gerente de vendas, o Melvin Marxen, tem no seu time o Darcel Schlecht, que é o representante, de vendas que mais gera lucro total dos representantes de vendas em geral.

6.  O escritório da região Oeste é o que mais fatura, vendendo US$ 2.447.825,00. A gerente de vendas que trabalha nesse escritório é a Celia Rouche, que tem a melhor equipe em faturamento. Summer Sewald sendo o gerente segundo melhor em faturamento também trabalha nesse escritório. Isso acaba explicando o por que essa região é a que mais vende.

7. Anna Snelling é a representante que mais vendeu em quantidade totalizando 208 vendas. Em faturamento geral ela ficou em 4° lugar, com de US$ 275.056,00. Ficando em segundo lugar o Darcel Schlecht, que no top 10 faturamento ficou em 1° lugar. Uma coisa fica mais nítido, Anna Snelling vende mais vezes, porém produtos mais baratos, já o Darcel Schlecht vende menos vezes, porém produtos mais caros.

8. A representante de vendas que vende mais rápido é a Rosie Papadopoulos, com uma média de 41 dias pra fechar negócio. Ela não aparece nem no top 10 quantidades vendidas, nem no top 10 faturamento.
Em segundo lugar aparece a Cecily Lampkin, com uma média de 42 dias para fechar negócio.
Já em terceiro lugar, com uma média de 44 dias, temos o Elease Gluck, e ele sim aparece em 7° lugar no top 10 faturamento. Isso mostra que ele, aparentemente traz bons faturamentos e também vende rápido.
Marty Freudenburg que aqui ficou em 6° demorando uma média de 48 dias pra vender, no ranking de faturamento está em 9° lugar, e também merece uma atenção, pois também traz boas vendas e mais rápido.

9. O produto GTX Plus Pro é o que mais trouxe faturamento (US$ 2.629.651,00) pois é o segundo produto mais caro (US$ 5.482), porém o GTX Basic foi o que mais vendeu em quantidade, com 1436 produtos vendidos, e talvez seja pelo seu preço ser o penúltimo mais barato, custando US$ 550, e por isso na ordem de faturamento ficou em 4° lugar, com US$ 499.263,00 em vendas.

## Estrutura do projeto

- `dados/` - CSVs extraídos das consultas SQL
- `dashboard/` - Planilha com capa, dados brutos, análises de apoio e dashboard final
- `python/` - Arquivo .ipynb da análise feita no jupyter notebook, e script .py para análises futuras
- `queries/` - Consultas SQL usadas na análise
