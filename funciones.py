def registro_de_pacientes():
    '''
    Solicitar al usuario que ingrese los datos de pacientes (nombre, edad y síntoma principal).
    Validar que la edad sea mayor a 0.
    Finalizar el ingreso con un nombre vacío, o pueden buscar otra salida del bucle.
    Al finalizar, mostrar:
    - Promedio de edades
    - Cantidad de pacientes mayores de 60
    - Porcentaje de pacientes con síntoma 'fiebre' (ignorar mayúsculas/minúsculas)
    '''

    #acumuladores 
    pacientes = 0
    edades = 0 # COntador de edades
    pacientes_mayores = 0
    sintoma_fiebre = 0
    #Inicio bucle para que el usuario pueda ingresar los pacientes.
    while True:
        #Primera entrada para que ingrese el nombre
        nombre_entrada = input("Ingrese el nombre del paciente (Si no desea continuar, ingrese el nombre vacio): ")
        #Si el nombre no esta, entonces que se rompa el bucle
        if not nombre_entrada:
            break

        #Segunda entrada para la edad del paciente        
        edad_usuario = input("Ingrese la edad del paciente: ")

        #Validaciones, de si es un numero o si la edad es menor o igual a 0
        if not edad_usuario.isdigit():
            print("Edad no valida, intente con un numero")
        else:
            edad = int(edad_usuario)
        if edad <= 0:
            print("La edad no es valida, ingrese una edad mayor a 0. ")

        #Tercera entrada para los sintomas
        sintoma = input("Ingrese el sintoma del paciente: ").lower()

        #Actualizo los acumuladores y el contador
        pacientes += 1
        edades += edad

        if edad > 60:
            pacientes_mayores += 1
        
        if sintoma == "fiebre":
            sintoma_fiebre += 1
    #Valido que por lo menos haya cargado 1 paciente
    if pacientes >= 1:
        #Calculos de promedio y porcentaje
        promedio = edades / pacientes 
        porcentaje_sintoma_fiebre = (sintoma_fiebre / pacientes) * 100
        #Salidas:
        print(f"Promedio de edades: {promedio}")
        print(f"Cantidad de pacientes mayores a 60: {pacientes_mayores}")
        print(f"Porcentaje de pacientes con el sintoma 'fiebre': {sintoma_fiebre} ")
    else:
        #Si no se cargo almenos 1 entonces va a tirar este mensaje.
        print("No se ingresaron pacientes. ")


def gestion_de_notas():
    '''
    Cargar una lista con las notas de 10 alumnos.
    Implementar una función que reciba la lista de notas y retorne:
    - Cantidad de aprobados (nota >= 6)
    - Nota promedio general
    - Mayor nota y su posición en la lista
    Mostrar los resultados.
    '''
    #Cargo la lista de notas
    notas = [10, 4, 8, 9, 6, 7, 5, 2, 3, 1]
    #Contadores y acumuladores
    aprobados = 0
    nota_mas_alta = 0
    notas_suma = 0
    
    #Recorro la lista 
    for i in range(len(notas)):
        #Guardo la nota en una variable
        nota = notas[i]
        #Sumo la nota para el acumulador 
        notas_suma += nota

        #Valido si la nota es mayor o igual a 6, si es asi se sumara un aprobado. 
        if nota >= 6:
            aprobados += 1

        #Valido si la nota es mas alta a la nota encontrada hasta el momento    
        if nota > nota_mas_alta:
            nota_mas_alta = nota
            posicion_de_nota_alta = i + 1

    #Hago los calculos
    promedio = notas_suma / len(notas)
    
    #salidas
    print(f"Cantidad de aprobados: {aprobados}")
    print(f"Nota promedio general: {promedio}")
    print(f"Nota mas alta: {nota_mas_alta}, en la posicion {posicion_de_nota_alta}. ")


