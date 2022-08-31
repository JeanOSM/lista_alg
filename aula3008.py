#bolha cria a variavel de controle para não perder os valores. percorre ate n-1 ou vetor -1

""" vetor = [10, 30, 5, 2, 15, 8]


for j in range(0, len(vetor)-1):
    for i in range (0,len(vetor)-1):
        if(vetor[i]>vetor[i+1]):
            controle = vetor[i]
            vetor[i]=[i+1] 
            vetor[i+1]= controle


    10, 30, 5, 2, 15, 8
    10, 5, 30, 2, 15, 8
    10, 5, 2, 30, 15, 8
    10, 5, 2, 15, 30, 8
    10, 5, 2, 15, 8, 30

    5, 10, 2, 15, 8, 30
    5, 2, 10, 15, 8, 30
    5, 2, 10, 8, 15, 30
    5, 2, 10, 8, 15, 30
    2, 5, 10, 8, 15, 30
    2, 5, 8, 10, 15, 30
#------------------------------------------


#Seleção troca o valor, o menor com o maior. percorre ate n-1 ou vetor -1
10,30,5,2,15,8

2,30,5,10,15,8
2,5,30,10,15,8
2,5,8,10,15,30

for i in range (0,len(vetor)-1):
    menor= vetor[i]
    posicaoMenor=[i]
    for j in range(i+1,len(vetor)):
        if (menor>vetor[j]):
            menor = vetor[j]
            posicaoMenor = j 
    controle = vetor[i]
    vetor[i] = menor
    vetor[posicaoMenor] = controle


#-------------------------------------------------


#inserção encontra o menor numero e compara com o aonterior.


10,30,5,2,15,8

5,10,30,2,15,8
2,5,10,30,15,8
2,5,10,30,15,8
2,5,10,15,30,8
2,5,8,10,15,30


for i in range (1, len(vetor)):
    valoratual = vetor[i]
    posicaovalor = i-1
    while (posicaovalor>=0 and vetor[posicaovalor]>valoratual ):

        vetor[posicaovalor+1]= vetor[posicaovalor]

        posicaovalor=posicaovalor-1

        vetor[posicaovalor+1] = valoratual 




#busca sequencial ou busca linear (Ordenados ou nao )

valorper = 4
i_valor = -1  #Numero referencia para entrar  no for. sendo diferente dos possiveis.
for i in range (0,len(vetor)):
    if (vetor[i]==valorper):
        i_valor = i 
        break
if(i_valor>=0):
    print(valorper , "esta no vetor.")
    print("Esta na posição" , i_valor )
else:
    print("Não esta no vetor.")




#Busca binaria (Precisa esta ordenado, precisa do inicio, meio e fim.
# testar o valor do meio, se tiver pra frente do meio, o inicio é ,meio +1. menor que o meio, o fim é meio -1.)
# O vetor deve estar ordenado
# 3 variaveis de controle 
#O (log² (n)) Na base para saber a quantidade de testes.  """


vetor = [1,3,5,7,9,11,13,15,17,19]
valor = 3
inicio = 0 

fim = len(vetor)-1
meio = int((inicio + fim)/2) 

while(inicio<=fim):
    meio = int((inicio + fim)/2)
    if(valor[meio]==valor):
        inicioValor = meio
        break
    elif (valor> vetor[meio] ):
        inicio = meio+1
    else :
        fim = meio -1
if (inicioValor>=0):
    print("Achou!")
else:
    print ("Não achou!")
































