class agenda:
    def __init__(self):
        self.contactos = []
    
    def añadirContacto(self,nombre,apellido,correo,telefono): #se crea un nuevo método para añadir un contacto a la base de datos.
        self.contactos.append([nombre,apellido,correo,telefono])

    def eliminarContacto(self,nombre,telefono): #se crea un nuevo método para eliminar un contacto
        for contacto in self.contactos:
            if contacto[0] == nombre and contacto[1] == telefono:
                self.contactos.remove(contacto)
                print(f"El contacto {nombre} fue eliminado")
    
    def buscarContacto(self,nombre,telefono): #se crea un nuevo método para buscar un contacto
        for contacto in self.contactos:
            if contacto[0] == nombre and contacto[1] == telefono:
                print(f"El contacto {nombre} fue encontrado")

    def modificarContacto(self,nombre,apellido,correo,telefono): #se crea un nuevo método para modificar un contacto.
        for contacto in self.contactos:
            if contacto[0] == nombre and contacto[1] == telefono:
                contacto[0] = nombre
                contacto[1] = apellido
                contacto[2] = correo
                contacto[3] = telefono
                print(f"El contacto {nombre} fue modificado")

Agenda = agenda()
contactos=[]

while True:
    print("**********************")
    print("1. Añadir Contacto")
    print("2. Eliminar Contacto")
    print("3. Buscar Contacto")
    print("4. Modificar Contacto")
    print("5. Salir")
    print("**********************")

    opcion = int(input("Qué acción desea realizar:   "))
    if opcion == 1:
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        correo = input("Correo: ")
        telefono = input("Teléfono: ")
        Agenda.añadirContacto(nombre,apellido,correo,telefono)
    elif opcion == 2:
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        Agenda.eliminarContacto(nombre,telefono)
    elif opcion == 3:
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        Agenda.buscarContacto(nombre,telefono)
    elif opcion == 4:
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        correo = input("Correo: ")
        telefono = input("Teléfono: ")
        Agenda.modificarContacto(nombre,apellido,correo,telefono)
    elif opcion == 5:
        break