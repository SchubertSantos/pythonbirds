class Pessoa:
    def __init__(self, *filhos, nome=None, idade=37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos) #Atributo Complexo

    def cumprimetar(self):   #Metodo de instância.
        return f'Olá {id(self)}'

    @staticmethod #Metodo Estatico ou decorator
    def metodo_estatico():
        return 42

    @classmethod #Metodo de classe ou decorator de classe.
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    beethoven.olhos = 1
    del beethoven.olhos
    print(beethoven.__dict__) #Atributo de instancia de um objeto __dict__
    print(schubert.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(beethoven.olhos)
    print(schubert.olhos)
    print(id(Pessoa.olhos), id(beethoven.olhos), id(beethoven.olhos))
    print(Pessoa.metodo_estatico(), beethoven.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), beethoven.nome_e_atributos_de_classe())