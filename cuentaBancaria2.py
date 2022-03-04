class CuentaBancaria:
    cuentas=[]
    def __init__(self, balance=0,tasa=0):
        self.balance=balance
        self.tasa=tasa/100
        CuentaBancaria.cuentas.append(self)
            
    @classmethod
    def todas (cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()
        




