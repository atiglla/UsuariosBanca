class CuentaBancaria:
    cuentas=[]
    def __init__(self, balance=0,tasa=0):
        self.balance=balance
        self.tasa=tasa/100
        CuentaBancaria.cuentas.append(self)
    
    def deposito(self,amount):
        self.balance+=amount
        return self

    def retiro(self,amount):
        if self.balance-amount>=0:
            self.balance-=amount
        else:
            print ("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance-=5
        return self

    def mostrar_info_cuenta (self):
        print(f"Balance: ${self.balance}")
        return self

    def generar_interes (self):
        self.balance+=(self.balance*self.tasa)
        return self


    
    @classmethod
    def todas (cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()
        




