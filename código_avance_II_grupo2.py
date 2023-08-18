import random
#Proyecto de Github
#comentario de prueba
class Usuario:
    def __init__(self, correo, nombre_comercio, telefono_comercio, nombre_dueno, ubicacion_local):
        self.correo = correo
        self.nombre_comercio = nombre_comercio
        self.telefono_comercio = telefono_comercio
        self.nombre_dueno = nombre_dueno
        self.ubicacion_local = ubicacion_local
#procesos
class FacturaElectronica:
    def __init__(self, tipo_cedula, numero_cedula, nombre, telefono, correo, provincia, canton, distrito):
        self.tipo_cedula = tipo_cedula
        self.numero_cedula = numero_cedula
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.provincia = provincia
        self.canton = canton
        self.distrito = distrito

class Paquete:
    def __init__(self, nombre_destinatario, telefono_destinatario, numero_cedula, peso, cobro_contra_entrega, num_guia):
        self.nombre_destinatario = nombre_destinatario
        self.telefono_destinatario = telefono_destinatario
        self.numero_cedula = numero_cedula
        self.peso = peso
        self.cobro_contra_entrega = cobro_contra_entrega
        self.num_guia = num_guia

class Guia:
    def __init__(self, num_guia, nombre_comercio, num_comercio, nombre_destinatario, num_destinatario):
        self.num_guia = num_guia
        self.nombre_comercio = nombre_comercio
        self.num_comercio = num_comercio
        self.nombre_destinatario = nombre_destinatario
        self.num_destinatario = num_destinatario

class Envio:
    def __init__(self, paquete, guia):
        self.paquete = paquete
        self.guia = guia
        self.estado = "Creado"

envios = []  

def registrar_cuenta_usuario():
    print("**********Registrar cuenta de usuario**********")
    correo = input("Ingrese su correo electrónico: ")
    nombre_comercio = input("Ingrese el nombre del comercio: ")
    telefono_comercio = input("Ingrese el teléfono del comercio: ")
    nombre_dueno = input("Ingrese el nombre del dueño: ")
    ubicacion_local = input("Ingrese la ubicación del local: ")
    print("*******************************")

    usuario = Usuario(correo, nombre_comercio, telefono_comercio, nombre_dueno, ubicacion_local)
    return usuario

def registrar_factura_electronica():
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

    factura = FacturaElectronica(tipo_cedula, numero_cedula, nombre, telefono, correo, provincia, canton, distrito)
    return factura

def crear_paquete(usuario, guias_utilizadas):
    print("**********Registrar paquete**************")
    nombre_destinatario = input("Ingrese el nombre del destinatario: ")
    telefono_destinatario = input("Ingrese el teléfono del destinatario: ")
    numero_cedula = input("Ingrese el número de cédula: ")
    peso = float(input("Ingrese el peso del paquete en kilogramos: "))
    cobro_contra_entrega = input("¿Desea cobrar contra entrega? (S/N): ")

    if cobro_contra_entrega.upper() == 'S':
        monto_cobro = float(input("Ingrese el monto en colones a cobrar contra entrega: "))
    else:
        monto_cobro = 0.0
    print("*******************************")

    while True:
        num_guia = random.randint(100, 1000)
        if num_guia not in guias_utilizadas:
            guias_utilizadas.add(num_guia)
            break

    nombre_comercio = usuario.nombre_comercio
    num_comercio = usuario.telefono_comercio
    guia = Guia(num_guia, nombre_comercio, num_comercio, nombre_destinatario, telefono_destinatario)
    paquete = Paquete(nombre_destinatario, telefono_destinatario, numero_cedula, peso, monto_cobro, num_guia)
    envio = Envio(paquete, guia)
    envios.append(envio)  # Agregar el envío a la lista
    return envio

def cambiar_estado(envio, nuevo_estado):
    estados_validos = ["Creado", "Recolectado", "Entrega Fallida", "Entregado"]
    if nuevo_estado in estados_validos:
        envio.estado = nuevo_estado
    else:
        print("Estado inválido. Los estados válidos son:", estados_validos)

