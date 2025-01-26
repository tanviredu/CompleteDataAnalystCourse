import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base,Data

class DataLake:
    def __init__(self,DATABSAE_URL = "sqlite:///datalake.db"):
        self.db_file = DATABSAE_URL
        self.engine  = create_engine(self.db_file,echo=True) 
        self.Session = sessionmaker(bind=self.engine)
        self.create_table()

    def create_table(self):
        Base.metadata.create_all(self.engine)
        print("[*] Table Created successfully")

    def collect_data(self,value):
        session = self.Session()
        try:
            new_data = Data(value = value)
            session.add(new_data)
            session.commit()
            print("[*] Data added : {}".format(new_data))
        except:
            session.rollback()
            print("[-] Error Rolling back")
        
        finally:
            session.close()

    def retrieve_data(self):
        query = "SELECT * FROM data"
        df    = pd.read_sql_query(query,self.engine)
        return df

    def analyze_data(self):
        data       = self.retrieve_data()
        mean_value = data['value'].mean()
        std_value  = data['value'].std() 
        return mean_value,std_value


    def visualize_data(self):
        data = self.retrieve_data()
        plt.plot(data['timestamp'],data['value'])
        plt.xlabel("timestamp")
        plt.ylabel("value")
        plt.title("Data Lake Visualization")
        plt.savefig("output-1.jpg")
        
        
