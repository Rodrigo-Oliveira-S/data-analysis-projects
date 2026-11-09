from database import get_engine
from queries import (
	total_vendas, vendas_mes,  crescimento, consumo,
	campanha, pais, tempo_relacionamento,
	faixa_etaria, reclamacao
)
from quality_checks import check_all
import pandas as pd

mes = '2012-10'

engine = get_engine()

df = pd.read_sql(total_vendas(), engine)
df.to_csv('../data/01_total_vendas.csv', index=False)
df.to_sql('total_vendas', engine, if_exists='replace', index=False)

df = pd.read_sql(vendas_mes(mes), engine)
df.to_csv('../data/01_vendas_mes.csv', index=False)
df.to_sql('vendas_mes', engine, if_exists='replace', index=False)

df = pd.read_sql(crescimento(), engine)
df.to_csv('../data/02_crescimento.csv', index=False)
df.to_sql('crescimento', engine, if_exists='replace', index=False)

df = pd.read_sql(consumo(), engine)
df.to_csv('../data/03_consumo.csv', index=False)
df.to_sql('consumo', engine, if_exists='replace', index=False)

df = pd.read_sql(campanha(mes), engine)
df.to_csv('../data/04_campanha.csv', index=False)
df.to_sql('campanha', engine, if_exists='replace', index=False)

df = pd.read_sql(pais(mes), engine)
df.to_csv('../data/05_pais.csv', index=False)
df.to_sql('pais', engine, if_exists='replace', index=False)

df = pd.read_sql(tempo_relacionamento(), engine)
df.to_csv('../data/06_tempo_relacionamento.csv', index=False)
df.to_sql('tempo_relacionamento', engine, if_exists='replace', index=False)

df = pd.read_sql(faixa_etaria(), engine)
df.to_csv('../data/07_faixa_etaria.csv', index=False)
df.to_sql('faixa_etaria', engine, if_exists='replace', index=False)

df = pd.read_sql(reclamacao(), engine)
df.to_csv('../data/08_reclamacao.csv', index=False)
df.to_sql('reclamacao', engine, if_exists='replace', index=False)

check_all()

print("Pipeline executado com sucesso para a data: ", mes)
