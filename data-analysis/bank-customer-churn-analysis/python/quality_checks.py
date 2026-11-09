import pandas as pd

def check_all():
	""" Executa todos os testes de qualidade."""
	print("Teste de qualidade...")
	check_nao_vazio('../data/01_volume_total_saldo.csv')
	check_nao_vazio('../data/02_clientes_mais_produtos.csv')
	check_nao_vazio('../data/03_faixa_etaria_clientes.csv')
	check_nao_vazio('../data/04_tempo_relacionamento.csv')
	check_nao_vazio('../data/05_categoria_renda.csv')
	check_nao_vazio('../data/06_porcentagem_cancelamento.csv')
	print("Testes concluídos.")

def check_nao_vazio(arquivo):
	"""Verifica se o arquivo não está vazio."""
	df = pd.read_csv(arquivo)
	if len(df) == 0:
		print(f"Alerta: {arquivo} está vazio!")
	else:
		print(f"OK: {arquivo} - {len(df)} linhas")
