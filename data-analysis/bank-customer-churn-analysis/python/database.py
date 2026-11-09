from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

def get_engine():
    return create_engine(
    	f'postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}'
    	f'@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/db_bank_customer_churn'
)
