print("*******************************************************")
print("********************VENTA DE CARROS********************")
print("****************BIENVENIDOS A CAR DREAM****************")
print("*******************************************************")

while True:
    print("*******************MENU DE OPCIONES********************")
    print("*******************************************************")
    print("[1].....................................Alta de carros")
    print("[2].....................................Baja de carros")
    print("[3].....................................Modificaciones de carros")
    print("[4].....................................Busqueda de carros")
    print("[5].....................................Salir")

    number = input("Ingresa el número de la opción a la que quieres acceder: ")
    # Comprobacion de que es numero lo que ingreso el usuario para que no crashee el programa
    try:
        number = int(number)
    except ValueError:
        print("Error, intenta ingresando un numero")
        break
    # Diccionario que podriamos usar en un futuro
    carros = {}
    # Esto es para las salidas de las opciones
    salida = 'si'

    # Opcion para dar de alta carros en el sistema
    if number == 1:
        while salida == 'si':
            marca = input("Ingrese marca del carro: ")
            modelo = input("Ingrese el modelo del carro: ")
            anio = input("Ingrese año del carro: ")
            color = input("Ingresa el color del carro: ")
            precio = input("Ingresa el precio del carro: $")
            # Aqui va una funcion para anadir el carro a la lista de carros 
            # anadir()
            salida = input("Deseas añadir otro carro? (ingresa si/no): ")
            # Funcion para hacer minuscula la informacion que ingrese el usuario y poder hacer una comparacion sin importar las mayusculas o minusculas
            salida = str.lower(salida)
            if salida != "si":
                # For loop para imprimir 100 brincos de linea, esto es para darle un refresh a la pagina
                for i in range(100):
                    print("\n")

    # Opcion para eliminar un carro del sistema                    
    elif number == 2:
        while salida == 'si':
            eliminar = input("Ingresa el numero del carro que quieres eliminar: ")
            confirmacion = input("Seguro que deseas eliminar este carro? (ingresa si/no)")
            # Aqui iria un print con toda la informacion del carro a eliminar
            # print(carro)
            if str.lower(confirmacion) == 'si':
                # Aqui va una funcion para eliminar carros 
                # eliminar()
                print("Eliminado")
            salida = input("Deseas eliminar otro carro? (ingresa si/no): ")
            # Funcion para hacer minuscula la informacion que ingrese el usuario y poder hacer una comparacion sin importar las mayusculas o minusculas
            salida = str.lower(salida)
            if salida != "si":
                # For loop para imprimir 100 brincos de linea, esto es para darle un refresh a la pagina
                for i in range(100):
                    print("\n")
    # Opcion para modificar la informacion de un carro
    elif number == 3:
        while salida == 'si':
            editar = input("Ingresa el numero del carro que deseas editar: ")
            # Aqui va una funcion para editar carros 
            # editar()
            salida = input("Deseas editar otro carro? (ingresa si/no): ")
            # Funcion para hacer minuscula la informacion que ingrese el usuario y poder hacer una comparacion sin importar las mayusculas o minusculas
            salida = str.lower(salida)
            if salida != "si":
                # For loop para imprimir 100 saltos de linea, esto es para darle un refresh a la pagina
                for i in range(100):
                    print("\n")
    # Opcion para buscar carros
    elif number == 4:
        while salida == 'si':
            buscar = input("Ingresa el numero del carro que desesas buscar: ")
            # Aqui va una funcion para buscar carros 
            # buscar()
            salida = input("Deseas buscar otro carro? (ingresa si/no): ")
            # Funcion para hacer minuscula la informacion que ingrese el usuario y poder hacer una comparacion sin importar las mayusculas o minusculas
            salida = str.lower(salida)
            if salida != "si":
                # For loop para imprimir 100 saltos de linea, esto es para darle un refresh a la pagina
                for i in range(100):
                    print("\n")
    # Opcion de salida
    elif number == 5:
        print("Gracias por su visita! Esperamos que vuelvas pronto =D")
        break
    else:
        # For loop para imprimir 100 brincos de linea, esto es para darle un refresh a la pagina
        for i in range(100):
                    print("\n")
        print("ERROR. Intenta ingresando un numero de la lista")


