import pymongo
import os, sys
from finance_complaint.constant.environment.variable_key import MONGO_DB_URL_ENV_KEY
import certifi
import ssl
ca = certifi.where()
from finance_complaint.constant.database import DATABASE_NAME
from finance_complaint.exception import FinanceException

class MongodbClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongodbClient.client is None:
                mongo_db_url = os.getenv(MONGO_DB_URL_ENV_KEY)
                print(mongo_db_url)
                if "localhost" in mongo_db_url:
                    MongodbClient.client = pymongo.MongoClient(mongo_db_url)
                else:
                    MongodbClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongodbClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e