def marcar_recolectado(envio):
    cambiar_estado(envio, "Recolectado")

def marcar_entrega_fallida(envio):
    cambiar_estado(envio, "Entrega Fallida")

def marcar_entregado(envio):
    cambiar_estado(envio, "Entregado")

def rastrear_paquete(num_guia):
    for envio in envios:
        if envio.guia.num_guia == num_guia:
            return envio
    return None  

def obtener_estadisticas(usuario):
    cantidad_envios = len(envios)
    paquetes_enviados = [envio.paquete for envio in envios]
    monto_cobro_total = sum(envio.paquete.cobro_contra_entrega for envio in envios)
    cantidad_por_telefono = sum(1 for envio in envios if envio.paquete.telefono_destinatario == usuario.telefono_comercio)
    cantidad_por_cedula = sum(1 for envio in envios if envio.paquete.numero_cedula == usuario.correo)

    return cantidad_envios, paquetes_enviados, monto_cobro_total, cantidad_por_telefono, cantidad_por_cedula

def crear_envio(usuario, guias_utilizadas):
    factura = registrar_factura_electronica()
    envio = crear_paquete(usuario, guias_utilizadas)

    print("Paquete creado con número de guía:", envio.guia.num_guia)
    marcar_recolectado(envio)

    return envio

def main():
    usuario = registrar_cuenta_usuario()
    guias_utilizadas = set()  
    envio = crear_envio(usuario, guias_utilizadas)

    num_guia_rastreo = input("Ingrese el número de guía para rastrear el paquete: ")
    paquete_rastreado = rastrear_paquete(num_guia_rastreo)

    if paquete_rastreado:
        print("Estado del paquete:", paquete_rastreado.estado)
    else:
        print("El paquete con el número de guía especificado no fue encontrado.")

    # Obtener estadísticas del usuario
    cantidad_envios, paquetes_enviados, monto_cobro_total, cantidad_por_telefono, cantidad_por_cedula = obtener_estadisticas(usuario)

    print("Estadísticas:")
    print("Cantidad de envíos:", cantidad_envios)
    print("Paquetes enviados:", paquetes_enviados)
    print("Monto de cobro total:", monto_cobro_total)
    print("Cantidad de paquetes por número de teléfono:", cantidad_por_telefono)
    print("Cantidad de paquetes por número de cédula:", cantidad_por_cedula)

if __name__ == "__main__":
    main()
    
#Función para hacer el modulo de estadisticas 
def guardar_estadisticas(usuario):
    cantidad_envios, paquetes_enviados, monto_cobro_total, cantidad_por_telefono, cantidad_por_cedula = obtener_estadisticas(usuario)

    with open("estadisticas.txt", "w") as archivo:
        archivo.write("Estadísticas del usuario:\n")
        archivo.write("Cantidad de envíos: {}\n".format(cantidad_envios))
        archivo.write("Paquetes enviados:\n")
        for paquete in paquetes_enviados:
            archivo.write("- {}\n".format(paquete))
        archivo.write("Monto de cobro total: {}\n".format(monto_cobro_total))
        archivo.write("Cantidad de paquetes por número de teléfono: {}\n".format(cantidad_por_telefono))
        archivo.write("Cantidad de paquetes por número de cédula: {}\n".format(cantidad_por_cedula))

def main():
    usuario = registrar_cuenta_usuario()
    guias_utilizadas = set()  
    envio = crear_envio(usuario, guias_utilizadas)

    num_guia_rastreo = input("Ingrese el número de guía para rastrear el paquete: ")
    paquete_rastreado = rastrear_paquete(num_guia_rastreo)

    if paquete_rastreado:
        print("Estado del paquete:", paquete_rastreado.estado)
    else:
        print("El paquete con el número de guía especificado no fue encontrado.")

    # Mostrar estadísticas del usuario
    mostrar_estadisticas(usuario)  # Llamada a la función de estadísticas

    # Guardar estadísticas en un archivo
    guardar_estadisticas(usuario)

if __name__ == "__main__":
    main()

