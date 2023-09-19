import pymongo

MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONGO_TIMEOUT = 1000

MONGO_URI= "mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

# try:
#     client = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIMEOUT)
#     client.server_info()
#     print("Conectado")
#     client.close()
# except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
#     print("Tiempo de espera excedido"+errorTiempo)
# except pymongo.errors.ConnectionFailure as errorConexion:
#     print("Error de conexión"+errorConexion)


class agenda:
    
    def __init__(self,client, nombre_bd,nombre_collection):   #se crea un nuevo objeto de la clase y se utiliza para inicializar las variables de instancia.
        self.client = client
        self.nombre_bd = nombre_bd
        self.nombre_collection = nombre_collection
        self.collection = self.client[self.nombre_bd][self.nombre_collection]
        
    def añadirContacto(self,nombre,apellido,correo,telefono): #se crea un nuevo método para añadir un contacto a la base de datos.
        self.collection.insert_one({"nombre":nombre,"apellido":apellido,"correo":correo,"telefono":telefono})

    def eliminarContacto(self,nombre,telefono): #se crea un nuevo método para eliminar un contacto
        self.collection.delete_one({"nombre":nombre,"telefono":telefono})
    
    def buscarContacto(self,nombre,telefono): #se crea un nuevo método para buscar un contacto
        self.collection.find_one({"nombre":nombre,"telefono":telefono})

    def modificarContacto(self,nombre,apellido,correo,telefono): #se crea un nuevo método para modificar un contacto.
        self.collection.find_one({"nombre":nombre,"telefono":telefono,"apellido":apellido,"correo":correo})

client = pymongo.MongoClient("mongodb://localhost:27017/")   
Agenda = agenda(client, 'agenda', 'contactos')

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




