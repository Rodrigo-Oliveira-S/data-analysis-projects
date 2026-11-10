# Data Ingestion Worker

Serviço automatizado em Python para consumo da API REST da Binance, validação de schemas de dados e persistência relacional em PostgreSQL.

## Arquitetura e Tecnologia

- **Linguagem:** Python 3.13
- **Cliente HTTP:** `httpx` (consumo de API REST pública da Binance)
- **Validação de Dados:** `pydantic` (conversão e sanitização de dados)
- **ORM & Persistência:** `SQLAlchemy` + `psycopg2-binary`
- **Banco de Dados:** PostgreSQL 16 (executado em container Podman/Docker)
- **Gerenciamento de Ambiente:** `python-dotenv` e ambiente virtual `.venv`

## Fluxo de Funcionamento

1. **Requisição REST:** O serviço faz uma chamada `GET` controlada a cada 60 segundos para o endpoint público da Binance (`https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT`).
2. **Tratamento de Exceções:** Trata potenciais falhas de rede (`httpx.RequestError`), timeouts e códigos de erro HTTP (`4xx`/`5xx`).
3. **Validação de Schema:** O payload JSON recebido é validado e sanitizado via Pydantic (`CryptoPriceSchema`).
4. **Persistência Relacional:** Os dados são mapeados via SQLAlchemy para a tabela `crypto_rates` e gravados no banco de dados `db_data_worker`.

## Estrutura do Projeto

```text
data-ingestion-worker/
├── data/               # Arquivos de suporte e dados temporários
├── src/
│   ├── database.py     # Gerenciamento de conexão e sessão do PostgreSQL
│   ├── models.py       # Modelo ORM (tabela 'crypto_rates')
│   ├── schemas.py      # Schemas Pydantic para validação
│   ├── client.py       # Cliente HTTP resiliente para a API da Binance
│   └── worker.py       # Orquestrador do laço de ingestão contínua
├── .env.example        # Modelo de variáveis de ambiente
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação técnica