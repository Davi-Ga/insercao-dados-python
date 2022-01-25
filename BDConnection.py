import psycopg2
from pytest import param

#Dados do banco utilizado
DB_HOST = "localhost"
DB_NAME = "testebd"
DB_USER = "postgres"
DB_PASS = "123543"

#Classe de conexão
class Connection:
    def __init__(self):
        self.conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password = DB_PASS,host = DB_HOST)
        self.cursor = self.conn.cursor()
    #Realiza conexão
    def connection(self):
        return self.conn
    
    #Ativa o banco
    def cursor(self):
        return self.cursor
    
    #Salva a alteração no banco
    def commit(self):
        return self.conn.commit()
    
    #Fecha a conexão, mas antes salva qualquer alteração
    def close(self,commit =True):
        if commit:
            self.commit()
        self.connection.close()
        
    #Executa qualquer ação do banco
    def execute(self,sql,params=None):
        return self.cursor.execute(sql,params or ())

    #Retorna algum valor buscado
    def fetchall(self):
        return self.cursor.fetchall()

    #Realiza o comando da query
    def query(self,sql,params=None):
        self.cursor.execute(sql,params or())
        return self.fetchall()

    #Realiza o INSERT 
    def insert(self,sql,params=None):
        self.cursor.execute(sql,params or())
        self.commit()
        return True

