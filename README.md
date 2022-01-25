# Bot de Inserção de Dados :robot:

Um programa feito em linguagem PYTHON:snake: que realiza automaticamente inserções de dados em um banco POSTGRES:elephant:, usando como base um arquivo .CSV:file_folder:,
útil em inserções de dados em massa.

Na criação do bot foi utilizado 4 arquivos nomeados de:  
:diamonds:**BDConnection.py** necessário para a conexão com o Banco de Dados.  
:diamonds:**insertCSVData.py** para a abertura e leitura do arquivo .CSV  
:diamonds:**insertQuerys.py** para realizar a inserção dos dados em cada tabela.  
:diamonds:**main.py** para realizar a inserção dos dados em cada tabela. 
   

## Como utilizar o bot:

:sparkle:1º - Defina a conexão com o banco no arquivo **BDConnection.py**,inserindo o host,banco,usuário e a senha: 

![giphy](https://media.giphy.com/media/m5aF90izLPCw08wQdM/giphy.gif)    


:sparkle:2º - Agora faça métodos semelhantes para cada tabela do seu Banco de Dados no arquivo **insertQuerys.py**, onde os argumentos deverão ser cada atributo da sua tabela, após isso altere os .format() de acordo com  necessário:

![giphy](https://media.giphy.com/media/OnHNIDeQYBXebsU71q/giphy.gif)   


:sparkle:3º - No mesmo arquivo **insertQuerys.py**, faça métodos para as relações entre tabelas. pegando suas ID, definindo-as como FK, lembre-se de sempre que terminar duas tabelas relacionadas, fazer a sua relação:

![giphy](https://media.giphy.com/media/vROXjzMywIrwNefOSo/giphy.gif)

:sparkle:4º - Por fim, no arquivo **insertCSVData.py***, adicione os métodos criados em **insertQuerys.py** e em seguida adicione os parâmetros de acordo com cada coluna do .CSV:

![giphy](https://media.giphy.com/media/rJyNB1szJ4BSeGHbBt/giphy.gif)

## Conclusão

Créditos para:  
  -:diamond_shape_with_a_dot_inside:Davi Galdino de Oliveira Souza  
  -:diamond_shape_with_a_dot_inside:[João Vitor Oliveira Correia](https://github.com/correavitor4)  

Extensão usada:  
:high_brightness:[Identificador de colunas de arquivos .CSV no VSCode](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)
