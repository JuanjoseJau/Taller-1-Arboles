# Árboles de Huffman

## 1. ¿Qué son los Árboles de Huffman?

Los **Árboles de Huffman** son una estructura de datos del tipo árbol binario utilizada para la **compresión de datos sin pérdida**. Fueron desarrollados en 1952 por **David A. Huffman**, un estudiante del MIT, como parte de un trabajo académico. El objetivo principal es representar los símbolos (letras, caracteres, bytes) de un mensaje usando **códigos de longitud variable**, asignando códigos más cortos a los símbolos más frecuentes y códigos más largos a los menos frecuentes.

Este método es la base del algoritmo de **Codificación de Huffman**, ampliamente utilizado en formatos de compresión como ZIP, GZIP, JPEG y MP3.

---

## 2. Conceptos Clave

### 2.1 Árbol Binario
Un árbol de Huffman es un árbol binario lleno (cada nodo tiene 0 o 2 hijos). Los **nodos hoja** representan los símbolos del mensaje, y los **nodos internos** son nodos auxiliares generados durante la construcción del árbol.

### 2.2 Frecuencia o Probabilidad
Cada símbolo tiene asociada una **frecuencia** (número de veces que aparece en el mensaje). Esta frecuencia determina la posición del símbolo dentro del árbol: a mayor frecuencia, más cerca de la raíz.

### 2.3 Código Huffman
El **código binario** de cada símbolo se obtiene recorriendo el árbol desde la raíz hasta la hoja correspondiente:
- Ir a la rama **izquierda** añade un **0** al código.
- Ir a la rama **derecha** añade un **1** al código.

### 2.4 Código Prefijo (Prefix-Free Code)
Los códigos generados por Huffman son **códigos prefijo**, lo que significa que ningún código es prefijo de otro. Esto garantiza que la decodificación sea **unívoca y sin ambigüedades**.

---

## 3. Elementos del Árbol de Huffman

| Elemento         | Descripción                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **Nodo hoja**    | Representa un símbolo del alfabeto con su frecuencia                        |
| **Nodo interno** | Nodo auxiliar cuyo valor es la suma de frecuencias de sus hijos             |
| **Raíz**         | Nodo con la mayor frecuencia (suma total de todas las frecuencias)           |
| **Rama izquierda** | Representa el bit **0** en el código del símbolo                          |
| **Rama derecha** | Representa el bit **1** en el código del símbolo                            |
| **Cola de prioridad** | Estructura auxiliar (min-heap) usada para construir el árbol eficientemente |

---

## 4. Proceso de Construcción

A continuación se describe el algoritmo paso a paso:

1. **Calcular frecuencias:** Contar la frecuencia de cada símbolo en el mensaje.
2. **Crear nodos:** Crear un nodo hoja por cada símbolo, con su frecuencia asociada.
3. **Insertar en una cola de prioridad (min-heap):** Ordenar los nodos de menor a mayor frecuencia.
4. **Repetir hasta tener un solo nodo:**
   - Extraer los dos nodos de menor frecuencia.
   - Crear un nuevo nodo interno cuya frecuencia es la **suma** de los dos nodos extraídos.
   - El nodo de menor frecuencia se asigna como hijo izquierdo y el otro como hijo derecho.
   - Insertar el nuevo nodo en la cola de prioridad.
5. **El último nodo restante es la raíz** del Árbol de Huffman.
6. **Asignar códigos:** Recorrer el árbol desde la raíz para asignar el código binario a cada símbolo.

---

## 5. Ejemplo Ilustrativo

Supongamos el mensaje: `"AABBBCCDDDDEE"`

### Paso 1: Frecuencias

| Símbolo | Frecuencia |
|---------|------------|
| A       | 2          |
| B       | 3          |
| C       | 2          |
| D       | 4          |
| E       | 2          |

### Paso 2: Construcción del árbol

Se combinan iterativamente los nodos de menor frecuencia hasta obtener la raíz con frecuencia total **13**.

```
         [13]
        /     \
      [6]      [7]
      / \      / \
    [3] [3]  [3] [4=D]
    /\   |   /\
  [A][C][B][A][E]
   2   2  3  
```
> *(El árbol exacto puede variar dependiendo del orden de desempate)*

### Paso 3: Códigos resultantes

| Símbolo | Código |
|---------|--------|
| D       | 11     |
| B       | 10     |
| A       | 000    |
| C       | 001    |
| E       | 010    |

Los símbolos más frecuentes (D, B) tienen códigos más cortos.

---

## 6. Propiedades del Árbol de Huffman

- **Optimalidad:** El árbol de Huffman produce el código de longitud variable óptimo para un conjunto dado de frecuencias.
- **Sin pérdida:** La compresión es reversible; el mensaje original puede reconstruirse exactamente.
- **Longitud promedio mínima:** La longitud promedio de los códigos es la menor posible para ese conjunto de frecuencias.
- **Dependiente de la fuente:** El árbol cambia si cambian las frecuencias de los símbolos.

---

## 7. Complejidad Algorítmica

| Operación           | Complejidad   |
|---------------------|---------------|
| Construcción del árbol | O(n log n) |
| Codificación         | O(n)          |
| Decodificación       | O(n)          |

Donde **n** es el número de símbolos únicos en el mensaje.

---

## 8. Aplicaciones

- **Compresión de archivos:** Formatos ZIP, GZIP, ZLIB.
- **Compresión de imágenes:** Parte del estándar JPEG (tabla de Huffman).
- **Compresión de audio/video:** MP3, codecs de video.
- **Transmisión de datos:** Reducción del ancho de banda necesario para enviar información.
- **Almacenamiento eficiente:** Bases de datos y sistemas de archivos.

---

## 9. Ventajas y Desventajas

### Ventajas
- Compresión sin pérdida de información.
- Algoritmo simple y eficiente.
- Códigos prefijo que evitan ambigüedades en la decodificación.
- Óptimo para distribuciones de frecuencia conocidas.

### Desventajas
- Requiere conocer las frecuencias antes de codificar (dos pasadas sobre los datos).
- No es ideal cuando todas las frecuencias son iguales (no hay ganancia).
- Para mensajes cortos, la tabla de códigos puede ocupar más espacio que el mensaje comprimido.

---

## 10. Conclusión

Los Árboles de Huffman son una solución elegante y eficiente para el problema de compresión de datos. Al explotar la frecuencia de aparición de los símbolos, logran reducir el espacio necesario para representar información sin perder ningún dato. Su influencia es fundamental en la computación moderna, siendo el pilar de numerosos estándares de compresión que usamos a diario.

---
