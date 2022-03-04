from usuario import Usuario


john = Usuario("john", "john@email.com")




john.hacer_deposito(2000,"cuenta1")
john.mostrar_balance_usuario("cuenta1")

john.transferir_dinero(100,"cuenta1","cuenta2")

john.mostrar_balance_usuario("cuenta1")
john.mostrar_balance_usuario("cuenta2")