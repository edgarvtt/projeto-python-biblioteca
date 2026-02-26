from datetime import datetime 

## Classe Livros:

class Livros:

    def __init__(self,titulo,autor,disponivel = True, data_emprestimo = None, data_devolucao = None):

        self.titulo = titulo 
        self.autor = autor
        self.disponivel = disponivel
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

    def emprestar_para(self,name):

        if self.disponivel != False:

            self.data_emprestimo = datetime.now(); ## altera para a data que foi emprestado o livro
            self.disponivel = False;
        
        else:
            print("Este Livro já foi emprestado, por favor tente outro livro")

        print(f"Empréstimo confirmado para {name}")

        return 0
    
    def devolver(self):

        if self.disponivel == False:

            self.disponivel = True
            self.data_devolucao = datetime.now()
        
        else:

            print("este livro não recebeu emprestimos ativo no momento")
        
        print(f"devolveu o livro às {datetime.now()}")

        return 0
    
    def __str__(self):

        return f"o livro '{self.titulo}' do autor {self.autor} está como {self.disponivel} , \nhouve empréstimo de {self.data_emprestimo} até {self.data_devolucao}"
    
## LivroA = Livros("A revolução dos Bichos","George O.")
## LivroA.emprestar_para("Joana");
## LivroA.devolver();
## print(LivroA)
## livro A: (a vida , monteil)
## Livro.emprestar()
## Livro.devolver() --> vai fazer a mesma operação só que invertendo os valores de disponível + colocar a hora da devolução

class Usuario:

    def __init__(self,nome,livros_emprestados = []):

        self.nome = nome.strip().title();
        self.livros_emprestados = livros_emprestados
    
    def pegar_livro(self,livro):

        self.livros_emprestados.append(livro)
        self.livros_emprestados = list(map(lambda x: x.lower().strip(),self.livros_emprestados))

    def devolver_livro(self,livro):

        try:

            livro = livro.lower().strip()
            self.livros_emprestados.remove(livro)
            

        except: 

            print("o livro a ser removido não existe, tente novamente com base nos emprestimos feitos")
            print(self.livros_emprestados)
            print("tente novamente")

    def __str__(self):

        return f"o usuario {self.nome} tem a seguinte lista de livros pego como emprestimo {self.livros_emprestados}"
    
""" usuarioA = Usuario("edgar vitor")
usuarioA.pegar_livro("O pequeno Principe")
usuarioA.pegar_livro("Scooby-Doo") 

usuarioA.devolver_livro(" o Pequeno PrinCipe")

print(usuarioA)  """