class Cliente:

    def __init__(self, nome):
        self.nome = nome

    def extrato(self):
        print("Nome do cliente é {}".format(self.nome).upper())