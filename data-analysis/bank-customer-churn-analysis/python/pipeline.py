from database import get_engine
from queries import (

	volume_total_saldo, clientes_mais_produtos,
	faixa_etaria_clientes, tempo_relacionamento,
	categoria_renda, porcentagem_cancelamento
)

from quality_checks import check_all
import pandas as pd

engine = get_engine()

df = pd.read_sql(volume_total_saldo(), engine)
df.to_csv('../data/01_volume_total_saldo.csv', index=False)

df = pd.read_sql(clientes_mais_produtos(), engine)
df.to_csv('../data/02_clientes_mais_produtos.csv', index=False)

df = pd.read_sql(faixa_etaria_clientes(), engine)
df.to_csv('../data/03_faixa_etaria_clientes.csv', index=False)

df = pd.read_sql(tempo_relacionamento(), engine)
df.to_csv('../data/04_tempo_relacionamento.csv', index=False)

df = pd.read_sql(categoria_renda(), engine)
df.to_csv('../data/05_categoria_renda.csv', index=False)

df = pd.read_sql(porcentagem_cancelamento(), engine)
df.to_csv('../data/06_porcentagem_cancelamento.csv', index=False)

check_all()
