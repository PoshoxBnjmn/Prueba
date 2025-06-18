ListaProductos = []
producto={
    "nombre": [],
    "precio": [],
    "cantidad": [],
    "codigo": []
}

opcion="0"

"""

Sacar las funciones del while [X]
Cambiar las listas para crear el producto por un diccionario []
Agregar un codigo al diccionario de producto []
Agregar una lista para almacenar los diccionarios de productos []
modificar las funciones para que utilicen la nueva estructura de diccionario[]
Agregar las funciones faltantes:
    Actualizar cantidad/precio []
    Mostrar inventario completo []
    Eliminar producto []

"""

def ValidarCodigo(codigo):
    codigo = "Diego"
    contador_mayusculas = 0
    contador_numeros = 0
    for l in codigo:
        if l.isupper():
            contador_mayusculas += 1
        if l.isnumeric():
            contador_numeros += 1
    if contador_mayusculas < 2:
        print("***El codigo debe tener al menos 2 mayusculas***")
        return False
    elif contador_numeros == 0:
        print("***El codigo debe tener al menos un numero***")
        return False
    elif len(codigo) < 5:
        print("***El codigo debe tener al menos 5 caracteres***")
        return False
    else:
        return True                                                           

def solicitarProducto():
    nombre=input("Ingrese el nombre del producto: ")
    while True:
        codigo = input ("Ingrese el codgio para el producto")
        if ValidarCodigo(codigo)==True:
            print("Codgio correcto!")
            break
        else:
            print("El codigo es incorrecto. Debe volvera a ingresarlo")
    try:
        stock=int(input("Ingrese el stock del producto: "))
        precio=int(input("Ingrese el precio del producto: "))
        
        if stock<0 or precio <0:
            raise ValueError
            
        else:
            producto=[nombre,precio,stock]
            return producto

    except ValueError:
        print("Debe ingresar valores enteros positivos")
    
def guardarProducto(nombre,precio,stock,codigo):
    ProductoBuscado = buscarProducto(codigo)
    if ProductoBuscado != None:
        print("Ese producto ya fue registrado")
        return None
    producto={"nombre":nombre,"precio":precio,"cantidad":stock,"codigo":codigo}
    ListaProductos.append(producto)
    return True


def buscarProducto(codigo):
    for DictProducto in ListaProductos:
        if codigo == DictProducto["codigo"]:
            return DictProducto
    return None

def mostrarProducto(codigo):
    productoBuscado = buscarProducto(codigo)
    if productoBuscado != None:
        print("-"*60)
        print(f"Cod: {productoBuscado["codigo"]} \t Nombre: {productoBuscado["nombre"]} \t Precio: ${productoBuscado["precio"]} \t Stock: {productoBuscado["cantidad"]} unidades")
        print("-"*60)
    else:
        print("No existe un producto con ese nombre")
        

while opcion!="6":
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion=input("Ingrese la opción que desea(1-6): ")
    
    match opcion:

        case "1":
            nuevoProducto=solicitarProducto()
            if nuevoProducto!= None:
                guardarProducto(nuevoProducto[0],nuevoProducto[1],nuevoProducto[2])
        case "2":
            nombreProducto=input("Ingrese el nombre del producto a buscar: ")
            buscarProducto(nombreProducto)

