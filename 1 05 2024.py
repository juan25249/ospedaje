# Registro y consulta de pacientes
#Escribe un programa en Python que permita a un hospital gestionar el registro de pacientes. Cada paciente tiene información personal como nombre, edad
# y número de seguro social. Además, se registra la temperatura corporal de cada paciente cada vez que se toma.

#El programa debe realizar las siguientes acciones:

#1. Permitir al usuario ingresar la información de un nuevo paciente, incluyendo nombre, edad y número de seguro social.
#2. Registrar la temperatura corporal del paciente. El hospital utiliza la escala Celsius para la temperatura.
#3. Mostrar un resumen de la información del paciente, incluyendo nombre, edad, número de seguro social y la última temperatura registrada
# (al finalizar el registro).
#4. Permitir al usuario ver la información de todos los pacientes registrados.
#El programa debe permitir registrar información de múltiples pacientes y mostrar resúmenes individuales y generales para cada uno.
# Lista global para almacenar los pacientes



list_pacientes = []


# Función para registrar un nuevo paciente
def registro_paciente():
    print("*****************************")
    print("Registro de paciente")
    print("*****************************")

    # Solicitar la cantidad de pacientes a registrar
    numeros_paciente = int(input("Digite la cantidad de pacientes: "))

    # Iterar sobre el número de pacientes ingresados
    for i in range(numeros_paciente):
        nombre = input("Digite nombre del paciente: ")
        edad = input("Digite la edad del paciente: ")
        numero_social = input("Digite el número de seguridad social del paciente:")

        # Crear un diccionario para almacenar la información del paciente
        paciente = dict(
            nombre=nombre,
            edad=edad,
            numero_social=numero_social,
        )

        # Agregar el paciente a la lista de pacientes
        list_pacientes.append(paciente)

        # Mostrar la información del paciente registrado
        mostrar_paciente(paciente)


# Función para mostrar la información de un paciente
def mostrar_paciente(paciente):
    print("*****************************")
    print("INFORMACIÓN DEL PACIENTE")
    print("*****************************")
    print("Datos:")
    print("Nombre: ", paciente["nombre"])
    print("Edad: ", paciente["edad"])
    print("Número social: ", paciente["numero_social"])
    if "temperatura" in paciente:
        print("Temperatura: ", paciente["temperatura"])


# Función para agregar la temperatura de un paciente
def agregar_temperatura_al_paciente():
    print("*****************************")
    print("Agregar temperatura de paciente")
    print("*****************************")
    n_social = input("Digite el número social del paciente:")

    # Buscar al paciente por su número de seguridad social
    for paciente in list_pacientes:
        if paciente["numero_social"] == n_social:
            paciente["temperatura"] = input("Digite la temperatura del paciente:")
            break


# Función para mostrar un resumen de un paciente
def mostrar_resumen():
    print("*****************************")
    print("Mostrar resumen del paciente")
    print("*****************************")
    n_social = input("Digite el número social del paciente:")

    # Buscar al paciente por su número de seguridad social
    for paciente in list_pacientes:
        if paciente["numero_social"] == n_social:
            mostrar_paciente(paciente)
            break


# Función para mostrar todos los pacientes registrados
def mostrar_todos_pacientes():
    print("*****************************")
    print("Mostrar todos los pacientes")
    print("*****************************")
    for paciente in list_pacientes:
        mostrar_paciente(paciente)


# Función para el menú de opciones
def menu(opt):
    # Diccionario que mapea las opciones a las funciones correspondientes
    tabla_menu = {
        "1": registro_paciente,
        "2": agregar_temperatura_al_paciente,
        "3": mostrar_resumen,
        "4": mostrar_todos_pacientes
    }
    # Llamar a la función correspondiente según la opción ingresada
    return tabla_menu[opt]()


if __name__ == '__main__':
    seguir = "s"
    while seguir.lower() == "s":
        print("*****************************")
        print("Clinica DevZeros S.A.S")
        print("*****************************")

        print("Opciones de menu:")
        print("1> Agregar y mostrar Registro paciente")
        print("2> Agregar temperatura al paciente en grados celsius")
        print("3> Mostrar Resumen")
        print("4> Mostrar todos los pacientes")
        opt = input("Digite una opción: ")
        menu(opt)
        seguir = input("Ejecucicón terminada, desea seguir? S/N")






