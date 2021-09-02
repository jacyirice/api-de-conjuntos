'''
Considere os conjuntos:   e o conjunto universo U que é definido pela união 
dentre os demais conjuntos, ou seja, .
Utilizando a API de Conjuntos resolva as questões a seguir:

'''
from conjuntos import Conjunto
A = Conjunto(1, 2, 3)
B = Conjunto('a', 'b', 'c')
C = Conjunto(1, 2, 4, 5)
D = Conjunto(A, 1, 2)
E = Conjunto(B, C)

# Conjunto universo
U = A.uniao(B)
for i in [C, D, E]:
    U = U.uniao(i)
print('Conjunto universo: ', U)

# Questão 1
u1 = A.uniao(B)
R = u1.uniao(C)
print('Questao 1: ', R)
# Resultado: {1, 2, 3, 4, 5, a, b, c}

# Questão 2
R = A.intersecao(C)
print('Questao 2: ', R)
# Resultado: {1, 2}

# Questão 3
R = A.complemento(U)
print('Questao 3: ', R)

# Questão 4
r1 = B.uniao(D)
R = r1.complemento(U)
print('Questao 4: ', R)

# Questão 5
R = A.intersecao(C)
print('Questao 5: ', R)
# Resultado: {1, 2}

# Questão 6
R = C.diferenca(A)
print('Questao 6: ', R)
# Resultado: {4, 5}

# Questao 7
R = C.contem(A)
print('Questao 7: ', R)
# Resultado: False

# Questao 8
R = C.contem_propriamente(A)
print('Questao 8: ', R)
# Resultado: False

# Questao 9
R = A.eh_igual(C)
print('Questao 9: ', R)
# Resultado: False

# Questao 10
R = B.conjunto_das_partes()
print('Questao 10: ', R)
# Resultado: {{a, b, c}, {a, b}, {a, c}, {a}, {b, c}, {b}, {c}, {}}

# Questao 11
R = D.conjunto_das_partes()
print('Questao 11: ', R)
# Resultado: {{1, 2, {1, 2, 3}}, {1, 2}, {1, {1, 2, 3}}, {1}, {2, {1, 2, 3}}, {2}, {{1, 2, 3}}, {}}

# Questao 12
R = A.produto_cartesiano(B)
print('Questao 12: ', R)
# Resultado: {(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')}

# Questao 13
R = A.produto_cartesiano(E)
print('Questao 13: ', R)
# Resultado: {(1, {1, 2, 4, 5}), (1, {a, b, c}), (2, {1, 2, 4, 5}), (2, {a, b, c}), (3, {1, 2, 4, 5}), (3, {a, b, c})}
