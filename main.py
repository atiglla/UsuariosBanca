from usuario import Usuario


john = Usuario("john", "john@email.com")


john.mostrar_balance_usuario()

john.hacer_deposito(1000)
john.mostrar_balance_usuario()