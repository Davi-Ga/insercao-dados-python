import csv
import time
import insertQuerys
import progressbar

def insertData(): #Método que lê o arquivo do tipo .csv
    with open ('2021-11-gasolina-etanol.csv',encoding='utf8') as file:  #Abre o arquivo com o tipo UTF-8 para ler em PT-BR
        reader = csv.reader(file,delimiter=';') #Separação das colunas do csv é feita por ';'
        print("----------------------Iniciando a inserção no BD----------------------\n")
        rowCounter=0 
        bar=progressbar.ProgressBar(max_value=progressbar.UnknownLength) #Cria uma barra de progresso|
        for row in reader:
            
            if(rowCounter>1):
                
                if time.localtime().tm_sec==30:
                    break
                insertQuerys.insertCity(row[0],row[1],row[2]) #Chama o metodo da 1º tabela, cada row é uma coluna do CSV, então row[0]=Region,row[1]=State,row[2]=City
                insertQuerys.insertUnity(row[3],row[4],row[9],row[8],row[2],row[1]) #Chama o metodo da 2º tabela
                insertQuerys.insertProduct(row[10],row[12],row[11],row[15],row[3])  #Chama o metodo da 3º tabela
                bar.update(rowCounter)
                
            rowCounter+=1
        
        print("--------------------------------Inserção Conluída---------------------------------")

        
                
    
   

