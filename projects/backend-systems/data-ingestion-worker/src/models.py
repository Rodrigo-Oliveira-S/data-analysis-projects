from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base

class CryptoRate(Base):
    __tablename__ = "crypto_rates"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(20), nullable=False, index=True) 
    price = Column(Float, nullable=False)                    
    fetched_at = Column(DateTime, default=datetime.utcnow)   

    def __repr__(self):
        return f"<CryptoRate(symbol='{self.symbol}', price={self.price}, fetched_at='{self.fetched_at}')>"


if __name__ == "__main__":
    from database import engine
    print("Criando tabela 'crypto_rates' no PostgreSQL se não existir...")
    Base.metadata.create_all(bind=engine)
    print("Tabela verificada/criada com sucesso!")