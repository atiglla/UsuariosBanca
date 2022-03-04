from cuentaBancaria2 import CuentaBancaria
class Usuario:

    def __init__(self,name,email):
        self.name=name
        self.emai=email
        self.cuenta={
            "cuenta1":CuentaBancaria(tasa=10, balance=0),
            "cuenta2":CuentaBancaria(tasa=5)
        }
    
    def hacer_deposito (self,amount,nombreCuenta):
        self.cuenta[nombreCuenta].balance+=amount
        return self

    def hacer_retiro (self,amount,nombreCuenta):
        if self.cuenta[nombreCuenta].balance-amount>=0:
            self.cuenta[nombreCuenta].balance-=amount
        else:
            print ("Fondos insuficientes: cobrando una tarifa de $5")
            self.cuenta[nombreCuenta].balance-=5
        return self

    def transferir_dinero (self,amount,cuentaorigen,cuentadestino):
        self.cuenta[cuentaorigen].balance-=amount
        self.cuenta[cuentadestino].balance+=amount

    def mostrar_balance_usuario (self,nombreCuenta):
        print(f"Balance: ${self.cuenta[nombreCuenta].balance}")
        return self
    
