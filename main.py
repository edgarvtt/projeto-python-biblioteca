import models 

## 1. Crie 2 livros

LivroA = models.Livros("A revolução dos Bichos","George O.")
LivroB = models.Livros("O pequeno Principe","Autor")

## 2. Crie 1 Usuário

UsuarioA = models.Usuario("Edgar vitor")
UsuarioA.pegar_livro(LivroA.titulo)
LivroA.emprestar_para(UsuarioA.nome) ## com o menu e condições, ao pegar livro X, o método do livro 'emprestado_para' funciona

## 3. para devolver

UsuarioA.devolver_livro(LivroA.titulo)
LivroA.devolver()

## 3. imprimir informações

print(LivroA)
print(UsuarioA) 

