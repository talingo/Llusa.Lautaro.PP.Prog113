import csv
import random
import json

def cargar_archivo(nombre_archivo):
    """Carga datos de bicicletas desde un archivo CSV."""
    bicicletas = []
    with open(nombre_archivo, 'r', newline='') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            fila['tiempo'] = int(fila['tiempo'])
            bicicletas.append(fila)
    return bicicletas

def imprimir_lista(bicicletas):
    """Imprime la lista de bicicletas en formato tabular."""
    print("ID\tNombre\tTipo\tTiempo")
    for bicicleta in bicicletas:
        print(f"{bicicleta['id_bike']}\t{bicicleta['nombre']}\t{bicicleta['tipo']}\t{bicicleta['tiempo']}")

def asignar_tiempos(bicicletas):
    """Asigna tiempos aleatorios a cada bicicleta."""
    for bicicleta in bicicletas:
        bicicleta['tiempo'] = random.randint(50, 120)
    imprimir_lista(bicicletas)  

def informar_ganador(bicicletas):
    """Informa el ganador o ganadores de la carrera (sin usar min)."""
    ganadores = []
    tiempo_ganador = float('inf')
    for bicicleta in bicicletas:
        if bicicleta['tiempo'] < tiempo_ganador:
            tiempo_ganador = bicicleta['tiempo']
            ganadores = [bicicleta]
        elif bicicleta['tiempo'] == tiempo_ganador:
            ganadores.append(bicicleta)

    if len(ganadores) == 1:
        print(f"El ganador es: {ganadores[0]['nombre']} con un tiempo de {tiempo_ganador} minutos.")
    else:
        nombres_ganadores = [ganador['nombre'] for ganador in ganadores]
        print(f"Hubo un empate entre: {nombres_ganadores} con un tiempo de {tiempo_ganador} minutos.")

def filtrar_por_tipo(bicicletas):
    """Filtra bicicletas por tipo (insensible a mayúsculas) y guarda las coincidencias en un nuevo archivo CSV."""
    tipo_buscado = input("Ingrese el tipo de bicicleta a filtrar: ")

    bicicletas_filtradas = []
    for bic in bicicletas:
        if bic['tipo'].upper() == tipo_buscado.upper():
            bicicletas_filtradas.append(bic)

    if bicicletas_filtradas:
        nombre_archivo_nuevo = f"{tipo_buscado}.csv"
        with open(nombre_archivo_nuevo, 'w', newline='') as archivo_nuevo:
            campos = ['id_bike', 'nombre', 'tipo', 'tiempo']
            escritor_csv = csv.DictWriter(archivo_nuevo, fieldnames=campos)
            escritor_csv.writeheader()
            escritor_csv.writerows(bicicletas_filtradas)
        print(f"Se ha creado el archivo '{nombre_archivo_nuevo}' con las bicicletas filtradas.")
    else:
        print(f"No se encontraron bicicletas del tipo '{tipo_buscado}'.")

def informar_promedio_por_tipo(bicicletas):
    """Calcula e imprime el promedio de tiempo por tipo de bicicleta (sin usar funciones de agregación)."""
    promedios = {}
    for bicicleta in bicicletas:
        tipo = bicicleta['tipo']
        if tipo not in promedios:
            promedios[tipo] = {'suma_tiempos': 0, 'cantidad': 0}
        promedios[tipo]['suma_tiempos'] += bicicleta['tiempo']
        promedios[tipo]['cantidad'] += 1

    for tipo, datos in promedios.items():
        promedio = datos['suma_tiempos'] / datos['cantidad']
        print(f"Promedio de tiempo para bicicletas tipo {tipo}: {promedio:.2f} minutos")

def ordenar_burbuja(bicicletas, clave):
    """Ordena una lista de diccionarios usando el algoritmo de burbuja."""
    n = len(bicicletas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if bicicletas[j][clave] > bicicletas[j + 1][clave]:
                bicicletas[j], bicicletas[j + 1] = bicicletas[j + 1], bicicletas[j]

def ordenar_seleccion(bicicletas, clave):
    """Ordena una lista de diccionarios usando el algoritmo de selección."""
    for i in range(len(bicicletas)):
        min_idx = i
        for j in range(i + 1, len(bicicletas)):
            if bicicletas[j][clave] < bicicletas[min_idx][clave]:
                min_idx = j
        bicicletas[i], bicicletas[min_idx] = bicicletas[min_idx], bicicletas[i]

def mostrar_posiciones(bicicletas):
    """Muestra las posiciones ordenadas por tipo y tiempo."""
    bicicletas_ordenadas = bicicletas.copy()
    ordenar_burbuja(bicicletas_ordenadas, 'tipo')
    ordenar_seleccion(bicicletas_ordenadas, 'tiempo')
    imprimir_lista(bicicletas_ordenadas)

def guardar_posiciones(bicicletas):
    """Guarda las posiciones ordenadas en un archivo JSON."""
    bicicletas_ordenadas = bicicletas.copy()
    ordenar_burbuja(bicicletas_ordenadas, 'tipo')
    ordenar_seleccion(bicicletas_ordenadas, 'tiempo')
    with open("posiciones.json", 'w') as archivo_json:
        json.dump(bicicletas_ordenadas, archivo_json)
    print("Se han guardado las posiciones en 'posiciones.json'.")
