class pilha:

    def __init__(self): #Construtor da classe
        self.items = list()
        
    def empilha(self, item): #Insere o item no topo da pilha
        self.items.insert(0,item)
    
    def desempilha(self): #Retorna o item no topo da pilha, retirando-o da pilha
        return self.items.pop(0)

    def getPosicao(self, posicao): #Retorna o item de uma determinada posicao
        return self.items[posicao]
    
    def getTamanho(self): #Retorna o numero de itens da pilha
        return len(self.items)
    
    def FPVazia(self): #Faz a pilha ficar vazia
        self.items.clear()
        
    def Vazia(self): #Retorna true se a pilha esta vazia; senao retorna false
        if(self.getTamanho() == 0): return True
        else: return False
