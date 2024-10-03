# #creara una calse banco
# class banco:

# #sus atributos seran : nombre, apellido, dni, numero de cuenta , saldao inicil
#  def __init__(self, nombre, apellido, dni, numero_de_cuenta, saldo_inicial):
#         self.nombre=nombre
#         self.apellido=epellido
#         self.dni=dni
#         self.numero_de_cuenta=numero_de_cuenta
#         self.saldo_inicial=saldo_inicial
# #como metodos podremos hacer depositos retirar dinero y ver estado de cuenta .
# usuario=bancio("joel","cachines",25633526,45156461321654115 "IV")
# print(ccori.nombre)
# parinango= alumno("edith",15,"agropecuaria","III")
# print(parinango.periodo)
# ccaccachaua=alumno("miguel",20,"enfermeria","VI")
# print(ccaccachaua.clase)

class Banco:
    def __init__(self,name,lastname,cui,acount,amount):
        self.name=name
        self.lastname=lastname
        self.cui=cui
        self.acount=acount
        self.amount=amount
    def deposit(self,amount):
        self.amount+=amount
        
    def remove_cash(self,amount):
        if amount > self.amount:
            return "no cuentas con saldo suficiente"
        self.amount-=amount
        
    def status_acount(self):
        response=f"""
        ------BIENVENIDO AL BANCO "TEPINCHA Y ESTAFA"------
        Cliente: {self.name}, {self.lastname}  NroCuenta:{self.acount}.
        En estos momentos tienes un saldo de : s/.{self.amount},
        fin del voucher:
        ___________________________________________________________________
        """
        return response

cliente_miguel=Banco("Miguelito","Barraza",784512963,4545,30)
print(cliente_miguel.status_acount())
cliente_miguel.deposit(100)
print(cliente_miguel.status_acount())
cliente_miguel.remove_cash(80)
print(cliente_miguel.status_acount())
cliente_miguel.remove_cash(80)
print(cliente_miguel.status_acount())
#ejercicio 

# crear una clase banco
# sus atributos seran nombres y apellidos del pasajero dni numero de asiento fecha de viaje 
# sus metodos seran ingresar origen, ingresar destino, cancelar viaje, ver estado de pasaje

class Agencia:
    def _init_(self, nombre, apellidos, dni, numero_aviento, fecha_viaje):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.numero_aviento = numero_aviento
        self.fecha_viaje = fecha_viaje
        self.origen = None
        self.destino = None
        self.estado = "Pendiente"

    def ingresar_origen(self, origen):
        self.origen = origen

    def ingresar_destino(self, destino):
        self.destino = destino

    def cancelar_viaje(self):
        self.estado = "Cancelado"

    def ver_estado_pasaje(self):
        print(f"Estado del pasaje: {self.estado}")
        if self.estado == "Pendiente":
            print(f"Origen: {self.origen}")
            print(f"Destino: {self.destino}")

# Ejemplo de uso
pasajero = Agencia("Juan", "Pérez", "12345678A", "12345", "2023-12-25")
pasajero.ingresar_origen("Madrid")
pasajero.ingresar_destino("Barcelona")
pasajero.ver_estado_pasaje()
pasajero.cancelar_viaje()
pasajero.ver_estado_pasaje()