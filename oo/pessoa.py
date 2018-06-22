class Pessoa:
    def __init__(self, *filhos, nome=None, idade=37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos) #Atributo Complexo

    def cumprimetar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    schubert = Pessoa(nome='Schubert')
    beethoven = Pessoa(schubert,nome='Beethoven')
    print(Pessoa.cumprimetar(beethoven))
    print(id(beethoven))
    print(beethoven.cumprimetar())
    print(beethoven.nome)
    print(beethoven.idade)
    for filho in beethoven.filhos:
        print(filho.nome)
    beethoven.sobrenome = 'Santos' #Atributo Dinamico
    del beethoven.filhos #Deletando um atributo
    print(beethoven.__dict__) #Atributo de instancia __dict__
    print(schubert.__dict__)