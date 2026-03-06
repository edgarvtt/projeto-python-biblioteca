import models 

## SECÇÃO DE TESTES 
## 1. Crie 2 livros

LivroA = models.Livro("A revolução dos Bichos","George O.",2)
LivroB = models.Livro("O pequeno Principe","Autor",2)

## 2. Crie 1 Usuário

UsuarioA = models.Usuario("Edgar vitor")
UsuarioB = models.Usuario("Victorino")
UsuarioC = models.Usuario("VictorinA")

UsuarioA.pegar_livro(LivroA.titulo)
print(LivroA.quantidade) 
LivroA.emprestar_para(UsuarioA.nome) ## com o menu e condições, ao pegar livro X, o método do livro 'emprestado_para' funciona
print(LivroA.quantidade) ##diminui a quantidade 1x
LivroA.emprestar_para(UsuarioB.nome) ## com o menu e condições, ao pegar livro X, o método do livro 'emprestado_para' funciona
print(LivroA.quantidade) ##diminui a quantidade 2x
LivroA.emprestar_para(UsuarioC.nome) ## com o menu e condições, ao pegar livro X, o método do livro 'emprestado_para' funciona
print(LivroA.quantidade) ##diminui a quantidade 3x

## 3. para devolver

##UsuarioA.devolver_livro(LivroA.titulo)
##LivroA.devolver()

## 3. imprimir informações

print(LivroA)
print(UsuarioA) 
print(UsuarioA.livros_emprestados)
