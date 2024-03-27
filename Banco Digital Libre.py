#Variables 
Usuarios = ["Rafael", "Raul", "Sebastian", "Kevin", "Jose"]

Contrasenas = [1234, 6969, 1122, 3344, 5566]

Saldo = [1000, 100, 50, 200, 300]

## Funcion Inicio de Sesion
def inicioSesion():
    global username
    username = str(input("\nBienvenido al BDL, Ingrese su nombre: "))

    if username not in Usuarios: 
        print("\nEste usuario no existe o esta mal escrito.")
        inicioSesion()
    
    if username in Usuarios: 
        cajero()

#Funcion cajero 
def cajero():

    print("\n-----Banco Digital Libre-----\n \n1) Hacer un deposito \n2) Hacer un retiro \n3) Revisar saldo \n4) Salir\n ")

    opcion = input("Elige una opcion: ")

    if opcion.isdigit():
        opcion = int(opcion)

        if opcion > 4 or opcion < 1:
            print("\nOpcion Invalida.\n")
            cajero()

    if opcion == 4:
        print("\nGracias por usar nuestro cajero, Saludos!\n")
    
    if opcion == 3: 
        saldo_usuario = str(Saldo[Usuarios.index(username)])
        print("\nBienvenido " + username + ", tu saldo es de: " + saldo_usuario + "$ pesos mexicanos\n")

    if opcion == 2: 
        retiro = int(input("Bienvenido, cuanto dinero te gustaria retirar?: "))
        if retiro > Saldo:
            print("Saldo Insuficiente, tu saldo es de: " + Saldo)
        
        if retiro < Saldo:
            saldoRetiro = Saldo - retiro 
            print("Retiro Realizado, tu saldo actual es de: " + saldoRetiro)
    
    if opcion == 1: 
        usuarioDepositar = input("Bienvenido, Ingresa el nombre de la persona a depositar: ")
        if usuarioDepositar not in Usuarios:
            print("Usuario no existe o mal escrito.")
        
        if usuarioDepositar in Usuarios: 
            dineroDepositar = int(input("Cuanto dinero te gustaria depositarle a " + usuarioDepositar + "?"))

            if dineroDepositar > Saldo[Usuarios.index(username)]:
                print("Saldo insuficiente.")
            else: 
                Saldo[Usuarios.index(username)] -= dineroDepositar
                Saldo[Usuarios.index(usuarioDepositar)] += dineroDepositar
                print("Deposito realizado con exito, tu saldo actual es de: " + str(Saldo[Usuarios.index(username)]))


inicioSesion()