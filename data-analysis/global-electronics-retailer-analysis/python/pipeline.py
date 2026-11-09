from database import get_engine
from queries import (
	faturamento_total, faturamento_desempenho,
	produto_top, top_produtos, top_pais, top_moedas,
	margem_mes, margem_desempenho, margem_categoria
)
from quality_checks import check_all
import pandas as pd

mes = '2019-12'

engine = get_engine()

df = pd.read_sql(faturamento_total(), engine)
df.to_csv('../data/01_faturamento_total.csv', index=False)
df.to_sql('faturamento_total', engine, if_exists='replace', index=False)

df = pd.read_sql(faturamento_desempenho(), engine)
df.to_csv('../data/02_faturamento_desempenho.csv', index=False)
df.to_sql('faturamento_desempenho', engine, if_exists='replace', index=False)

df = pd.read_sql(produto_top(mes), engine)
df.to_csv('../data/03_produto_top.csv', index=False)
df.to_sql('produto_top', engine, if_exists='replace', index=False)

df = pd.read_sql(top_produtos(mes), engine)
df.to_csv('../data/04_top_produtos.csv', index=False)
df.to_sql('top_produtos', engine, if_exists='replace', index=False)

df = pd.read_sql(top_pais(mes), engine)
df.to_csv('../data/05_top_pais.csv', index=False)
df.to_sql('top_pais', engine, if_exists='replace', index=False)

df = pd.read_sql(top_moedas(mes), engine)
df.to_csv('../data/06_top_moedas.csv', index=False)
df.to_sql('top_moedas', engine, if_exists='replace', index=False)

df = pd.read_sql(margem_mes(mes), engine)
df.to_csv('../data/07_margem_mes.csv', index=False)
df.to_sql('margem_mes', engine, if_exists='replace', index=False)

df = pd.read_sql(margem_desempenho(), engine)
df.to_csv('../data/08_margem_desempenho.csv', index=False)
df.to_sql('margem_desempenho', engine, if_exists='replace', index=False)

df = pd.read_sql(margem_categoria(mes), engine)
df.to_csv('../data/09_margem_categoria.csv', index=False)
df.to_sql('margem_categoria', engine, if_exists='replace', index=False)

check_all()

print("Pipeline executado com sucesso para a data: ", mes)
