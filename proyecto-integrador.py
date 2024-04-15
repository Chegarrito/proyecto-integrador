def alta_carros(carros): # Función para dar de alta carros
    marca = input("Ingrese marca del carro: ")
    modelo = input("Ingrese el modelo del carro: ")
    anio = input("Ingrese año del carro: ")
    color = input("Ingresa el color del carro: ")
    precio = input("Ingresa el precio del carro: $")
    
    carro = { # Creando un diccionario con los datos del carro
        # Asignacion de los datos del carro
        "Marca": marca,
        "Modelo": modelo,
        "Año": anio,
        "Color": color,
        "Precio": precio,
        "Numero": len(carros) + 1  # Añadiendo el número del carro automáticamente
    }

    carros.append(carro) # Agregando el carro a la lista de carros
    print("Carro registrado correctamente.")

def baja_carros(carros): # Función para eliminar carros
    imprimir_carros(carros) # Imprime los carros para que el usuario pueda ver los números
    eliminar = int(input("Ingrese el numero del carro que desea eliminar: "))  # Convierte input a int
    
    encontrado = False # Variable para saber si se encontró el carro
    for carro in carros: # Itera sobre la lista de carros
        if carro["Numero"] == eliminar:  # Compara el número del carro con el número a eliminar
            encontrado = True # Cambia a True si se encuentra el carro
            print("Carro encontrado, sus datos son:")
            for clave, valor in carro.items(): # Itera sobre las claves y valores del carro
                print(clave + ": " + str(valor)) #Convierte valor a string
            
            confirmacion = input("¿Seguro que desea eliminar este carro? (si/no): ")
            if confirmacion.lower() == "si": # Convierte confirmación a minúsculas
                carros.remove(carro) # Elimina el carro de la lista
                print("Carro eliminado correctamente.")
            else:
                print("Eliminacion cancelada.")

            reasignar_numeros(carros) # Reasigna los números de los carros
            break
    if not encontrado: # Si no se encontró el carro
        print("Carro no encontrado.")

def imprimir_carros(carros): 
    print("Lista de carros")
    for carro in carros: # Itera sobre la lista de carros
        print(f"Número: {carro['Numero']}")  # Cambiando aquí
        for clave, valor in carro.items(): # Itera sobre las claves y valores del carro
            if clave != "Numero":  # Excluyendo el campo 'Numero' para evitar impresión duplicada
                print(f"{clave}: {valor}") # Imprime clave y valor
        print()

def reasignar_numeros(carros): # Reasigna los números de los carros
    for i, carro in enumerate(carros, start=1): # Enumera los carros empezando en 1
        carro["Numero"] = i # Asigna el número al carro

def main():
    print("*******************************************************")
    print("********************VENTA DE CARROS********************")
    print("****************BIENVENIDOS A CAR DREAM****************")
    print("*******************************************************")

    carros = [] # Lista para guardar los carros
    ultimo_indice = -1 # Variable para guardar el último índice de la lista de carros

    while True:
        print("*******************MENU DE OPCIONES********************")
        print("*******************************************************")
        print("[1].....................................Alta de carros")
        print("[2].....................................Baja de carros")
        print("[3].....................................Modificaciones de carros")
        print("[4].....................................Busqueda de carros")
        print("[5].....................................Impresion de carros")
        print("[6].....................................Salir")

        number = input("Ingresa el número de la opción a la que quieres acceder: ")
        # Comprobacion de que es numero lo que ingreso el usuario para que no crashee el programa
        try:
            number = int(number)
        except ValueError:
            print("Error, intenta ingresando un numero")
            break

        # Esto es para las salidas de las opciones
        salida = 'si'

        # Opcion para dar de alta carros en el sistema
        if number == 1:
            while salida == 'si':
                # Funcion para dar de alta carros
                alta_carros(carros)
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
                baja_carros(carros)
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

        # Opcion para imprimir la lista de carros
        elif number == 5:
            imprimir_carros(carros)
        # Opcion de salida
        elif number == 6:
            print("Gracias por su visita! Esperamos que vuelvas pronto =D")
            break
        else:
            # For loop para imprimir 100 brincos de linea, esto es para darle un refresh a la pagina
            for i in range(100):
                        print("\n")
            print("ERROR. Intenta ingresando un numero de la lista")


if __name__ == "__main__":
    main()