class fila:

    def __init__(self): #Construtor da classe
        self.items = list()
    
    def enfileira(self, item): #Insere o item no final da lista
        self.items.append(item)
        
    def desenfileira(self): #Retorna o item do inicio da fila, retirando-o da lista
        return self.items.pop()

    def getPosicao(self, posicao): #Retorna o item de uma determinada posicao
        return self.items[posicao]
    
    def getTamanho(self): #Retorna o tamanho da lista
        return len(self.items)
    
    def FFVazia(self): #Faz a fila ficar vazia
        self.items.clear()
        
    def Vazia(self): #Retorna true se a fila esta vazia; senao retorna false
        if(self.getTamanho() == 0): return True
        else: return False
   
