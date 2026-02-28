from datetime import datetime 

## Classe Livros:

class Livro:

    def __init__(self,titulo,autor,disponivel = True, data_emprestimo = None, data_devolucao = None):

        self.titulo = titulo 
        self.autor = autor
        self.disponivel = disponivel
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

    def emprestar_para(self,name):

        if self.disponivel:

            self.data_emprestimo = datetime.now(); ## altera para a data que foi emprestado o livro
            self.disponivel = False;
            print(f"Empréstimo confirmado para {name}")

        
        else:
            print("Este Livro já foi emprestado, por favor tente outro livro")

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

        return f"o livro '{self.titulo}' do autor {self.autor} está disponivel ({self.disponivel}) , \nhouve empréstimo de {self.data_emprestimo} até {self.data_devolucao}"    
class Usuario:

    def __init__(self,nome,livros_emprestados = None):

        self.nome = nome.strip().title();
        self.livros_emprestados = [] if livros_emprestados is None else livros_emprestados
    
    def pegar_livro(self,livro):

        self.livros_emprestados.append(livro)
        self.livros_emprestados = list(map(lambda x: x.lower().strip(),self.livros_emprestados))

    def devolver_livro(self,livro):

        try:

            livro = livro.lower().strip()
            self.livros_emprestados.remove(livro)
            
        except Exception as e: 

            print("o livro a ser removido não existe, tente novamente com base nos emprestimos feitos")
            print(self.livros_emprestados)
            print("tente novamente")

    def __str__(self):

        return f"o usuario {self.nome} tem a seguinte lista de livros pego como emprestimo {self.livros_emprestados}"
    
