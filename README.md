## Projeto Gerenciamento Biblioteca - Python 

Olá, este projeto decidi fazer para fortalecer meu desenvolvimento em aplicações com Python , Este projeto esta baseado nos requesitos para o Exam PCAP-31-0x do Python Institute, o que incluí basicamente: </br>

* Gerenciar Módulos , PIP & UV , Lambda , List Comprehension , Programação Orientada a Objetos (POO) , Interadores , Geradores , entre outros tópicos cátalogados com 'Intermédiario'
</br></br> está é a base para esse projeto, ao longo desse README.md colocarei mais sobre como o sistema funciona com base no aprendizado, já que não é um projeto além de didático

## Sumário: 

1. Classes </br>
1.1 Usuários </br>
1.2 Livros </br>
1.3 Conexão Usuários e Livros </br>

## 1. Classes 

### Usuários:

### Livro: 

ATRIBUTOS </br></br>
`titulo` - String  </br>
`autor` - String </br>
`disponivel` - Booleano </br>
`data_emprestimo` - Datatime </br>
`data_devolucao` - Datatime </br>
MÉTODOS </br></br>
`emprestar_para(self,name)` -- confirmação do empréstimo e mudando o estado de disponibilidade do livro </br>
`devolver(self)` -- ao acionar este método, o livro volta a ter uma unidade disponível 

### conexão Usuários e Livros
