import json

import time



contactos = []

def generar_id():
    return "ID" + str(int(time.time() * 1000))

def agregarContacto(cantidad):
    for i in range(cantidad):
        contactos.append({
            "Id": generar_id(),
            "nombre": input(f"Ingrese el nombre del contacto #{i+1}: "),
            "apellido": input(f"Ingrese el apellido del contacto #{i+1}: "),
            "telefono": input(f"Ingrese el telefono del contacto #{i+1}: "),
            "email": input(f"Ingrese el email del contacto #{i+1}: ")
        })
    print("👌Contacto agregado con exito")

def listarContactos():
    contactos = leerJson('contacts.json')
    print("--------Lista de contactos📝--------")
    print("-"*50)
    
    for contacto in contactos:
        print(f"Id: {contacto['Id']}")
        print(f"Nombre: {contacto['nombre']} {contacto['apellido']}")
        print(f"Email: {contacto['email']}")
        print(f"Telefono: {contacto['telefono']}")
        print("-"*50)
    print("Gracias por usar el programa🤩")

def buscarContacto():
    buscarNombre= input("Ingrese el nombre del contacto a buscar: ")
    for contact in leerJson('contacts.json'):
        if contact['nombre'] == buscarNombre:
            print("-"*50)
            print("✔️Contacto encontrado: ")
            print(f"Nombre: {contact['nombre']} {contact['apellido']}")
            print(f"Id: {contact['Id']}")
            print(f"Email: {contact['email']}")
            print(f"Telefono: {contact['telefono']}")
            print("-"*50)
            break
    else:
        print("Contacto no encontrado✖️")

def eliminarContacto():
    eliminarNombre = input("✖️Ingrese el nombre que desea eliminar: ")
    datos = leerJson('contacts.json')
    for nombre_eliminado in datos:
        if nombre_eliminado['nombre'] == eliminarNombre:
            datos.remove(nombre_eliminado)
            escribirJson('contacts.json', datos)
            print("Contacto eliminado correctamente👍")
            print("-"*50)
            print ("📱Informacion del contacto eliminado: ")
            print(f"Nombre: {nombre_eliminado['nombre']} {nombre_eliminado['apellido']}")
            print(f"Id: {nombre_eliminado['Id']}")
            print(f"Email: {nombre_eliminado['email']}")
            print(f"Telefono: {nombre_eliminado['telefono']}")
            print("-"*50)
    else:
        print("Contacto no encontrado")
    
def modificarContacto():
    modificarNombre = input("Ingrese el nombre que desea modificar: ")
    datos = leerJson('contacts.json')
    encontrado = False
    for nombre_modificado in datos:
        
        if nombre_modificado['nombre'] == modificarNombre:
            nombre_modificado['nombre']= input("Ingrese el nuevo nombre")
            nombre_modificado['apellido']= input("Ingrese el nuevo apellido")
            nombre_modificado['telefono']= input("Ingrese el nuevo telefono")
            nombre_modificado['email']= input("Ingrese el nuevo email")
            encontrado = True
            
    if encontrado:
        escribirJson('contacts.json', datos)
        print("✅ Contacto modificado exitosamente.")
    else:
        print("Contacto no encontrado")
    
    

def escribirJson(path: str, data: list):
    with open(path,mode= 'w') as file:
        json.dump(data, file, indent= 4)

def leerJson(path: str):
    with open(path, mode='r') as file:
        datos = json.load(file)
        return datos

menu = """
    Bienvenido a tu Agenda de Contactos
    Selecciona una opcion:
    1. Agregar Contacto
    2. Listar Contactos
    3. Buscar Contacto
    4. Eliminar Contacto
    5. Modificar Contacto
    6. Salir
"""
while True:
    
    opcion = int(input(menu))

    if opcion == 1:
        cantidad = int(input("Cuantos contactos desea agregar: "))
        agregarContacto(cantidad)
        escribirJson('contacts.json', contactos)
    elif opcion == 2:
        listarContactos()
        
    elif opcion == 3:
        buscarContacto()
    
    elif opcion == 4:
        eliminarContacto()
        
    elif opcion == 5:
        modificarContacto()
    elif opcion == 6:
        print("Saliendo....")
        break
        
        
    
    else:
        print("Opcion no valida")
