import funciones

def main():
    bicicletas = funciones.cargar_archivo("bicicletas.csv")
    while True:
        print("\n--- Menú ---")
        print("1. Cargar archivo (ya cargado)")
        print("2. Imprimir lista")
        print("3. Asignar tiempos")
        print("4. Informar ganador")
        print("5. Filtrar por tipo")
        print("6. Informar promedio por tipo")
        print("7. Mostrar posiciones")
        print("8. Guardar posiciones")
        print("9. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            print("El archivo ya ha sido cargado.")
        elif opcion == '2':
            funciones.imprimir_lista(bicicletas)
        elif opcion == '3':
            funciones.asignar_tiempos(bicicletas)
        elif opcion == '4':
            funciones.informar_ganador(bicicletas)
        elif opcion == '5':
            funciones.filtrar_por_tipo(bicicletas)
        elif opcion == '6':
            funciones.informar_promedio_por_tipo(bicicletas)
        elif opcion == '7':
            funciones.mostrar_posiciones(bicicletas)
        elif opcion == '8':
            funciones.guardar_posiciones(bicicletas)
        elif opcion == '9':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