def control_de_produccion():
    '''
    Cargar una matriz de 7 filas (días) y 5 columnas (máquinas).
    Cada celda contiene la cantidad de unidades producidas.
    Calcular y mostrar:
    - Promedio de unidades por día
    - Día con mayor producción total
    - Ordenar las producciones del primer día de menor a mayor sin usar sorted()
    '''

    matriz = [
        [3, 8, 10, 7, 15],
        [13, 12, 8, 14, 11],
        [7, 14, 10, 18, 13],
        [12, 8, 4, 11, 7],
        [7, 8 , 3 , 9, 6],
        [8, 9 , 10, 13, 14],
        [15, 19 , 11, 8, 6]
    ]
    mayor_produccion_en_dia = 0
    #Bucle para iterar por filas
    for i in range(len(matriz)):
        #Guardo en una variable la cantidad de produccion x fila 
        cantidad_producidos = 0
        #Este segundo bucle va a iterar para cada elemento de la fila
        for j in matriz[i]:
            #Se van a sumar la cantidad de produccion en el dia 
            cantidad_producidos += j
        promedio = cantidad_producidos / len(matriz[i])
        #salida
        print(f"Cantidad del dia {i + 1}: {promedio}")

        #Aca verifico que la cantidad de productos producidos en el dia sea mas grande que la mayor produccion ya guardada, si es asi entonces que la reemplaze.
        if cantidad_producidos > mayor_produccion_en_dia:
            mayor_produccion_en_dia = cantidad_producidos

    primer_dia = matriz[0] #Saco la primer lista de la matriz
    n = len(primer_dia) #Cantidad de pasadas
    i = 0 
    while i < n - 1: 
        flag = False # Bandera para ver si hubo intercambio o no
        j = 0
        #Recorro la lista de inicio a final
        while j < n - 1 - i:
            if primer_dia[j] > primer_dia[j + 1]: # Verifica si los elementos estan fuera de orden
                lista_aux = primer_dia[j] # Guardo la lista en una variable ya que se va a modificar proximamente.
                primer_dia[j] = primer_dia[j + 1]#Intercambio los numeros
                primer_dia[j+ 1] = lista_aux
                flag = True
            j = j + 1
        i = i + 1
        if not flag: # Si la lista ya estaba ordenada entonces se rompe 
            break
        i = i + 1

    print(f"Las producciones del primer dia fueron: {primer_dia}")
    print("La cantidad mas producida en un dia fue: ", mayor_produccion_en_dia)




def inventario_productos():
    '''
    Usar un diccionario para registrar productos.
    Clave: código (str), Valor: tupla con (nombre, stock, precio).
    Implementar un menú con las opciones:
    1. Agregar producto
    2. Modificar stock
    3. Mostrar productos con stock menor a 5
    4. Salir
    Validar entradas numéricas donde sea necesario.
    '''
    productos = {}
    while True:
        print("MENU PRINCIPAL")
        print("Opcion 1: Agregar producto")
        print("Opcion 2: Modificar stock")
        print("Opcion 3: Mostrar productos con stock menor a 5")

        opcion_usuario = input("Elige una opcion o presiona enter para salir: ")
        #VALIDACIONES DE QUE SEAN SOLOS NUMEROS Y TAMBIEN PARA QUE SI PRESIONA ENTER SE SALGA, O SI DA OTRA COSA QUE NO SEA UN NUMERO ENTONCES LO SACA.
        if opcion_usuario.isdigit():
            opcion = int(opcion_usuario)
        else:
            print("ERROR, NO PUEDE INGRESAR ALGO QUE NO SEA UN NUMERO.")
            break
        if not opcion_usuario:
            break
        
        #AGREGO LA OPCION 1: 
        if opcion == 1:
            #ENTRADAS
            codigo = input("Ingrese el codigo del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = input("Ingrese la cantidad del producto: ")
            #VALIDACION DE QUE SEAN SOLO NUMEROS
            if cantidad.isdigit():
                stock = int(cantidad)
            else:
                print("ERROR: NO PUEDE INGRESAR ALGO QUE NO SEA UN NUMERO. ")
                break
            precio_usuario = input("Ingrese el precio del producto: ")
             #VALIDACION DE QUE SEAN SOLO NUMEROS
            if precio_usuario.isdigit():
                precio = int(precio_usuario)
            else:
                print("ERROR: NO PUEDE INGRESAR ALGO QUE NO SEA UN NUMERO. ")
                break

            productos[codigo] = (nombre, stock, precio)
            print("Producto cargado.")
            print(productos)
        
        elif opcion == 2: # SI el usuario elige opcion 2
            if len(productos) > 0: #Verifica que haya cargado almenos 1 producto.
                codigo_entrada = input("Ingrese el codigo del producto que desee modificar: ") # primer entrada 
                for codigo in productos: # Va a recorrer los codigos
                        if codigo_entrada in productos: # si el codigo de entrada esta en productos entonces sigue, si no tira un "error"
                            cantidad_stock = input("Ingrese la nueva cantidad de stock: ") # Input para la nueva cantidad de stock
                            if cantidad_stock.isdigit(): # Verifica que sea un numero entero y lo convierte a entero guardado en una variable
                                stock_nuevo = int(cantidad_stock)
                                #Guardo el diccionario pero sin el stock
                                nombre, _, precio = productos[codigo]
                                productos[codigo] = (nombre, stock_nuevo, precio)
                                print(productos)
                else: # Caso contrario si no encuentra el codigo que puso.
                    print("ERROR: CODIGO NO ENCONTRADO")
            else:
                print("ERROR: Productos no cargados.")
