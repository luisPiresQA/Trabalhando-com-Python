class Conta:

    def __init__(self, numeroP, titularP, saldoP, limiteP):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numeroP
        self.__titular = titularP
        self.__saldo = saldoP
        self.__limite = limiteP
#         O P no final é para indicar que são parametros
    def extrato(self):
        print("Saldo {} do titular {} ".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if(valor > self.__saldo):
            print("Não é premitido sacar valor maior que saldo")
        else:
            self.__saldo -= valor

    def trasfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
