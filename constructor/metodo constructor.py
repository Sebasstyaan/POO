#metodo constructor
class Cuenta:
    def __init__(self,numero,fecha,saldo):
        self.numero=numero
        self.fechaApertura=fecha
        self.saldo=saldo

    #metodos set +++++++++++++++++++
    def setNumero(self, numero):
        self.numero = numero

    def setSaldo(self, saldo):
        self.saldo = saldo

    #metodos get +++++++++++++++++++
    def getNumero(self):
        return self.numero

    def getFechaApertura(self):
        return self.fecha

    def getSaldo(self):
        return self.saldo

    # metodos de retiro ++++++++++
    def retirar (self, retiro):
        if self.saldo >= retiro:
            self.saldo -= retiro
            print(' su retiro por valor {}. su saldo es {}'.format(retiro, self.saldo))
        else:
            print('Su saldo es insuficiente')

    def consignar (self, valor):
        self.saldo += valor
        print('Su nuevo saldo es {}'.format(self.saldo))

    def mostrarCuenta (self):
        print('Numero de cuenta: {}'.format(self.numero))
        print('Fecha de apertura: {}'.format(self.fechaApertura))
        print('Saldo $' + str(self.saldo))
        print('------------------------------------')

#Programa principal ----------------------------
cuenta1 = Cuenta (607080, '15/05/2022', 500000)

cuenta1.consignar(500000)
print('El saldo es: ' + str(cuenta1.getSaldo()))
cuenta1.consignar(3000000)
cuenta1.retirar (50000000)
cuenta1.retirar(500000)
cuenta1.mostrarCuenta()
    