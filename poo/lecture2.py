# class personaje:
# #atributio
#     def __init__(self, nombre, edad, usuario, bando, raza):
#         self.nombre=nombre
#         self.edad=edad
#         self.usuario=usuario
#         self.bando=bando
#         self.raza=raza
#     def mostrar_personaje(self):
#         return{
#             "nombre":self.nombre,
#             "edad":self.edad,
#             "usuario":self.usuario,
#             "bando":self.bando,
#             "raza":self.raza,
#         }

# luffy= personaje("luffy",18,"gomu gomu no mi8", "pirata","humano")
# print(luffy.nombre)
# cobby= personaje("cobby",15,"no","sword","humano")
# print(cobby.bando)
# king=personaje("king",40,"zoan mitologia","pirata","lunaria")
#print(king.raza)

# crea una clase de alumnos con los atributos que usted crea combeniente
# luego instancia a 4 alumnos  
class alumno:
      def __init__(self, nombre, edad, clase, periodo):
        self.nombre=nombre
        self.edad=edad
        self.clase=clase
        self.periodo=periodo
#instanciar
ccori=alumno("joel",18,"arquitectura de plataformas", "IV")
print(ccori.nombre)
parinango= alumno("edith",15,"agropecuaria","III")
print(parinango.periodo)
ccaccachaua=alumno("miguel",20,"enfermeria","VI")
print(ccaccachaua.clase)
