class Nodo:
    def __init__(self, dato):
        self.info = dato
        self.liga = None


class ListaSimplementeLigada:
    def __init__(self):
        self.p = None

    def insertar_al_inicio(self, dato):
        """Inserta un nodo al principio de la lista, generando orden inverso."""
        q = Nodo(dato)
        q.liga = self.p
        self.p = q

    def insertar_al_final(self, dato):
        """Inserta un nodo al final para conservar el orden original."""
        q = Nodo(dato)
        if self.p is None:
            self.p = q
        else:
            actual = self.p
            visitados = set()
            while actual.liga is not None and actual.liga not in visitados:
                visitados.add(actual)
                actual = actual.liga
            actual.liga = q

    def insertar_antes_de(self, x, dato):
        """Inserta un nuevo nodo antes del nodo que contiene la información X."""
        if self.p is None:
            print("La lista está vacía.")
            return

        if self.p.info == x:
            self.insertar_al_inicio(dato)
            return

        anterior = self.p
        actual = self.p.liga
        visitados = {anterior}
        while actual is not None and actual.info != x and actual not in visitados:
            visitados.add(actual)
            anterior = actual
            actual = actual.liga

        if actual is None or actual.info != x:
            print(f"No se encontró el nodo con la información '{x}'.")
        else:
            q = Nodo(dato)
            q.liga = actual
            anterior.liga = q

    def insertar_despues_de(self, x, dato):
        """Inserta un nuevo nodo después del nodo que contiene la información X."""
        actual = self.p
        visitados = set()
        while actual is not None and actual.info != x and actual not in visitados:
            visitados.add(actual)
            actual = actual.liga

        if actual is None or actual.info != x:
            print(f"No se encontró el nodo con la información '{x}'.")
        else:
            q = Nodo(dato)
            q.liga = actual.liga
            actual.liga = q

    def apuntar_a_mismo_nodo(self, dato_origen, dato_destino):
        """Busca el nodo_origen y hace que su liga apunte al nodo_destino."""
        nodo_origen = None
        nodo_destino = None

        actual = self.p
        visitados = set()

        while actual is not None and actual not in visitados:
            visitados.add(actual)
            if actual.info == dato_origen:
                nodo_origen = actual
            if actual.info == dato_destino:
                nodo_destino = actual
            actual = actual.liga

        if nodo_origen is None:
            print(f"Error: No se encontró el nodo origen '{dato_origen}'.")
            return
        if nodo_destino is None:
            print(f"Error: No se encontró el nodo destino '{dato_destino}'.")
            return

        nodo_origen.liga = nodo_destino
        print(f"\n¡Enlace exitoso! Ahora '{dato_origen}' apunta directamente a '{dato_destino}'.")
        print(f"(Cualquier otro nodo que antes apuntara a '{dato_destino}' lo sigue haciendo).")

    def todos_apuntan_a_uno(self, dato_destino):
        """Hace que absolutamente todos los nodos de la lista apunten al nodo con dato_destino."""
        if self.p is None:
            print("La lista está vacía.")
            return

        nodos = []
        actual = self.p
        visitados = set()
        nodo_destino = None

        while actual is not None and actual not in visitados:
            visitados.add(actual)
            nodos.append(actual)
            if actual.info == dato_destino:
                nodo_destino = actual
            actual = actual.liga

        if nodo_destino is None:
            print(f"Error: No se encontró el nodo destino '{dato_destino}'.")
            return

        for nodo in nodos:
            if nodo != nodo_destino:
                nodo.liga = nodo_destino
            else:
                nodo.liga = None

        print(f"\n¡Éxito! Todos los nodos ahora apuntan directamente a '{dato_destino}'.")
        print("Estado individual de cada nodo en memoria:")
        for nodo in nodos:
            destino_str = nodo.liga.info if nodo.liga is not None else "NIL"
            print(f"  Nodo [{nodo.info}] ---> {destino_str}")

    def mostrar(self):
        """Recorre e imprime los elementos desde el inicio P (con detección de ciclos)."""
        actual = self.p
        elementos = []
        visitados = set()

        while actual is not None:
            if actual in visitados:
                elementos.append(f"[CICLO -> vuelve a '{actual.info}']")
                break
            visitados.add(actual)
            elementos.append(str(actual.info))
            actual = actual.liga
        else:
            elementos.append("NIL")

        print(" -> ".join(elementos))