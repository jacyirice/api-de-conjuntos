# Alunos: Jacyiricê e Rayanna

def remove_virgula(s, end=''):
    if s.endswith(', '):
        s = s[:-2]
    return s+end


def to_string_tupla(i):
    aux1 = '('
    for j in i:
        aux1 += f'{j}, '
    return remove_virgula(aux1, end='), ')


class Conjunto:
    def __init__(self, *args):
        if len(args) == 0:
            self.elementos = ()
        elif type(args[0]) == list:
            self.elementos = tuple(args[0])
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

    def uniao(self, b):
        aux = []
        for i in b.elementos:
            if i not in self.elementos:
                aux.append(i)
        aux.extend(self.elementos)
        return Conjunto(aux)

    def intersecao(self, b):
        aux = []
        for i in b.elementos:
            if i in self.elementos:
                aux.append(i)
        return Conjunto(aux)

    def diferenca(self, b):
        aux = []
        for i in self.elementos:
            if i not in b.elementos:
                aux.append(i)
        return Conjunto(aux)

    def complemento(self, u):
        aux = []
        for i in u.elementos:
            if i not in self.elementos:
                aux.append(i)
        return Conjunto(aux)

    def conjunto_das_partes(self):
        elementos = self.elementos
        aux = [Conjunto()]

        for i in elementos:
            aux.append(Conjunto(i))

        for i in range(len(elementos)-1):
            for j in elementos[i+1:]:
                aux.append(Conjunto(elementos[i], j))

        aux.append(Conjunto(elementos))
        return Conjunto(aux)

    def produto_cartesiano(self, b):
        aux = []
        for i in self.elementos:
            for j in b.elementos:
                aux.append((i, j))
        return Conjunto(aux)

    def string(self):
        return str(self)

    def __str__(self):
        aux = '{'
        for i in self.elementos:
            if type(i) == tuple:
                aux += to_string_tupla(i)
            else:
                aux += f'{i}, '
        return remove_virgula(aux, end='}')
