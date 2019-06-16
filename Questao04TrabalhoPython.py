class Carro(object):
    def __init__(self, kml):
        self.kml = kml
        self.gasolina = 0

    def adicionarGasolina(self, gaso):
        self.gasolina = gaso + self.gasolina

    def andar(self, n):
        self.n = n
        if self.gasolina <=0:
            print('TANQUE SEM GASOLINA, POR FAVOR ABASTEÇA!!!')
        elif self.gasolina < (self.n/self.kml):
            print('GASOLINA INSUFICIENTE, POR FAVOR ABASTEÇA!!!')
        else:
            self.gasolina = self.gasolina - (self.n/self.kml)

    def obterGasolina(self):
        return print('RESTAM {} LITROS DE GASOLINA'.format(self.gasolina))

meuFusca = Carro(2)
meuFusca.adicionarGasolina(5)
meuFusca.andar(20)
meuFusca.obterGasolina()



