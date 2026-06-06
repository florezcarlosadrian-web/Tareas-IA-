calificaciones = [85, 92, 70, 65, 100, 58, 92, 77]
def ordenamiento_burbuja_descedente_stats(lista_original):
    lista = lista_original.copy()
    intercambios = 0
    pasadas = 0
    n = len(lista)
    for i in range(n):
        pasadas += 1
        intercambio = False
        for j in range(0,n -i -1):
            if lista[j] < lista[j+1]:
                lista[j],lista[j+1] = lista[j+1],lista[j]
                intercambio = True
                intercambios += 1
        if not intercambio:break
    salida = lista,intercambios,pasadas
    return salida

def analizar_calificaciones(lista_original):
    # información de las calificaciones
    ordenada,intercambios,pasadas = ordenamiento_burbuja_descedente_stats(lista_original)
    n = len(ordenada)
    promedio = sum(ordenada) / n
    
    if n % 2 == 0:
        mediana = (ordenada[n // 2 ] + ordenada[n // 2 -1]) / 2
    else:
      mediana = ordenada[n // 2]
      
    calificacion_mas_alta = ordenada[0]
    calificacion_mas_baja = ordenada[-1]
    reprobados = 0
    aprobados = 0 
    notas_aprobados = []
    for i in ordenada :
        if i < 70: reprobados += 1
        else: 
          aprobados += 1
          notas_aprobados.append(i)
          
    top_3 = ordenada[0:3]
    
    print(f"Lista original :{lista_original}")
    print(f"Lista ordenada :{ordenada}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Mediana: {mediana}")
    print(f"Mas alta: {calificacion_mas_alta}")
    print(f"Mas baja: {calificacion_mas_baja}")
    print(f"Reprobados: {reprobados}")
    print(f"top 3: {top_3}")
    print(f"Aprobados: {aprobados}")
    print(f"calificaciones de aprobados: {notas_aprobados}\n El Ordenamiento tomo {intercambios} intercambios y {pasadas} pasadas")
    return
analizar_calificaciones(calificaciones)

# Salida esperada:
# Lista original: [85, 92, 70, 65, 100, 58, 92, 77]
# Lista ordenada: [100, 92, 92, 85, 77, 70, 65, 58]
# Promedio: 79.88
# Mediana: 81.0
# Más alta: 100 | Más baja: 58
# Reprobados: 2
# Top 3: [100, 92, 92]
# Ordenamiento tomó 38 intercambios en 6 pasadas