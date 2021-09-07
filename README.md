# API de conjuntos
## Sobre o app
A API de conjuntos foi desenvolvida a fim de operações relacionadas a Teoria de Conjuntos.
### Exemplos
```python
from conjuntos import Conjunto
A = Conjunto(1, 2, 3)
B = Conjunto('a', 'b', 'c')
C = Conjunto(1, 2, 4, 5)

U = Conjunto.conjunto_universo(A,B,C,D,E)
R = B.uniao(D).complemento(U)
print('Resultado: ', R) # Resultado: {3, 4, 5, {1, 2, 4, 5}, {a, b, c}}
```

## Funcionalidades
- [x] Tamanho


## Desenvolvido por
[Jacyiricê Silva Oliveira](https://github.com/jacyirice/)

[Rayanna Quirino](https://github.com/rayannaQuirino/)

## Disponivel em 
[GitHub](https://github.com/jacyirice/api-de-conjuntos)