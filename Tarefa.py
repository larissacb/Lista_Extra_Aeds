class tarefa :

    def __init__(self,nome,materia,dia,mes,ano,ponto): #Construtor da classe
        self.nome = nome
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.ponto = ponto
        self.materia = materia

    def getNome(self): #Retorna a variavel nome
        return self.nome

    def getDia(self): #Retorna a variavel dia
        return self.dia

    def getMes(self): #Retorna a variavel mes
        return self.mes

    def getAno(self): #Retorna a variavel ano
        return self.ano

    def getPonto(self): #Retorna a variavel de pontuacao
        return self.ponto

    def getMateria(self): #Retorna a variavel disciplina/materia
        return self.materia

    def imprimir(self):
        print("====================================================")
        print('Titulo :', self.nome)
        print('Materia :', self.materia)
        print('Pontuacao :', self.ponto)
        print('Data :', self.dia,'/', self.mes,'/', self.ano)
        print("====================================================")
