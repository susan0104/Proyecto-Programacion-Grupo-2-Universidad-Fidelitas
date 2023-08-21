import random

def registrar_usuario():
    print("**********Registrar cuenta de usuario**********")
    correo = input("Ingrese su correo electrónico: ")
    nombre_comercio = input("Ingrese el nombre del comercio: ")
    telefono_comercio = input("Ingrese el teléfono del comercio: ")
    nombre_dueno = input("Ingrese el nombre del dueño: ")
    ubicacion_local = input("Ingrese la ubicación del local: ")
    print("*******************************")

    usuario = {
        'correo': correo,
        'nombre_comercio': nombre_comercio,
        'telefono_comercio': telefono_comercio,
        'nombre_dueno': nombre_dueno,
        'ubicacion_local': ubicacion_local
    }

    with open('usuario.txt', 'w') as archivo:
        for clave, valor in usuario.items():
            archivo.write(f"{clave}: {valor}\n")
    
    return usuario


def registrar_factura():
    print("**********Registrar factura electrónica*********")
    print("Seleccione el tipo de cédula:")
    print("1. Cédula Física")
    print("2. Cédula Jurídica")
    tipo_cedula_opcion = input("Ingrese el número de opción (1 o 2): ")

    while tipo_cedula_opcion not in ('1', '2'):
        print("Opción inválida. Seleccione el tipo de cédula nuevamente.")
        tipo_cedula_opcion = input("Ingrese el número de opción (1 o 2): ")

    tipo_cedula = "Física" if tipo_cedula_opcion == '1' else "Jurídica"

    numero_cedula = input("Ingrese el número de cédula: ")
    nombre = input("Ingrese el nombre registrado: ")
    telefono = input("Ingrese el teléfono: ")
    correo = input("Ingrese el correo: ")
    provincia = input("Ingrese la provincia: ")
    canton = input("Ingrese el cantón: ")
    distrito = input("Ingrese el distrito: ")
    print("*******************************")

    factura = {
        'tipo_cedula': tipo_cedula,
        'numero_cedula': numero_cedula,
        'nombre': nombre,
        'telefono': telefono,
        'correo': correo,
        'provincia': provincia,
        'canton': canton,
        'distrito': distrito
    }
    with open('factura.txt', 'w') as archivo:
        for clave, valor in factura.items():
            archivo.write(f"{clave}: {valor}\n")

    return factura


def crear_paquete():
    print("**********Registrar paquete**************")
    nombre_destinatario = input("Ingrese el nombre del destinatario: ")
    telefono_destinatario = input("Ingrese el teléfono del destinatario: ")
    numero_cedula = input("Ingrese el número de cédula: ")
    peso = float(input("Ingrese el peso del paquete en kilogramos: "))
    monto_cobro = peso * 500
    cobro_contra_entrega = input("¿Desea cobrar contra entrega? (S/N): ").strip()
    print("*******************************")

    paquete = {
        'nombre_destinatario': nombre_destinatario,
        'telefono_destinatario': telefono_destinatario,
        'numero_cedula': numero_cedula,
        'peso': peso,
        'cobro_contra_entrega': cobro_contra_entrega,
        'monto_cobro': monto_cobro
    }

    with open('paquete.txt', 'w') as archivo:
        for clave, valor in paquete.items():
            archivo.write(f"{clave}: {valor}\n")
    
    numero_guia = ''.join(random.choice('0123456789ABCDEF') for _ in range(8))
    print("El número de guía para el rastreo del paquete es: ")
            
    with open(f'guia_{numero_guia}.txt', 'w') as archivo_guia:
        archivo_guia.write(f"Número de guía: {numero_guia}\n")
        archivo_guia.write("Información del destinatario:\n")
        archivo_guia.write(f"  Nombre: {nombre_destinatario}\n")
        archivo_guia.write(f"  Teléfono: {telefono_destinatario}\n")
        archivo_guia.write(f"  Estado: Creado\n")
        if cobro_contra_entrega.lower() == 's':
            archivo_guia.write("Requiere cobro\n")
            archivo_guia.write(f"Monto a cobrar: {monto_cobro}\n")


    return paquete

