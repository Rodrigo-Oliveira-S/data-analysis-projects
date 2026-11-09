import pandas as pd

def check_all():
	"""Executa todos os testes de qualidade."""
	print("Teste de qualidade...")
	check_nao_vazio('../data/01_total_vendas.csv')
	check_nao_vazio('../data/01_vendas_mes.csv')
	check_nao_vazio('../data/02_crescimento.csv')
	check_nao_vazio('../data/03_consumo.csv')
	check_nao_vazio('../data/04_campanha.csv')
	check_nao_vazio('../data/05_pais.csv')
	check_nao_vazio('../data/06_tempo_relacionamento.csv')
	check_nao_vazio('../data/07_faixa_etaria.csv')
	check_nao_vazio('../data/08_reclamacao.csv')
	print("Testes concluídos.")

def check_nao_vazio(arquivo):
	"""Verifica se o arquivo não está vazio."""
	df = pd.read_csv(arquivo)
	if len(df) == 0:
		print(f"Alerta: {arquivo} está vazio.")
	else:
		print(f"OK: {arquivo} - {len(df)} linhas")
