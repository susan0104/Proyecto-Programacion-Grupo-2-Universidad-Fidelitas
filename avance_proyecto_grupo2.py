class Usuario:
    def __init__(self, correo, nombre_comercio, telefono_comercio, nombre_dueno, ubicacion_local):
        self.correo = correo
        self.nombre_comercio = nombre_comercio
        self.telefono_comercio = telefono_comercio
        self.nombre_dueno = nombre_dueno
        self.ubicacion_local = ubicacion_local


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
    def __init__(self, nombre_destinatario, telefono_destinatario, numero_cedula, peso, cobro_contra_entrega):
        self.nombre_destinatario = nombre_destinatario
        self.telefono_destinatario = telefono_destinatario
        self.numero_cedula = numero_cedula
        self.peso = peso
        self.cobro_contra_entrega = cobro_contra_entrega


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
    tipo_cedula = input("Ingrese el tipo de cédula: ")
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


def crear_paquete(usuario):
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

    paquete = Paquete(nombre_destinatario, telefono_destinatario, numero_cedula, peso, monto_cobro)
    return paquete


# Ejemplo de uso
usuario = registrar_cuenta_usuario()
factura = registrar_factura_electronica()
crear_paquete(usuario)
