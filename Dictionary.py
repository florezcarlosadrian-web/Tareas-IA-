products = {
    'café':{'precio':9.0,'stock':50},
    'azúcar':{'precio':1.3,'stock':50},
    'leche':{'precio':0.5,'stock':50}
}
def mostrar_menu():
    print('\n===MENÚ DE INVENTARIO===')
    print('1.Mostrar productos')
    print('2.Consultar precio')
    print('3.Añadir producto')
    print('4.ver total de inventario')
    print('5.Eliminar producto')
    print('6.Actualizar Stock')
    print('7.Salir')
    print('=' * 30)

# función para mostrar los artículos del diccionario
def mostrar_articulos(dict_productos):
    print('Estos son los productos:')
    for productos,info in dict_productos.items():
        print(f"-{productos} precio=${info['precio']}, Stock={info['stock']}")
# función para consultar precio
def mostrar_precio(dict_productos):
    compra = input("nombre de producto: ").lower()
    print(compra,dict_productos.get(compra,{}).get('precio','no existe'))
# función para calcular el Valor total del inventario
def calcular_total_inventario(dict_productos):
    total_inventario = 0
    for nombre_producto, info in dict_productos.items():
        precio = info.get('precio',0)
        stock = info.get('stock',0)
        total_inventario += (precio * stock)
    print(f'Valor total del inventario: ${total_inventario}')
    return total_inventario

# función para actualizar el stock

def actualizar_stock(dict_productos):
    print('===Actualizar stock===')
    while True:
        if (nombre := input('Nombre').lower()) == '':
          return
        if nombre in dict_productos:
            try:
                dict_productos[nombre]['stock'] = (stock_nuevo := int(input('Stock nuevo')))
                return
            except ValueError:
                print("Error: el valor del stock debe ser solo números")
                return
        else:
            print(f'{nombre} no existe')

# función para AÑADIR PRODUCTO NUEVO =====
def añadir_producto(dict_productos):
        print("\n--- Añadir nuevo producto ---")
        while True:
            if (nombre_nuevo := input('Nombre: ').lower()) == '':
                return
            if not nombre_nuevo in dict_productos:
                try:
                    precio_nuevo = float(input('Precio: '))
                    stock_nuevo = int(input('Stock: '))
                    dict_productos[nombre_nuevo] = {'precio':precio_nuevo,'stock':stock_nuevo}
                    print(f"Producto '{nombre_nuevo}' añadido.")
                    return
                except ValueError:
                    print("Error: precio y stock deben ser números")
                    return
            else:
                print("Ese producto ya existe. Usa otra opción para actualizar stock")
                return
# función para eliminar producto
def eliminar_producto(dict_productos):
      print("\n---Eliminar producto---")
      if not (nombre := input('Nombre:  ').lower()) in dict_productos:
          print(f"{nombre} no existe")
          return
      dict_productos.pop(nombre)
      print(f'{nombre} Eliminado ')
      return
# función base
def main():
    while True:
        mostrar_menu()
        print("Pulsar Enter/pulsar Espacio.Salir de opción")
        opcion = input(" Elejir Opciones:  ")
        if opcion == '1':
            mostrar_articulos(products)
        elif opcion == '2':
            mostrar_precio(products)
        elif opcion == '3':
            añadir_producto(products)
        elif opcion == '4':
            print("===Calcular total inventario===")
            calcular_total_inventario(products)
        elif opcion == '5':
            eliminar_producto(products)
        elif opcion == '6':
            actualizar_stock(products)
        elif opcion == '7':
            print("Cerrado inventario")
            break
        else:
            print("Función Incorrecta Intenta De Nuevo!")
main()