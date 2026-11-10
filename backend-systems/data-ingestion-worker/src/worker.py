import time
from datetime import datetime, timezone
from client import fetch_crypto_price
from schemas import CryptoPriceSchema
from database import SessionLocal
from models import CryptoRate

INTERVAL_SECONDS = 60  # Pausa de 1 minuto entre as requisições

def run_ingestion_cycle():
    """
    Executa um ciclo completo de ingestão:
    1. Consome a API da Binance
    2. Valida o payload recebido via Pydantic
    3. Persiste os dados na tabela 'crypto_rates' do PostgreSQL
    """
    db = SessionLocal()
    try:
        raw_data = fetch_crypto_price("BTCUSDT")
        
        validated_data = CryptoPriceSchema(**raw_data)
        
        crypto_record = CryptoRate(
            symbol=validated_data.symbol,
            price=validated_data.price,
            fetched_at=datetime.now(timezone.utc)        
        )
        
        db.add(crypto_record)
        db.commit()
        db.refresh(crypto_record)
        
        print(f"[{crypto_record.fetched_at.strftime('%Y-%m-%d %H:%M:%S')}] "
              f"Sucesso: {crypto_record.symbol} | Preço: US$ {crypto_record.price:.2f} "
              f"registrado no ID #{crypto_record.id}")
        
    except Exception as exc:
        db.rollback()
        print(f"[{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}] "
              f"Falha na execução do ciclo de ingestão: {exc}")
    finally:
        db.close()

def main():
    print("=== DATA INGESTION WORKER INICIADO ===")
    print(f"Monitorando cotações Binance (BTCUSDT) a cada {INTERVAL_SECONDS} segundos.")
    print("Pressione Ctrl+C para encerrar o worker.\n")
    
    try:
        while True:
            run_ingestion_cycle()
            time.sleep(INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nWorker interrompido manualmente pelo usuário. Encerrando rotina...")

if __name__ == "__main__":
    main()