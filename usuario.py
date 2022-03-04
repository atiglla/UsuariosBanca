from cuentaBancaria2 import CuentaBancaria
class Usuario:

    def __init__(self,name,email):
        self.name=name
        self.emai=email
        self.cuenta=CuentaBancaria(tasa=2,balance=1000)
    
    def hacer_deposito (self,amount):
        self.cuenta.balance+=amount
        return self

    def hacer_retiro (self,amount):
        if self.cuenta.balance-amount>=0:
            self.cuenta.balance-=amount
        else:
            print ("Fondos insuficientes: cobrando una tarifa de $5")
            self.cuenta.balance-=5
        return self

    def mostrar_balance_usuario (self):
        print(f"Balance: ${self.cuenta.balance}")
        return self
    
