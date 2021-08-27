class Conjunto:
    def __init__(self, *args):
        if len(args) == 0:
            self.elementos = ()
        elif type(args[0]) == list:
            self.elementos = tuple(args[0])
        elif type(args[0]) == Conjunto:
            self.elementos = args[0].elementos
        else:
            self.elementos = args
            
        self.elementos = sorted(self.elementos, key=lambda x: str(x))
        
    def tamanho(self):
        return len(self.elementos)

    def possui(self, e):
        return e in self.elementos

    def contem(self, b):
        for i in b.elementos:
            if i not in self.elementos:
                return False
        return True

    def contem_propriamente(self, b):
        if self.eh_igual(b):
            return False
        return self.contem(b)

    def eh_igual(self, b):
        if b.elementos != self.elementos:
            return False
        return True

    def eh_vazio(self):
        return self.tamanho() == 0

    def uniao(self,b):
        aux = []
        for i in b.elementos:
            if i not in self.elementos:
                aux.append(i)
        aux.extend(self.elementos)
        return Conjunto(aux)
    
    def intersecao(self,b):
        aux = []
        for i in b.elementos:
            if i in self.elementos:
                aux.append(i)
        return Conjunto(aux)
    
    def diferenca(self,b):
        aux = []
        for i in self.elementos:
            if i not in b.elementos:
                aux.append(i)
        return Conjunto(aux)