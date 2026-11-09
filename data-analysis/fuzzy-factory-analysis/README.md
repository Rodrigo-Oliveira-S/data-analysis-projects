## Análise de Vendas - Fuzzy Factory (2012-2015)

Este conjunto de dados é um banco de dados de comércio eletrônico para Maven Fuzzy Factory, um varejista on-line especializado na venda de ursinhos de pelúcia. 

## Ferramentas

- PostgreSQL
- Python (Jupyter Notebook)
- Metabase

## Metodologia

- Armazenamento: Ingestão de dados brutos no PostgreSQL.

- Processamento e Análise: Conexão via SQLAlchemy, manipulação e extração de insights usando Python (Pandas) dentro do Jupyter Notebook.

- Visualização: Conexão direta com o Metabase para construção do Dashboard.

## Escopo da análise

1. Qual o faturamento da empresa

2. Através de qual mídia os produtos mais vendem

3. Qual produto traz lucro líquido para a empresa

4. Qual produto tem mais vendas em quantidade

5. O produto que mais traz lucro líquido, é mais vendido através de qual campanha

6. Qual produto teve mais reembolso

7. Através de qual dispositivo existe mais vendas (mobile/desktop)

## Principais descobertas

1. A empresa teve seu maior faturamento em dezembro de 2014, com US$ 214.665,34. É notável que a empresa está em crescimento, porém é importante destacar que o faturamento só ficou acima da média a partir de fevereiro de 2014, quase 3 anos após o início das vendas. No começo, as variações de um mês para o outro eram grandes, depois de 1 ano estabilizou.

2. 65% dos compradores totais da Fuzzy Factory vem pelo Google search, trazendo US$ 1.276.144,89 em faturamento.

3. The Original Mr. Fuzzy é lider absoluto nas vendas, com US$ 738.893,00 de lucro líquido. 3x mais que o segundo lugar, o The Forever Love Bear que faturou US$ 217.350,00.

4. The Original Mr. Fuzzy lidera também em quantidades, vendendo 24226 produtos. O segundo lugar, The Forever Love Bear vendeu 5796 quantidades, muito abaixo do primeiro lugar.

5. A campanha que o The Original Mr. Fuzzy foi mais vendido é chamada de Campanha Genérica, com 17192 quantidades vendidas, e trazendo US$ 524.356,00 de lucro líquido. Isso significa que a empresa está conquistando clientes que não conheciam a marca.

6. Por ser o produto mais vendido, The Original Mr. Fuzzy também é o produto que mais teve reembolso US$ 69.361,92 foi reembolsado.

7. As vendas do The Original Mr. Fuzzy lideram através do Desktop, faturando US$ 638.822,50 e com 20945 em quantidades vendidas. Já pelo Mobile o mesmo produto também é o mais vendido, porém pelo faturamento de US$ 100.070,50.

## Estrutura do projeto

- `dados/` - CSVs extraídos das consultas SQL
- `dashboard/` - Insights visualizados no Metabase, organizados com capa e dashboard.
- `python/` - Arquivo .ipynb da análise feita no jupyter notebook, e script .py para análises futuras
- `queries/` - Consultas SQL usadas na análise
- `raw/` - CSVs originais, como vieram da fonte de dados