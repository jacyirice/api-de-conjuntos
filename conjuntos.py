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
    '''
    Classe criada para representar um conjunto e suas caracteristicas
    '''

    def __init__(self, *args):
        '''
        Inicializa um objeto da classe Conjunto.

        Exemplo:
        - C = Conjunto(1, 2, 3)
        '''
        if len(args) == 0:
            self.elementos = ()
        elif isinstance(args[0], list):
            self.elementos = tuple(args[0])
        else:
            self.elementos = args

        self.elementos = sorted(self.elementos, key=lambda x: str(x))
        # Cria um alias para o metodo __str__, conforme documentação.
        self.string = self.__str__

    def conjunto_universo(*args):
        '''
        Retorna o conjunto universo dos conjuntos passados como argumentos.

        Exemplo:
        - A = Conjunto(1, 2, 3)
        - B = Conjunto('a', 'b', 'c')
        - print(Conjunto.conjunto_universo(A,B))

        Saída:
        - {1, 2, 3, a, b, c}
        '''
        u = Conjunto()
        for i in args:
            u = u.uniao(i)
        return u

    def tamanho(self):
        '''
        Retorna a quantidade de elementos no conjunto.

        Exemplo:
        - C = Conjunto(1, 2, 3)
        - print(C.tamanho())

        Saída:
        - 3
        '''
        return len(self.elementos)

    def possui(self, e):
        '''
        Retorna um booleano indicando se o elemento e pertence ao conjunto.

        Exemplo:
        - C = Conjunto(1, 2, 3)
        - print(C.possui(6))

        Saída:
        - False
        '''
        return e in self.elementos

    def contem(self, b):
        '''
        Retorna um booleano indicando se o conjunto-argumento B pertence ao conjunto-instância.

        Exemplo:
        - A = Conjunto(1, 2)
        - B = Conjunto(1, 2, 3, 4)
        - print(B.contem(A))

        Saída:
        - True
        '''
        for i in b.elementos:
            if i not in self.elementos:
                return False
        return True

    def contem_propriamente(self, b):
        '''
        Retorna um booleano indicando se o conjunto-argumento B pertence propriamente ao conjunto-instância A.

        Exemplo:
        - A = Conjunto(1, 2, 3)
        - B = Conjunto(1, 2)
        - print(B.contem_propriamente(A))

        Saída:
        - False
        '''
        if self.eh_igual(b):
            return False
        return self.contem(b)

    def eh_igual(self, b):
        '''
        Retorna um booleano indicando se o conjunto-instância é igual ao conjunto-argumento B.

        Exemplo:
        - A = Conjunto(1, 2)
        - B = Conjunto(1, 2)
        - print(A.eh_igual(B))

        Saída:
        - True
        '''
        if b.elementos != self.elementos:
            return False
        return True

    def eh_vazio(self):
        '''
        Retorna  um booleano indicando se o conjunto-instância A é vazio.

        Exemplo:
        - A = Conjunto()
        - print(A.eh_vazio())

        Saída:
        - True
        '''
        return self.tamanho() == 0

    def uniao(self, b):
        '''
        Retorna um conjunto contendo elementos dos dois conjuntos,
        o conjunto-instância e o conjunto-argumento B, sem repetições.

        Exemplo:
        - A = Conjunto(1, 2)
        - B = Conjunto(1, 2, 3)
        - print(A.uniao(B))

        Saída:
        - {1, 2, 3}
        '''
        aux = []
        for i in b.elementos:
            if i not in self.elementos:
                aux.append(i)
        aux.extend(self.elementos)
        return Conjunto(aux)

    def intersecao(self, b):
        '''
        Retorna um conjunto contendo elementos que pertencem aos 
        dois conjuntos ao mesmo tempo, o conjunto-instância e 
        o conjunto-argumento B, sem repetições.

        Exemplo:
        - A = Conjunto(1, 2)
        - B = Conjunto(2, 3, 4)
        - print(A.intersecao(B))

        Saída:
        - {2}
        '''
        aux = []
        for i in b.elementos:
            if i in self.elementos:
                aux.append(i)
        return Conjunto(aux)

    def diferenca(self, b):
        '''
        Retorna um conjunto contendo elementos que pertencem
        ao conjunto-instância, mas não pertencem ao 
        conjunto-argumento B.

        Exemplo:
        - A = Conjunto(1, 2, 3)
        - B = Conjunto(1, 4)
        - print(A.diferenca(B))

        Saída:
        - {2, 3}
        '''
        aux = []
        for i in self.elementos:
            if i not in b.elementos:
                aux.append(i)
        return Conjunto(aux)

    def complemento(self, u):
        '''
        Retorna um conjunto que representa o complemento 
        do conjunto-instância em referência ao 
        conjunto-argumento U (o conjunto universo).

        Exemplo:
        - U = Conjunto(1, 2, 3, 4, 5)
        - A = Conjunto(1, 2)
        - print(A.complemento(U))

        Saída:
        - {3, 4, 5}
        '''
        aux = []
        for i in u.elementos:
            if i not in self.elementos:
                aux.append(i)
        return Conjunto(aux)

    def conjunto_das_partes(self):
        '''
        Retorna um conjunto que contém todos os subconjuntos do conjunto-instância.

        Exemplo:
        - A = Conjunto(1, 2, 3)
        - print(A.conjunto_das_partes())

        Saída:
        - {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
        '''
        elementos = self.elementos
        aux = [Conjunto()]

        tam = self.tamanho()
        if tam > 0:
            aux.append(Conjunto(elementos))
                
            if tam > 1:
                for i in elementos:
                    aux.append(Conjunto(i))

                if tam > 2:
                    for i in range(len(elementos)-1):
                        for j in elementos[i+1:]:
                            aux.append(Conjunto(elementos[i], j))
        return Conjunto(aux)

    def produto_cartesiano(self, b):
        '''
        Retorna um conjunto que contém tuplas compostas por 
        elementos do conjunto-instância e do conjunto-argumento B.

        Exemplo:
        - A = Conjunto(1, 2, 3)
        - B = Conjunto(4, 5, 6)
        - print(A.produto_cartesiano(B))

        Saída:
        - {(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)}
        '''
        aux = []
        for i in self.elementos:
            for j in b.elementos:
                aux.append((i, j))
        return Conjunto(aux)

    def __str__(self):
        '''
        Formata os elementos do conjunto e retorna uma string.

        Exemplo:
        - C = Conjunto(1, 2, 3)
        - print(C)

        Retorno:
        - {1, 2, 3}
        '''
        aux = '{'
        for i in self.elementos:
            if isinstance(i, tuple):
                aux += to_string_tupla(i)
            else:
                aux += f'{i}, '
        return remove_virgula(aux, end='}')
