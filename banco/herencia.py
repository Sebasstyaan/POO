from cuenta import Cuenta, CuentaCorriente

#Programa principal ----------------------------
cuenta1 = Cuenta (607080, '15/05/2022', 500000)

cuenta1.consignar(500000)
print('El saldo es: ' + str(cuenta1.getSaldo()))
cuenta1.consignar(3000000)
cuenta1.retirar (50000000)
cuenta1.retirar(500000)
cuenta1.mostrarCuenta()

cuenta2 = CuentaCorriente(345671, '29/07/2021',2000000,23412122)

cuenta2.consignar(400000)
print('El saldo es: ' + str(cuenta2.getSaldo()))
cuenta2.consignar(2000000)
cuenta2.retirar (40000000)
cuenta2.retirar(600000)
cuenta2.mostrarCuenta()
cuenta2.mostrarCuenta() + NumeroChequera()