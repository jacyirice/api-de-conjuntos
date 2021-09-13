# API de conjuntos

# 🏁 Indice

- [Sobre](#-sobre)
- [Features](#-features)
- [Tecnologias Utilizadas](#%EF%B8%8F-tecnologias-utilizadas)
- [Como baixar o projeto](#-como-baixar-o-projeto)
- [Exemplos de Utilização](#exemplos-de-utilização)
- [Desenvolvedores](#desenvolvido-por)

## 🔖&nbsp; Sobre
A API de conjuntos foi desenvolvida a fim de operações relacionadas a Teoria de Conjuntos.

---

## 🚀 Features
- [x] Conjunto universo
- [x] Tamanho
- [x] Possui
- [x] Contém
- [x] Contém propriamente
- [x] É igual
- [x] É vazio
- [x] União
- [x] Interseção
- [x] Diferença
- [x] Complemento
- [x] Conjunto das partes
- [x] Produto cartesiano
- [x] to_string

---
## ⚒️ Tecnologias utilizadas

O projeto foi desenvolvido utilizando a seguinte tecnologia

- [Python](https://python.org)

---

## 🗂 Como baixar o projeto

```bash

    # Clonar o repositório
    $ git clone https://github.com/jacyirice/api-de-conjuntos

    # Entrar no diretório
    $ cd api-de-conjuntos

    # Executar testes
    $ python -m unittest discover testes -v
```
## Exemplos de Utilização
- Formas de instanciar um conjunto

    ```python
    # Importar API
    from conjuntos import Conjunto
    
    # Conjunto vazio
    A = Conjunto()

    # Conjunto a partir de lista
    B = Conjunto([1, 2, 'A', '1'])

    # Conjunto com um ou mais elementos
    C = Conjunto(1, 2, 'A', '1')
    ```
- Relação de pertinência

    ```python
    # Conjunto exemplo
    A = Conjunto(1, 2, 3, 4)

    # Verificando se o elemento e pertence ao conjunto
    print(A.possui(3)) # saída é: True
    ```
- Relação de subconjunto
    ```python
    # Conjuntos exemplos
    A = Conjunto(1, 2)
    B = Conjunto(1, 2, 3, 4)

    # Verificando se o conjunto-argumento B pertence ao conjunto-instância A
    print(B.contem(A)) # saída é: True
    ```
- Relação de subconjunto próprio
    ```python
    # Conjuntos exemplos
    A = Conjunto(1, 2, 3)
    B = Conjunto(1, 2)

    # Verificando se o conjunto-argumento B pertence propriamente ao conjunto-instância A
    print(B.contem_propriamente(A)) # saída é: False
    ```
- União entre dois conjuntos
    ```python
    # Conjuntos exemplos
    A = Conjunto(1, 2)
    B = Conjunto(1, 2, 3)

    # Uniao de A e B
    C = A.uniao(B) # um novo conjunto com os elementos: 1, 2, 3    
    ```
- Interseção entre dois conjuntos
    ```python
    # Conjuntos exemplos
    A = Conjunto(1, 2)
    B = Conjunto(2, 3, 4)

    # Interseção de A com B
    C = A.intersecao(B) # um novo conjunto com o elemento: 2
    ```
- Complemento de um conjunto
    ```python
    # Conjuntos exemplos
    U = Conjunto(1, 2, 3, 4, 5)
    A = Conjunto(1, 2)

    # Complemento de A em referência a U
    C = A.complemento(U) # um novo conjunto com os elementos: 3, 4, 5
    ```
- Diferença entre dois conjuntos
    ```python
    # Conjuntos exemplos
    A = Conjunto(1, 2, 3)
    B = Conjunto(1, 4)

    # Diferença de A e B (A-B)
    C = A.diferenca(B) # um novo conjunto com os elementos: 2, 3    
    ```
- Conjunto das partes de um conjunto
    ```python
    # Conjunto exemplo
    A = Conjunto(1, 2, 3)
    
    # Conjunto das partes de A
    P = A.conjunto_das_partes() 
    # P é um novo conjunto com os elementos:
    # Conjunto(), 
    # Conjunto(1), Conjunto(2), Conjunto(3), 
    # Conjunto(1, 2), Conjunto(1, 3), Conjunto(2, 3), 
    # Conjunto(1, 2, 3)
    ```
- Produto cartesiano de um conjunto
    ```python
    # Conjunto exemplo
    A = Conjunto(1, 2, 3)
    B = Conjunto(4, 5, 6)
    
    # Produto cartesiano de A e B
    P = A.produto_cartesiano(B) 
    # P é um novo conjunto com os elementos:
    # (1, 4), (1, 5), (1, 6)
    # (2, 4), (2, 5), (2, 6)
    # (3, 4), (3, 5), (3, 6)
    ```
- Saída textual (string) representando o conjunto
    ```python
    # Conjunto exemplo
    A = Conjunto(1, 2, 3)
    B = Conjunto(1, A)
    C = Conjunto()
    D = Conjunto(A, B, C)

    #Obtendo representação em string do conjunto D
    print(D) # a saída é: {{1, 2, 3}, {1, {1, 2, 3}}, {}}
    
    # OU
    print(D.string()) # a saída é: {{1, 2, 3}, {1, {1, 2, 3}}, {}}

    ```
---

## Desenvolvido por
[Jacyiricê Silva Oliveira](https://github.com/jacyirice/)

[Rayanna Quirino](https://github.com/rayannaQuirino/)

## Disponivel em 
[GitHub](https://github.com/jacyirice/api-de-conjuntos)