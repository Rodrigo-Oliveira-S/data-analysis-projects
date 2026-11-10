import os
import httpx
from dotenv import load_dotenv

load_dotenv()

BINANCE_API_URL = os.getenv("BINANCE_API_URL", "https://api.binance.com/api/v3/ticker/price")

def fetch_crypto_price(symbol: str = "BTCUSDT") -> dict:
    """
    Realiza uma requisição GET para a API REST pública da Binance
    para obter a cotação em tempo real de um par de moedas.
    """
    params = {"symbol": symbol}
    
    try:
        with httpx.Client(timeout=10.0) as client:
            response = client.get(BINANCE_API_URL, params=params)
            
            response.raise_for_status()
            
            return response.json()
            
    except httpx.HTTPStatusError as exc:
        print(f"Erro de Status HTTP ao consultar a Binance: {exc.response.status_code} - {exc}")
        raise
    except httpx.RequestError as exc:
        print(f"Erro de conexão/rede ao se comunicar com a Binance: {exc}")
        raise
    except Exception as exc:
        print(f"Erro inesperado no cliente HTTP: {exc}")
        raise

if __name__ == "__main__":
    try:
        data = fetch_crypto_price("BTCUSDT")
        print(f"Dados retornados da API da Binance: {data}")
    except Exception as e:
        print(f"Falha ao executar o teste do cliente HTTP: {e}")