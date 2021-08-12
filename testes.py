from conjuntos import Conjunto

## Teste tamanho
A = Conjunto(1, 2, 3, 4, 5)
print(A.tamanho()) # saída é: 5

## Teste possui
A = Conjunto(1, 2, 3, 4)
B = Conjunto(1, 2, A)
print(A.possui(3)) # saída é: True
print(A.possui(10)) # saída é: False
print(B.possui(A)) # saída é: True

## Teste contem
A = Conjunto(1, 2)
B = Conjunto(1, 2, 3, 4)
C = Conjunto(5, 6, 7)
print(A.contem(A)) # saída é: True
print(B.contem(A)) # saída é: True
print(C.contem(A)) # saída é: False

