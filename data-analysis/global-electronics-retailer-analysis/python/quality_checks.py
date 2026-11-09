import pandas as pd

def check_all():
    """Executa Todos os Testes de qualidade."""
    print("Teste de qualidade...")
    check_nao_vazio('../data/01_faturamento_total.csv')
    check_nao_vazio('../data/02_faturamento_desempenho.csv')
    check_nao_vazio('../data/03_produto_top.csv')
    check_nao_vazio('../data/04_top_produtos.csv')
    check_nao_vazio('../data/05_top_pais.csv')
    check_nao_vazio('../data/06_top_moedas.csv')
    check_nao_vazio('../data/07_margem_mes.csv')
    check_nao_vazio('../data/08_margem_desempenho.csv')
    check_nao_vazio('../data/09_margem_categoria.csv')
    print("Testes Concluídos")

def check_nao_vazio(arquivo):
    """Verifica se o arquivo não está vazio"""
    df = pd.read_csv(arquivo)
    if len(df) == 0:
        print(f"Alerta: {arquivo} está vazio.")
    else:
        print(f"OK: {arquivo} - {len(df)} linhas")
