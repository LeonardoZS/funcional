#Leonardo Zaniboni Silva 11801049
fibo = lambda x: fibo(x-1) + fibo(x-2) if x>=2 else 1       #Função 'anonima' Fibonacci
fato = lambda y: y * fato(y-1) if y>=2 else 1               #Função 'anonima' Fatorial
lista_x = [] ; lista_y = []                                 #Declaração da lista x e y
with open("input.dat") as input: caracteres = input.read()  #Abrindo o arquivo de input e lendo os dados
for i in range(len(caracteres)) :
    if caracteres[i] == ',' or caracteres[i] == ' ' : 
        lista_x.append(caracteres[i-1] )                    #Adicionando os valores que serão calculados no Fibonacci 
        lista_y.append(caracteres[i+1])                     #Adicionando os valores que serão calculados no Fatorial 
with open("output.dat",'w') as output:                      #Abrindo o arquivo de output
    output.write("".join(list((map(lambda i,x,y: f"Linha {i+1} : Fibo({x}) =  {fibo(int(x))} Fact({y}) = {fato(int(y))} \n", range(0,len(lista_x)), lista_x, lista_y)))))
# Este programa faz uso de duas funções anônimas. Declarou elas inicialmente para uma melhor legibilidade no código.
# Além disso, utilizou-se a função map() para iterar em todos os itens na hora de escrever no arquivo final.
