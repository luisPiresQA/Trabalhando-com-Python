class Conta:

    def __init__(self, numeroP, titularP, saldoP, limiteP):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numeroP
        self.__titular = titularP
        self.__saldo = saldoP
        self.__limite = limiteP
#         O P no final é para parametros



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

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite
