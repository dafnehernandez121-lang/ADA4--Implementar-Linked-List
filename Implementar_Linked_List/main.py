from MyLinkedList import ListaSimplementeLigada

if __name__ == "__main__":
    datos = []
    cantidad = int(input("¿Cuántos datos iniciales deseas ingresar a la lista?: "))

    for i in range(cantidad):
        dato = input(f"Ingresa el dato #{i + 1}: ").strip()
        datos.append(dato)

    print("\n--- Creación de lista insertando al inicio (Figura 5.3) ---")
    lista_inversa = ListaSimplementeLigada()
    for nombre in datos:
        lista_inversa.insertar_al_inicio(nombre)
        print(f"Luego de insertar a '{nombre}':")
        lista_inversa.mostrar()

    print("\n--- Creación de lista insertando al final (orden original) ---")
    lista = ListaSimplementeLigada()
    for nombre in datos:
        lista.insertar_al_final(nombre)
    lista.mostrar()

    while True:
        print("\n--- Opciones para manipular la lista ordenada ---")
        print("1. Insertar un nodo al inicio")
        print("2. Insertar un nodo al final")
        print("3. Insertar un nodo antes de X")
        print("4. Insertar un nodo después de X")
        print("5. Hacer que un nodo apunte a otro (2 nodos apuntando al mismo)")
        print("6. Hacer que TODOS los nodos apunten a uno solo")
        print("7. Salir")

        opcion = input("Selecciona una opción (1-7): ").strip()

        if opcion == "1":
            nuevo = input("Ingresa el nuevo dato a insertar al inicio: ").strip()
            lista.insertar_al_inicio(nuevo)
            lista.mostrar()

        elif opcion == "2":
            nuevo = input("Ingresa el nuevo dato a insertar al final: ").strip()
            lista.insertar_al_final(nuevo)
            lista.mostrar()

        elif opcion == "3":
            x = input("Ingresa el dato de referencia (X): ").strip()
            nuevo = input(f"Ingresa el nuevo dato a insertar ANTES de '{x}': ").strip()
            lista.insertar_antes_de(x, nuevo)
            lista.mostrar()

        elif opcion == "4":
            x = input("Ingresa el dato de referencia (X): ").strip()
            nuevo = input(f"Ingresa el nuevo dato a insertar DESPUÉS de '{x}': ").strip()
            lista.insertar_despues_de(x, nuevo)
            lista.mostrar()

        elif opcion == "5":
            print("\nNota: Si haces que el último nodo apunte a uno intermedio, ambos apuntarán al mismo nodo.")
            origen = input("Ingresa el dato del nodo que cambiará su flecha (origen): ").strip()
            destino = input("Ingresa el dato del nodo al que quieres que apunte (destino): ").strip()
            lista.apuntar_a_mismo_nodo(origen, destino)
            lista.mostrar()

        elif opcion == "6":
            destino = input("Ingresa el dato del nodo al que TODOS van a apuntar: ").strip()
            lista.todos_apuntan_a_uno(destino)
            print("\nRecorrido iniciando desde P (cabeza de la lista):")
            lista.mostrar()

        elif opcion == "7":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")