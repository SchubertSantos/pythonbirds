"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade.
2) Método acelerar, que deve incrementar a velocidade de uma unidade.
3) Método frear que deverá decrementar a velocidade de duas unidades.

A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar a direita.
3) Método girar a esquerda.

    N
  O   L
    S

    Exemplo:
    #Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> # Método "Frear" diminui em 2 unidades
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> # ao "Frear" novamente, o valor minino que posso chegar é " 0 "
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> #Testando Direção
    >>> motor.Direcao()
    >>> direcao.valor
    'Norte'
    >>> motor.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> motor.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> motor.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> motor.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> motor.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> motor.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> motor.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> motor.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_acelerar()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    >>> 'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    >>> 'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'Oeste'
"""

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:
    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }

    rotacao_a_esquerda_dct = {
        NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL
    }


def __init__(self):
       self.valor = NORTE

   def girar_a_direita(self):
       self.valor = self.rotacao_a_direita_dct[self.valor]
   def girar_a_esquerda(self):
       self.valor = self.rotacao_a_esquerda_dct[self.valor]




class Motor:

    def __init__(self):
        self.velocidade = 0


    def acelerar(self):
        self.velocidade += 1


    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)