# ===========================================
# Autor: Juan Jose Jauregui Mendoza
# Nombre: Arbol con Listas Enlazadas
# ===========================================

class NodoGeneral:
  def __init__(self, valor, padre):
    self.valor = valor
    self.padre = padre
    self.hijos = [] # Added to store children nodes

class Arbol:
  def __init__(self):
    self.raiz = None

  def _BuscarNodoRecursivo(self, nodo_actual, valor_buscado):
    if nodo_actual is None:
      return None
    if nodo_actual.valor == valor_buscado:
      return nodo_actual
    for hijo in nodo_actual.hijos:
      found_node = self._BuscarNodoRecursivo(hijo, valor_buscado)
      if found_node:
        return found_node
    return None

  def BuscarNodo(self, valor_buscado):
    return self._BuscarNodoRecursivo(self.raiz, valor_buscado)

  def AgregarNodo(self, valor, padre_valor):
    if self.raiz is None:
      self.raiz = NodoGeneral(valor, None)
    else:
      nodo_padre = self.BuscarNodo(padre_valor)
      if nodo_padre is not None:
        nuevo_nodo = NodoGeneral(valor, nodo_padre)
        nodo_padre.hijos.append(nuevo_nodo)
      else:
        print(f"Error: No se encontró el padre '{padre_valor}' para el nodo '{valor}'.")

  def PesoArbol(self):
    if self.raiz is None:
      return 0
    else:
      return self._ContarNodosRecursivo(self.raiz)

  def _ContarNodosRecursivo(self, nodo):
    if nodo is None:
      return 0
    count = 1 # Count current node
    for hijo in nodo.hijos:
      count += self._ContarNodosRecursivo(hijo)
    return count

  def OrdenArbol(self):
    if self.raiz is None:
      return 0
    else:
      return self._ObtenerOrdenRecursivo(self.raiz)

  def _ObtenerOrdenRecursivo(self, nodo):
    if nodo is None:
      return 0
    current_node_degree = len(nodo.hijos)
    max_degree_in_subtree = 0
    for hijo in nodo.hijos:
      max_degree_in_subtree = max(max_degree_in_subtree, self._ObtenerOrdenRecursivo(hijo))
    return max(current_node_degree, max_degree_in_subtree)

  def AlturaArbol(self):
    if self.raiz is None:
      return 0
    else:
      return self._ObtenerAlturaRecursivo(self.raiz)

  def _ObtenerAlturaRecursivo(self, nodo):
    if nodo is None:
      return 0
    if not nodo.hijos:
      return 1
    max_altura_hijo = 0
    for hijo in nodo.hijos:
      max_altura_hijo = max(max_altura_hijo, self._ObtenerAlturaRecursivo(hijo))
    return 1 + max_altura_hijo

arbol=Arbol()

while True:
  print("Menu:")
  print("1. Agregar Nodo")
  print("2. Sacar Peso del Arbol")
  print("3. Sacar Orden del Arbol")
  print("4. Sacar Altura del Arbol")
  print("5. Salir")
  print(" ")
  try:
    O=int(input("Elegir Opcion: "))
    print(" ")
  except ValueError:
    print("ERROR---Por favor, ingrese un número válido para la opción.")
    print(" ")
    continue
  match O:
    case 1:
      valor = input("Ingrese el valor del nodo: ")
      padre = input("Ingrese el valor del padre del nodo: ")
      print(" ")
      arbol.AgregarNodo(valor, padre)
    case 2:
      peso = arbol.PesoArbol()
      print("El peso del árbol es:", peso)
      print(" ")
    case 3:
      orden = arbol.OrdenArbol()
      print("El orden del árbol es:", orden)
      print(" ")
    case 4:
      altura = arbol.AlturaArbol()
      print("La altura del árbol es:", altura)
      print(" ")
    case 5:
      print("Saliendo del programa...")
      break
    case _:
      print("ERROR---Valor Erroneo")
      print(" ")
