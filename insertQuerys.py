from multiprocessing import connection
import BDConnection

#Método para inserir a 1º tabela
def insertCity(region,state,city): #Recebe argumentos do CSV das linhas da região,uf e cidade
    conn = BDConnection.Connection()
    queryConsultResult =conn.query("SELECT * FROM cidade WHERE nome='{2}'".format(region,state,city)) #Faz o select com o state {2}
    if queryConsultResult == []: #Caso a busca retorne nula, fará uma inserção, isso evita repetição de dados
        if conn.insert("INSERT INTO cidade(regiao,uf,nome) VALUES ('{0}','{1}','{2}')".format(region,state,city)):#Insere regiao {0}, uf{1} e nome{2}
            print("Região ",region," inserida\n")
            print("Estado ",state," inserida\n")
            print("Cidade ",city," inserida\n")

#Método para inserir a 2º tabela
def insertUnity(name,cnpj,cep,district,city,uf): #Recebe argumentos do CSV das linhas do nome da unidade,cnpj,cep,bairro,(cidade e uf)->Esses dois serve para fazer a relação entre a 1º tabela e a 2ºtabela
    conn = BDConnection.Connection()
    queryConsultResult =conn.query("SELECT * FROM unidade WHERE nome='{0}'".format(name))
    if queryConsultResult == []: #Caso a busca retorne nula, fará uma inserção, isso evita repetição de dados
        if conn.insert("INSERT INTO unidade(nome,cnpj,bairro,cep) VALUES ('{0}','{1}','{2}','{3}')".format(name,cnpj,district,cep)): #Insere nome da unidade{0},cnpj{1},bairro{2},cep{3}
            print("Cnpj ",cnpj," inserida\n")
            print("Cep ",cep," inserida\n")
            print("Bairro",district,"inserido\n")
            unity = conn.query("SELECT MAX(id_unidade) FROM unidade")  #Pega o ID da unidade
            unity = unity[0][0] #formata o ID do tipo tupla para o tipo inteiro
            if insertCityToUnity(city,unity,uf): #chama o método da relação com os argumentos das PK
                print("Unidade inserida e associação concluída\n")
        
#Método para inserir a 1º relação           
def insertCityToUnity(city,unity,uf):
    conn = BDConnection.Connection()
    
    if conn.insert("INSERT INTO pertenceCit_Unid(nomeFK,ufFK,id_unidadeFK) VALUES ('{0}','{1}','{2}') ".format(city,uf,unity)): #Insere as FKs na tabela de relação
        return True
                  

#Método para inserir a 3º tabela
def insertProduct(tipo,price,data,flag,unity): #Recebe argumentos do CSV das linhas do tipo,preço,data,bandeira e (unidade)-> Serve oara fazer a relação entre a 3º tabela e a 4º tabela 
    conn = BDConnection.Connection()
    price = price.replace(',','.') #Redefine a vírgula e colocando um ponto, podendo ser identificado como DOUBLE

    if conn.insert("INSERT INTO produto(tipo,valor_venda,data_coleta,bandeira) VALUES ('{0}','{1}','{2}','{3}')".format(tipo,price,data,flag)): #Insere tipo{0},valor_venda{1},data_coleta{2},bandeira{3}
        print("Tipo de combustível ",tipo," inserida\n")
        print("Valor da venda ",price," inserida\n")
        print("Data da coleta ",data," inserida\n")   
        print("Bandeira ",flag," inserida\n")   
    
    idArray=conn.query("SELECT MAX(id_produto) FROM produto") #Seleciona o ID do produto
    id=idArray[0][0] #formata o ID do tipo tupla para o tipo inteiro, fazendo com que UMA unidade possua 3 tipos de produto através das FK, inserção de ID manual
    if insertProdToUnity(id,unity): #Chama o método da relação com os argumentos da PK
        print("Produto inserido e relação completada")

#Método para inserir a 2º relação  
def insertProdToUnity(id,unity):
    conn = BDConnection.Connection()
    id_unidade =conn.query("SELECT id_unidade FROM unidade WHERE nome='{0}'".format(unity)) #Seleciona o ID do produto
    id_unidade=id_unidade[0][0] #formata o ID do tipo tupla para o tipo inteiro
    if conn.insert("INSERT INTO contemProd_Unid(id_produtoFK,id_unidadeFK) VALUES ('{0}','{1}') ".format(id,id_unidade)): #Insere na tabela de relação as FKs
        return True


    
    
