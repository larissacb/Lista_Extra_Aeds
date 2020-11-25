from Tarefa import tarefa
from Pilha import pilha
#Bibliotecas usadas
import re
#-------------------------------------------------------------------------------
#Algumas variaveis e estruturas usadas
y = True
agenda = pilha()
tarefas = list()
pontuacao_ordenada=list()
ano_ordenado=list()
mes_ordenado=list()
dia_ordenado=list()
#-------------------------------------------------------------------------------
#Funcoes
def menu():
    print("====================================================")
    print('Menu')
    print('1 - Adicionar Tarefa')
    print('2 - Excluir Tarefa')
    print('3 - Informacoes da Tarefa')
    print('4 - Ordenar os dados em ordem crescente para pontuacao')
    print('5 - Ordenar as tarefas pela data de entrega')
    print('0 - Sair')
    print("====================================================")
    x = int(input('Digite um numero: '))
    print("====================================================")
    return x

def linha():
    print("====================================================")
#-------------------------------------------------------------------------------
#Loop
while y == True:  # loop
    x = menu()
    if x == 1: #Adicionar Tarefa
        #Validacao dos dados digitados pelo usuario
        aux = False
        titulo = input("Informe o titulo: ")
        materia = input("Informe a materia: ")
        while (aux == False):
            dia = input("Informe o dia: ")
            if (re.findall('[0-9]+', dia)):
                aux = True
            else:
                print("Dado invalido. Digite novamente")
        aux = False
        while (aux == False):
            mes = input("Informe o mes: ")
            if (re.findall('[0-9]+', mes)):
                aux = True
            else:
                print("Dado invalido. Digite novamente")
        aux = False
        while (aux == False):
            ano = input("Informe o ano: ")
            if (re.findall('[0-9]+', ano)):
                aux = True
            else:
                print("Dado invalido. Digite novamente")
        aux = False
        while (aux == False):
            pontuacao = input("Informe a pontuacao: ")
            if (re.findall('[0-9.]+', pontuacao)):
                aux = True
            else:
                print("Dado invalido. Digite novamente")
        linha()
        a = tarefa(titulo, materia, int(dia), int(mes), int(ano), float(pontuacao))  # cria um objeto do tipo tarefa
        agenda.empilha(a) #adiciona o item no inicio da pilha
        
    elif x == 2: #Excluir Tarefa        
        agenda.desempilha() #remove o item do inicio da pilha
        linha()
        
    elif x == 3: #Informacoes da Tarefa
        k = int(input('Digite o numero da Tarefa: '))  # tenho que converter o numero para inteiro pq ele fica salvo como string
        k -= 1  # considero que o usuario digita o numero da tarefa ignorando a posicao 0
        agenda.getPosicao(k).imprimir()
        linha()
        
    elif x == 4:  #Ordenar os dados em ordem crescente para pontuacao
        for i in range(agenda.getTamanho()): #nao encontrei outra forma mais eficiente para realizar a ordenacao
            tarefas.append(agenda.getPosicao(i))
        i=0
        pontuacao_ordenada=sorted(tarefas, key=tarefa.getPonto) #ordenando as tarefas pela pontuacao
        print("\nImprimindo as tarefas em ordem crescente de acordo com a pontuacao...")
        for i in range(len(pontuacao_ordenada)):
            pontuacao_ordenada[i].imprimir()
            linha()
        tarefas.clear() #limpa a lista tarefas
        pontuacao_ordenada.clear() #limpa a lista de pontuacao ordenada
        
    elif x == 5:  #Ordenar as tarefas pela data de entrega
        i=0
        for i in range(agenda.getTamanho()): #nao encontrei outra forma mais eficiente para realizar a ordenacao
            tarefas.append(agenda.getPosicao(i))
        i=0
        dia_ordenado=sorted(tarefas, key=tarefa.getDia) #ordenando o dia a partir da lista 'tarefas'
        mes_ordenado=sorted(dia_ordenado, key=tarefa.getMes) #ordenando o mes a partir da lista 'dia_ordenado'
        ano_ordenado=sorted(mes_ordenado, key=tarefa.getAno) #ordenando o ano a partir da lista 'mes_ordenado'
        print("\nImprimindo as tarefas em ordem crescente de acordo com a data de entrega...")
        for i in range(len(ano_ordenado)):
            ano_ordenado[i].imprimir()
        tarefas.clear() #limpa a lista de tarefas
        ano_ordenado.clear() #limpa a lista de ano ordenado
        mes_ordenado.clear() #limpa a lista de mes ordenado
        dia_ordenado.clear() #limpa a lista de dia ordenado
        
    elif x == 0: #Sair
        agenda.FPVazia() #limpa a pilha
        break #interrompe o loop
    
    else: print("Opcao invalida. Digite novamente")