def cambiar_estado():
    while True:
        numero_guia_buscar = input("Ingrese el número de guía para buscar el paquete: ")
        archivo_guia_path = f'guia_{numero_guia_buscar}.txt'

        try:
            with open(archivo_guia_path, 'r') as archivo_guia:
                guia_contenido = archivo_guia.read()
                break
        except FileNotFoundError:
            print("La guía no existe. Intente de nuevo.")

    print("********Lista de estados disponibles para el paquete**********")
    print("1. Creado")
    print("2. Recolectado")
    print("3. Entrega Fallida")
    print("4. Entregado")
    seleccion = input('Ingrese una opcion de los estados disponibles: ')
    if seleccion == "1":
        nuevo_estado = "Creado"
    elif seleccion == "2":
        nuevo_estado = "Recolectado"
    elif seleccion == "3":
        nuevo_estado = "Entrega Fallida"
    elif seleccion == "4":
        nuevo_estado = "Entregado"
    else:
        print("Ingreso un numero incorrecto, error en el cambio de estado de paquete!")

    with open(archivo_guia_path, 'w') as archivo_guia:
        guia_contenido = guia_contenido.replace("Estado: Creado", f"Estado: {nuevo_estado}")
        archivo_guia.write(guia_contenido)

    print(f"El estado de la guía {numero_guia_buscar} se ha cambiado a '{nuevo_estado}'.")

def rastreo_paquetes():
    while True:
        numero_guia_buscar = input("Ingrese el número de guía para rastrear el paquete: ")
        archivo_guia_path = f'guia_{numero_guia_buscar}.txt'

        try:
            with open(archivo_guia_path, 'r') as archivo_guia:
                print("Datos del paquete:")
                for linea in archivo_guia:
                    print(linea.strip())
            break
        except FileNotFoundError:
            print("La guía no existe. Intente de nuevo.")

def modulo_estadisticas():
    print("********** Módulo de Estadísticas **********")

    try:
        with open('usuario.txt', 'r') as archivo_usuario:
            lineas_usuario = archivo_usuario.readlines()
            nombre_comercio = lineas_usuario[1].strip().split(":")[1].strip()
    except FileNotFoundError:
        print("No se encontró información de usuario registrada.")
        return

    print(f"Estadísticas para el comercio '{nombre_comercio}':")
    
    # Obtener la cantidad de guías generadas
    cantidad_envios = sum(1 for _ in open('paquete.txt', 'r'))
    print(f"Cantidad de envíos: {cantidad_envios}")

    # Obtener la lista de paquetes enviados
    lista_paquetes = []
    try:
        with open('paquete.txt', 'r') as archivo_paquete:
            for linea in archivo_paquete:
                clave, valor = linea.strip().split(":")
                lista_paquetes.append(f"{clave.strip()}: {valor.strip()}")
        print("Lista de paquetes enviados:")
        for paquete in lista_paquetes:
            print(paquete)
    except FileNotFoundError:
        print("No se encontraron paquetes registrados.")

    # Obtener el monto total de cobro
    monto_total_cobro = sum(float(linea.strip().split(":")[1]) for linea in open('paquete.txt', 'r') if "monto_cobro" in linea)
    print(f"Monto total de cobro: {monto_total_cobro}")

    # Obtener cantidad de paquetes por número de teléfono
    dic_telefonos = {}
    with open('paquete.txt', 'r') as archivo_paquete:
        for linea in archivo_paquete:
            if "telefono_destinatario" in linea:
                telefono = linea.strip().split(":")[1].strip()
                dic_telefonos[telefono] = dic_telefonos.get(telefono, 0) + 1
    print("Cantidad de paquetes por número de teléfono:")
    for telefono, cantidad in dic_telefonos.items():
        print(f"Número de teléfono: {telefono} - Cantidad de paquetes: {cantidad}")

    # Obtener cantidad de paquetes por número de cédula
    dic_cedulas = {}
    with open('paquete.txt', 'r') as archivo_paquete:
        for linea in archivo_paquete:
            if "numero_cedula" in linea:
                cedula = linea.strip().split(":")[1].strip()
                dic_cedulas[cedula] = dic_cedulas.get(cedula, 0) + 1
    print("Cantidad de paquetes por número de cédula:")
    for cedula, cantidad in dic_cedulas.items():
        print(f"Número de cédula: {cedula} - Cantidad de paquetes: {cantidad}")

    print("*******************************************")


print("***************************Bienvenido a Mensajería Fidélitas***************************")

funcionamiento = True

while funcionamiento:
    print("Opciones de usuario Mensajería Fidélitas: ")
    print("1. Crear usuario")
    print("2. Crear factura electrónica")
    print("3. Crear paquete")
    print("4. Cambiar estado de un paquete")
    print("5. Rastrear un paquete")
    print("6. Módulo de estadísticas")
    print("7. Salir")
    
    menu = input("Ingrese una de las opciones: ")
    
    if menu == "1":
        registrar_usuario()
    elif menu == "2":
        registrar_factura()
    elif menu == "3":
        crear_paquete()
    elif menu == "4":
        cambiar_estado()
    elif menu == "5":
        rastreo_paquetes()
    elif menu == "6":
        modulo_estadisticas()
    elif menu == "7":
        print("Gracias por participar!")
        break
    else:
        print("Opción inválida!")

        


