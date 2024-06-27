#forma de crear
def imprimir_hola():
    print("hola")

imprimir_hola()

# funciones con parametros
def imprimir_mensaje(mensaje):
    print(mensaje)

imprimir_mensaje("hola")

# funciones con parametros por defecto
def imprimir_mensaje_defecto(mensaje="hola"):
    print(mensaje)

imprimir_mensaje_defecto()
imprimir_mensaje("hola 2")

#funciones de retorno
def concatenar_mensajes (mensaje_1, mensaje_2):
    return  mensaje_1 + mensaje_2

concatenar_mensajes("hola" , "mundo")

class Carro:
    def _init_(self, placa, modelo, marca, color, tipo_motor="Manual"):
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.velocidad = 0
        self.tipo_motor = tipo_motor
        self.esta_prendido = False
        self.cambio = 0
        self.cloche = False

    def prender(self):
        if not self.esta_prendido:
            self.esta_prendido = True
            print("He prendido el carro")
        else:
            print("El carro se encuentra encendido")

    def meter_cambio(self, cambio, cloche  = False):
        self.cloche = cloche
        if self.cloche:
            if (cambio - self.cambio) > 2:
                self.apagar()
            self.cambio = cambio
            return self.cambio
        else:
            print("Se apaga el carro")
            return cambio

    def acelerar(self, velocidad):
        self.velocidad += velocidad
        print("Acelerando a :", self.velocidad)


    def frenar(self):
        if self.velocidad > 0:
            self.velocidad -= 10

    def apagar(self):
        if self.esta_prendido:
            self.esta_prendido = False

carro1 = Carro("123", "2024", "Mazada Cx30", "Rojo")
carro1.prender()
carro1.prender()
print(carro1.meter_cambio(1,True))
acelar = 1
while True:
    carro1.acelerar(acelar)
    if carro1.velocidad >= 10 and carro1.cambio == 1:
        cambio = int(input("Meta un cambio por favor: "))
        carro1.meter_cambio(cambio, True)
        if carro1.velocidad == 15:
            carro1.apagar()
        if not carro1.esta_prendido:
            break

    if carro1.velocidad >= 30 and carro1.cambio == 2:
        cambio = int(input("Meta un cambio por favor: "))
        carro1.meter_cambio(cambio, True)

        if carro1.velocidad == 35:
            carro1.apagar()

        if not carro1.esta_prendido:
            break











