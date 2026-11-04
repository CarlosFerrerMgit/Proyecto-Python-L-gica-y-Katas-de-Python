# Importamos reduce desde functools para acumulaciones de colecciones
from functools import reduce

# EJERCICIO 1: Escribe una función que reciba una cadena de texto como parámetro y
# devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios
# no deben ser considerados.


def contar_frecuencias_letras(texto: str) -> dict:
    """
    Calcula la frecuencia de cada carácter en una cadena ignorando espacios.
    Utiliza el método .get() de los diccionarios para inicializar y acumular.
    """
    frecuencias = {}

    # Normalizamos a minúsculas para que 'A' y 'a' cuenten como la misma letra
    for letra in texto.lower():
        # Filtramos explícitamente los espacios según el requerimiento
        if letra != " ":
            # .get(letra, 0): si la letra ya existe en el diccionario, devuelve su valor actual;
            # si es la primera vez que aparece, devuelve 0 por defecto y le suma 1.
            frecuencias[letra] = frecuencias.get(letra, 0) + 1

    return frecuencias


# Comprobación de funcionamiento:
print(contar_frecuencias_letras("Me llamo Carlos"))


# EJERCICIO 2: Dada una lista de números, obtén una nueva lista con el doble de cada
# valor. Usa la función map().


def duplicar_valores(numeros: list) -> list:
    """
    Devuelve una nueva lista con el doble de cada valor numérico usando map().
    Aplica una función lambda elemento a elemento sobre la colección original.
    """
    # map(función, iterable) transforma cada número de forma diferida (lazy evaluation).
    # Envolvemos el resultado en list() para materializar el iterador en memoria.
    return list(map(lambda x: x * 2, numeros))


# Comprobación de funcionamiento:
print("La nueva lista es:", duplicar_valores([1, 2, 3, 4, 5]))


# EJERCICIO 3: Escribe una función que tome una lista de palabras y una palabra
# objetivo como parámetros. La función debe devolver una lista con todas las
# palabras de la lista original que contengan la palabra objetivo.


def filtrar_palabras_objetivo(palabras: list, objetivo: str) -> list:
    """
    Filtra y retorna las palabras que contienen el término objetivo como subcadena.
    Aplica list comprehension por legibilidad y normalización a minúsculas.
    """
    # Recorremos cada palabra de la lista evaluando si el objetivo forma parte de ella
    resultado = [
        palabra
        for palabra in palabras
        # .lower() asegura que la búsqueda no discrimine mayúsculas de minúsculas
        if objetivo.lower() in palabra.lower()
    ]

    return resultado


# Comprobación de funcionamiento:
print(filtrar_palabras_objetivo(["manzana", "platano", "cereza", "mango"], "ma"))


# EJERCICIO 4: Genera una función que calcule la diferencia entre los valores de dos
# listas. Usa la función map().


def calcular_diferencias(lista1: list, lista2: list) -> list:
    """
    Calcula la resta elemento a elemento entre dos listas paralelas usando map().
    Aprovecha la capacidad de map() para sincronizar múltiples iterables.
    """
    # map() toma en paralelo el valor x de lista1 y el valor y de lista2 en cada posición
    diferencias = map(lambda x, y: x - y, lista1, lista2)

    # Convertimos el objeto map resultante en una lista estándar
    return list(diferencias)


# Comprobación de funcionamiento:
print(calcular_diferencias([4, 5, 6], [1, 2, 3]))


# EJERCICIO 5: Escribe una función que tome una lista de números como parámetro y un
# valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la
# media de los números en la lista y determinar si la media es mayor o igual que
# nota_aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso".
# La función debe devolver una tupla que contenga la media y el estado.


def evaluar_media(calificaciones: list, nota_aprobado: float = 5.0) -> tuple:
    """
    Calcula el promedio de una lista de notas y califica como aprobado o suspenso.
    Usa un parámetro por defecto y gestiona colecciones vacías de forma segura.
    """
    # Verificamos si la lista contiene elementos para prevenir un error ZeroDivisionError
    if not calificaciones:
        return (0.0, "suspenso")

    # sum() suma todos los valores y len() obtiene el recuento total
    media = sum(calificaciones) / len(calificaciones)

    # Determinamos el estado usando un operador ternario según el umbral parametrizado
    estado = "aprobado" if media >= nota_aprobado else "suspenso"

    return (media, estado)


# Comprobación de funcionamiento:
print(evaluar_media([6, 4, 3, 6]))
print(evaluar_media([6, 4, 5, 6]))


# EJERCICIO 6: Escribe una función que calcule el factorial de un número de manera recursiva.


def factorial_recursivo(n: int) -> int:
    """
    Calcula el factorial de un número entero n mediante llamadas recursivas.
    Contempla la validación de valores negativos y el caso base en n <= 1.
    """
    # El factorial no está definido para números enteros negativos
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")

    # Caso base: 0! = 1 y 1! = 1 (detiene la recursividad de llamadas)
    if n in (0, 1):
        return 1

    # Caso recursivo: n! = n * (n - 1)!
    return n * factorial_recursivo(n - 1)


# Comprobación de funcionamiento:
print(factorial_recursivo(5))


# EJERCICIO 7: Genera una función que convierta una lista de tuplas a una lista de strings.
# Usa la función map().


def tuplas_a_strings(lista_tuplas: list) -> list:
    """
    Transforma una colección de tuplas en una lista de cadenas de texto con map().
    Combina map() exterior para la lista y .join() interior para los elementos de cada tupla.
    """
    # Para cada tupla 't', transformamos sus elementos a string con str y los unimos con espacio
    resultado = map(lambda t: " ".join(map(str, t)), lista_tuplas)

    return list(resultado)


# Comprobación de funcionamiento:
print(tuplas_a_strings([("Hola", "Mundo"), ("1", "2"), ("Viernes", "13")]))


# EJERCICIO 8: Escribe un programa que pida al usuario dos números e intente dividirlos.
# Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja
# esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando
# si la división fue exitosa o no.


def dividir_numeros_usuario():
    """
    Solicita dos números por teclado y realiza la división controlando excepciones.
    Maneja ValueError para entradas no numéricas y ZeroDivisionError si divisor es cero.
    """
    try:
        # Solicitamos los datos por consola y convertimos la entrada a tipo float
        dividendo = float(input("Introduce el primer número (dividendo): "))
        divisor = float(input("Introduce el segundo número (divisor): "))

        # Operación principal protegida por el bloque try
        resultado = dividendo / divisor

    except ValueError:
        # Se activa si el usuario ingresa letras o símbolos en lugar de números
        print("Error: Has introducido un carácter no numérico.")
        print("Estado: La división no fue exitosa.")

    except ZeroDivisionError:
        # Se activa si el divisor introducido es exactamente 0
        print("Error: No es posible dividir un número entre cero.")
        print("Estado: La división no fue exitosa.")

    else:
        # Este bloque se ejecuta únicamente si no saltó ninguna excepción previa
        print(f"El resultado de la división es: {resultado}")
        print("Estado: La división fue exitosa.")


# Comprobación de funcionamiento:
dividir_numeros_usuario()


# EJERCICIO 9: Escribe una función que tome una lista de nombres de mascotas como
# parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en
# España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón",
# "Cocodrilo", "Oso"]. Usa la función filter().


def filtrar_mascotas_permitidas(mascotas: list) -> list:
    """
    Filtra una lista de animales descartando las especies prohibidas con filter().
    Utiliza una colección de búsqueda para optimizar las comprobaciones de pertenencia.
    """
    # Definimos el conjunto de especies vetadas (uso de set para búsqueda O(1))
    prohibidas = {"Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"}

    # filter() conserva solo los elementos donde la función lambda devuelve True
    permitidas = filter(lambda animal: animal not in prohibidas, mascotas)

    return list(permitidas)


# Comprobación de funcionamiento:
print(filtrar_mascotas_permitidas(["Perro", "Gato", "Mapache", "Conejo", "Tigre"]))


# EJERCICIO 10: Escribe una función que reciba una lista de números y calcule su
# promedio. Si la lista está vacía, lanza una excepción personalizada y maneja
# el error adecuadamente.


# Definimos una clase de excepción personalizada heredando de la clase base Exception
class ListaVaciaError(Exception):
    """
    Excepción propia para notificar que una estructura numérica no contiene datos.
    """

    pass


def promedio_con_excepcion(numeros: list) -> float:
    """
    Calcula el promedio de una lista o gestiona la excepción propia si viene vacía.
    """
    try:
        # Si la lista no tiene elementos (len == 0 o evaluación booleana False)
        if not numeros:
            raise ListaVaciaError("La lista recibida no contiene elementos numéricos.")

        # Si contiene datos, calculamos la media aritmética
        return sum(numeros) / len(numeros)

    except ListaVaciaError as error:
        # Capturamos la excepción personalizada y mostramos el mensaje descriptivo
        print(f"Error detectado: {error}")
        return 0.0


# Comprobación de funcionamiento:
print(promedio_con_excepcion([1, 2, 3, 4, 5]))


# EJERCICIO 11: Escribe un programa que pida al usuario que introduzca su edad.
# Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado
# (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.


def solicitar_edad_usuario():
    """
    Pide la edad por teclado validando tipo de dato y rango biológico coherente.
    """
    try:
        # Convertimos la entrada a número entero
        edad_str = input("Por favor, introduce tu edad: ")
        edad = int(edad_str)

        # Validamos si está dentro de un rango de edad humano realista
        if edad < 0 or edad > 120:
            # Lanzamos manualmente ValueError con un mensaje explicativo
            raise ValueError(
                f"La edad introducida ({edad}) está fuera del rango permitido (0 a 120 años)."
            )

    except ValueError as error:
        # Captura tanto si el usuario escribe letras como si no cumple el rango de edad
        print(f"Error detectado: {error}")

    else:
        # Se ejecuta únicamente si la conversión y el rango fueron válidos
        print(f"Edad registrada correctamente: {edad} años.")


# Comprobación de funcionamiento:
solicitar_edad_usuario()

# EJERCICIO 12: Genera una función que al recibir una frase devuelva una lista
# con la longitud de cada palabra. Usa la función map().


def longitudes_palabras(frase: str) -> list:
    """
    Devuelve el número de caracteres de cada palabra en una frase usando map().
    """
    # .split() sin argumentos divide la cadena usando los espacios en blanco como separador
    palabras = frase.split()

    # map() aplica la función len directamente sobre cada palabra de la lista
    longitudes = map(len, palabras)

    # Convertimos el generador map en una lista para devolverla
    return list(longitudes)


# Comprobación de funcionamiento:
print(longitudes_palabras("Este ejercicio cuenta las letras de cada palabra"))

# EJERCICIO 13: Genera una función la cual, para un conjunto de caracteres, devuelva
# una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden
# estar repetidas. Usa la función map().


def transformar_caracteres_unicos(caracteres: list) -> list:
    """
    Genera tuplas (MAYÚSCULA, minúscula) de caracteres únicos mediante set y map().
    """
    # Usamos set() para eliminar automáticamente duplicados según el requerimiento
    caracteres_unicos = set(caracteres)

    # map() crea una tupla (char en mayúscula, char en minúscula) para cada elemento único
    tuplas_letras = map(lambda c: (c.upper(), c.lower()), caracteres_unicos)

    return list(tuplas_letras)


# Comprobación de funcionamiento:
print(transformar_caracteres_unicos(["x", "y", "z", "A", "B", "C"]))

# EJERCICIO 14: Crea una función que retorne las palabras de una lista de palabras
# que comience con una letra en específico. Usa la función filter().


def filtrar_por_letra_inicial(palabras: list, letra_inicial: str) -> list:
    """
    Filtra palabras que inician por una letra determinada usando filter().
    """
    # filter() conserva solo las palabras que cumplen la condición booleana
    # .startswith() comprueba el inicio y .lower() evita discrepancias entre mayúsculas y minúsculas
    palabras_filtradas = filter(
        lambda p: p.lower().startswith(letra_inicial.lower()), palabras
    )

    return list(palabras_filtradas)


# Comprobación de funcionamiento:
print(filtrar_por_letra_inicial(["manzana", "platano", "cereza", "mango"], "m"))


# EJERCICIO 15: Crea una función Lambda que sume 3 a cada número de una lista dada.

# Asignamos la expresión lambda que utiliza map() sobre una lista para sumar 3
sumar_tres_a_lista = lambda lista: list(map(lambda x: x + 3, lista))

# Comprobación de funcionamiento:
print(sumar_tres_a_lista([1, 2, 3, 4, 5]))


# EJERCICIO 16: Escribe una función que tome una cadena de texto y un número
# entero n como parámetros y devuelva una lista de todas las palabras que sean
# más largas que n. Usa la función filter().


def filtrar_palabras_largas(texto: str, n: int) -> list:
    """
    Retorna las palabras de un texto cuya longitud supere n caracteres con filter().
    """
    # Dividimos la cadena en palabras individuales
    palabras = texto.split()

    # filter() evalúa la longitud de cada palabra frente al umbral n
    palabras_largas = filter(lambda palabra: len(palabra) > n, palabras)

    return list(palabras_largas)


# Comprobación de funcionamiento:
print(filtrar_palabras_largas("Esta es una cadena de texto para probar la función", 4))


# EJERCICIO 17: Crea una función que tome una lista de dígitos y devuelva el
# número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572.
# Usa la función reduce().


def digitos_a_numero(digitos: list) -> int:
    """
    Convierte una lista de dígitos en un único número entero usando reduce().
    """
    # Si la lista viene vacía devolvemos 0 para evitar excepciones en reduce
    if not digitos:
        return 0

    # Lógica posicional: acumulador * 10 desplaza las cifras a la izquierda para sumar el dígito actual
    # Paso a paso con [5, 7, 2]: (5 * 10) + 7 = 57 -> (57 * 10) + 2 = 572
    return reduce(lambda acumulador, digito: acumulador * 10 + digito, digitos)


# Comprobación de funcionamiento:
print(digitos_a_numero([5, 7, 2]))


# EJERCICIO 18: Escribe un programa en Python que cree una lista de diccionarios
# que contenga información de estudiantes (nombre, edad, calificación) y use la
# función filter para extraer a los estudiantes con una calificación mayor o igual
# a 90. Usa la función filter().


def filtrar_estudiantes_destacados(estudiantes: list) -> list:
    """
    Filtra una lista de estudiantes en formato diccionario con nota >= 90 usando filter().
    """
    # filter() accede a la clave 'calificación' de cada diccionario individual
    aprobados_honor = filter(lambda e: e.get("calificacion", 0) >= 90, estudiantes)

    return list(aprobados_honor)


# Comprobación de funcionamiento:
print(
    filtrar_estudiantes_destacados(
        [
            {"nombre": "Ana", "edad": 20, "calificacion": 95},
            {"nombre": "Luis", "edad": 22, "calificacion": 88},
            {"nombre": "Marta", "edad": 21, "calificacion": 92},
        ]
    )
)


# EJERCICIO 19: Crea una función Lambda que filtre los números impares de una lista dada.

# Asignamos la expresión lambda que utiliza filter() y el operador módulo (%)
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

# Comprobación de funcionamiento:
print(filtrar_impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# EJERCICIO 20: Para una lista con elementos tipo integer y string obtén una nueva
# lista sólo con los valores int. Usa la función filter().


def extraer_enteros(elementos: list) -> list:
    """
    Extrae exclusivamente los elementos de tipo int de una lista heterogénea con filter().
    """
    # type(x) is int valida el tipo exacto sin confundir valores booleanos (True/False son subclase de int)
    solo_enteros = filter(lambda x: type(x) is int, elementos)

    return list(solo_enteros)


# Comprobación de funcionamiento:
print(extraer_enteros([1, "dos", 3, "cuatro", 5, True, 6.0, "siete"]))


# EJERCICIO 21: Crea una función que calcule el cubo de un número dado mediante una función Lambda.

# Función lambda que eleva un número a la potencia de 3
cubo_numero = lambda x: x**3

# Comprobación de funcionamiento:
print(cubo_numero(3))


# EJERCICIO 22: Dada una lista numérica, obtén el producto total de los valores
# de dicha lista. Usa la función reduce().


def producto_total(numeros: list) -> float:
    """
    Calcula la multiplicación acumulada de todos los elementos de una lista usando reduce().
    """
    if not numeros:
        return 0

    # reduce multiplica acumulador * elemento sucesivamente a lo largo de toda la lista
    return reduce(lambda acumulador, elemento: acumulador * elemento, numeros)


# Comprobación de funcionamiento:
print(producto_total([1, 2, 3, 4, 5]))


# EJERCICIO 23: Concatena una lista de palabras. Usa la función reduce().


def concatenar_palabras(palabras: list) -> str:
    """
    Une todas las palabras de una colección en una única cadena usando reduce().
    """
    if not palabras:
        return ""

    # Concatena con un espacio separador entre cada palabra acumulada
    return reduce(lambda acumulador, elemento: f"{acumulador} {elemento}", palabras)


# Comprobación de funcionamiento:
print(concatenar_palabras(["Hola", "me", "llamo", "Carlos"]))


# EJERCICIO 24: Calcula la diferencia total en los valores de una lista. Usa la función reduce().


def diferencia_total(numeros: list) -> float:
    """
    Calcula la resta acumulativa sucesiva de una lista numérica usando reduce().
    """
    if not numeros:
        return 0

    # Resta del primer elemento todos los siguientes de izquierda a derecha
    return reduce(lambda acumulador, elemento: acumulador - elemento, numeros)


# Comprobación de funcionamiento:
print(diferencia_total([10, 5, 3, 1]))


# EJERCICIO 25: Crea una función que cuente el número de caracteres en una cadena de texto dada.


def contar_caracteres(texto: str) -> int:
    """
    Devuelve el total de caracteres de una cadena utilizando la función incorporada len().
    """
    # len() devuelve la longitud total de cualquier secuencia en Python
    return len(texto)


# Comprobación de funcionamiento:
print(contar_caracteres("Hola Mundo"))


# EJERCICIO 26: Crea una función lambda que calcule el resto de la división entre dos números dados.

# Función lambda que calcula el módulo o resto de la división entera mediante %
resto_division = lambda dividendo, divisor: dividendo % divisor

# Comprobación de funcionamiento:
print(resto_division(10, 3))


# EJERCICIO 27: Crea una función que calcule el promedio de una lista de números.


def calcular_promedio(numeros: list) -> float:
    """
    Calcula la media aritmética sumando elementos y dividiendo entre el total.
    """
    # Control de seguridad para evitar ZeroDivisionError si la lista viene vacía
    if not numeros:
        return 0.0

    return sum(numeros) / len(numeros)


# Comprobación de funcionamiento:
print(calcular_promedio([10, 5, 3, 1]))


# EJERCICIO 28: Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.


def primer_elemento_duplicado(elementos: list):
    """
    Retorna el primer elemento repetido en orden de aparición usando un conjunto de vistos.
    """
    # Los sets permiten comprobar pertenencia en tiempo constante O(1)
    elementos_vistos = set()

    for item in elementos:
        # Si el item ya fue almacenado previamente en el set, es el primer duplicado encontrado
        if item in elementos_vistos:
            return item
        elementos_vistos.add(item)

    # Si se recorre la lista completa sin repeticiones, devuelve None
    return None


# Comprobación de funcionamiento:
print(primer_elemento_duplicado([1, 2, 3, 4, 5]))
print(primer_elemento_duplicado([1, 2, 3, 1, 2]))


# EJERCICIO 29: Crea una función que convierta una variable en una cadena de texto
# y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.


def enmascarar_variable(valor) -> str:
    """
    Enmascara con '#' una cadena excepto sus últimos cuatro caracteres.
    """
    texto = str(valor)

    # Si la cadena tiene 4 caracteres o menos no se enmascara ninguno
    if len(texto) <= 4:
        return texto

    # Multiplicamos '#' por el total menos 4, y concatenamos el corte final [-4:]
    caracteres_ocultos = "#" * (len(texto) - 4)
    ultimos_cuatro = texto[-4:]

    return caracteres_ocultos + ultimos_cuatro


# Comprobación de funcionamiento:
print(enmascarar_variable("123456789"))
print(enmascarar_variable("1234"))


# EJERCICIO 30: Crea una función que determine si dos palabras son anagramas, es decir,
# si están formadas por las mismas letras pero en diferente orden.


def son_anagramas(palabra1: str, palabra2: str) -> bool:
    """
    Verifica si dos palabras contienen exactamente las mismas letras ordenadas alfabéticamente.
    """
    # Limpiamos espacios y pasamos a minúsculas para comparar con precisión
    p1 = palabra1.replace(" ", "").lower()
    p2 = palabra2.replace(" ", "").lower()

    # sorted() ordena alfabéticamente los caracteres de cada cadena; si son idénticos, es anagrama
    return sorted(p1) == sorted(p2)


# Comprobación de funcionamiento:
print(son_anagramas("Roma", "amor"))
print(son_anagramas("visa", "vida"))


# EJERCICIO 31: Crea una función que solicite al usuario ingresar una lista de nombres
# y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista,
# se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.


def buscar_nombre_con_excepcion():
    """
    Solicita nombres al usuario y lanza ValueError si el buscado no está presente.
    """
    entrada = input("Introduce los nombres separados por comas: ")
    # Normalizamos la lista eliminando espacios alrededor de cada nombre
    nombres = [n.strip() for n in entrada.split(",")]

    busqueda = input("Introduce el nombre que deseas buscar: ").strip()

    try:
        if busqueda in nombres:
            print(f"Éxito: El nombre '{busqueda}' se encuentra en la lista.")
        else:
            # Si no existe en la lista, lanzamos explícitamente ValueError
            raise ValueError(f"El nombre '{busqueda}' no fue encontrado en la lista.")
    except ValueError as error:
        print(f"Excepción capturada: {error}")


# Comprobación de funcionamiento:
buscar_nombre_con_excepcion()


# EJERCICIO 32: Crea una función que tome un nombre completo y una lista de empleados,
# busque el nombre completo en la lista y devuelve el puesto del empleado si está en
# la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.


def buscar_puesto_empleado(nombre_completo: str, empleados: list) -> str:
    """
    Busca un empleado por nombre completo y retorna su puesto o mensaje de no coincidencia.
    """
    # Recorremos la lista de diccionarios de empleados
    for empleado in empleados:
        if empleado.get("nombre", "").lower() == nombre_completo.lower():
            return empleado.get("puesto", "Puesto no especificado")

    return "La persona no trabaja aquí."


# Comprobación de funcionamiento:
empleados_lista = [
    {"nombre": "Carlos Ferrer", "puesto": "Ingeniero"},
    {"nombre": "Ana Hdez", "puesto": "Administradora"},
    {"nombre": "Luis Rguez", "puesto": "Jefe"},
]

# Comprobación de funcionamiento:
print(buscar_puesto_empleado("Carlos Ferrer", empleados_lista))
print(buscar_puesto_empleado("Pedro Glez", empleados_lista))


# EJERCICIO 33: Crea una función Lambda que sume elementos correspondientes de dos listas dadas.

# Usamos map() con dos iterables en paralelo dentro de una función lambda
sumar_listas_paralelas = lambda lista1, lista2: list(
    map(lambda x, y: x + y, lista1, lista2)
)

# Comprobación de funcionamiento:
print(sumar_listas_paralelas([1, 2, 3], [10, 20, 30]))


# EJERCICIO 34: Crea la clase Arbol, define un árbol genérico con un tronco y ramas como atributos.
# Los métodos disponibles son: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol.


class Arbol:
    """
    Representa la estructura botánica de un árbol mediante tronco y colección de ramas.
    """

    def __init__(self):
        # 1. Inicializar un árbol con tronco de longitud 1 y lista vacía de ramas
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        """2. Incrementa en una unidad la longitud del tronco."""
        self.tronco += 1

    def nueva_rama(self):
        """3. Agrega una nueva rama con longitud inicial de 1."""
        self.ramas.append(1)

    def crecer_ramas(self):
        """4. Aumenta en una unidad la longitud de todas las ramas existentes."""
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion: int):
        """5. Elimina una rama en un índice específico validando que exista."""
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print(f"Error: La posición {posicion} no existe en las ramas del árbol.")

    def info_arbol(self) -> dict:
        """6. Devuelve un resumen con la longitud del tronco, recuento y longitudes de ramas."""
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas.copy(),
        }


# Comprobación de funcionamiento:
mi_arbol = Arbol()
mi_arbol.crecer_tronco()
mi_arbol.nueva_rama()
mi_arbol.crecer_ramas()
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()
mi_arbol.quitar_rama(2)
print(mi_arbol.info_arbol())


# EJERCICIO 36: Crea la clase UsuarioBanco, representa a un usuario de un banco con
# su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar
# operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.


class UsuarioBanco:
    """
    Gestiona cuentas de usuario bancarias y operaciones transaccionales seguras.
    """

    def __init__(self, nombre: str, saldo: float, tiene_cuenta_corriente: bool = True):
        # 1. Inicializar usuario con nombre, saldo y booleano de cuenta corriente
        self.nombre = nombre
        self.saldo = float(saldo)
        self.tiene_cuenta_corriente = tiene_cuenta_corriente

    def agregar_dinero(self, cantidad: float):
        # 2. Incrementa el saldo disponible en la cuenta del usuario.
        if cantidad <= 0:
            raise ValueError("La cantidad a ingresar debe ser superior a cero.")
        self.saldo += cantidad
        print(
            f"Se han ingresado {cantidad}€ a {self.nombre}. Saldo actual: {self.saldo}€"
        )

    def retirar_dinero(self, cantidad: float):
        # 3. Retira fondos validando saldo suficiente y validez de la cuenta corriente.
        if not self.tiene_cuenta_corriente:
            raise PermissionError(
                f"{self.nombre} no dispone de una cuenta corriente habilitada."
            )
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que cero.")
        if cantidad > self.saldo:
            raise ValueError(
                f"Saldo insuficiente. {self.nombre} tiene {self.saldo}€ e intentó retirar {cantidad}€."
            )

        self.saldo -= cantidad
        print(
            f"Retiro de {cantidad}€ realizado por {self.nombre}. Saldo restante: {self.saldo}€"
        )

    def transferir_dinero(self, origen: "UsuarioBanco", cantidad: float):
        # 4. Transfiere fondos desde otro usuario emisor hacia la cuenta actual.
        if cantidad <= 0:
            raise ValueError("El monto a transferir debe ser positivo.")
        if origen.saldo < cantidad:
            raise ValueError(
                f"Transferencia fallida: {origen.nombre} no tiene saldo suficiente ({origen.saldo}€)."
            )

        # Descontamos del emisor y sumamos al receptor
        origen.saldo -= cantidad
        self.saldo += cantidad
        print(
            f"Transferencia completada: {origen.nombre} transfirió {cantidad}€ a {self.nombre}."
        )


# Comprobación de funcionamiento:
alicia = UsuarioBanco("Alicia", 100, True)
carlos = UsuarioBanco("Carlos", 50, True)
carlos.agregar_dinero(20)
alicia.transferir_dinero(carlos, 20)
alicia.retirar_dinero(50)


# EJERCICIO 37: Crea una función llamada procesar_texto que procesa un texto según
# la opción especificada: contar_palabras, reemplazar_palabras, eliminar_palabra.


def contar_palabras(texto: str) -> dict:
    # 1. Cuenta la frecuencia de aparición de cada palabra devolviendo un diccionario.
    palabras = texto.lower().split()
    conteo = {}
    for p in palabras:
        conteo[p] = conteo.get(p, 0) + 1
    return conteo


def reemplazar_palabras(texto: str, palabra_vieja: str, palabra_nueva: str) -> str:
    # 2. Reemplaza una palabra original por una nueva dentro del texto.
    return texto.replace(palabra_vieja, palabra_nueva)


def eliminar_palabra(texto: str, palabra_a_eliminar: str) -> str:
    # 3. Elimina una palabra específica del texto y recompone los espacios.
    palabras = texto.split()
    filtradas = [p for p in palabras if p != palabra_a_eliminar]
    return " ".join(filtradas)


def procesar_texto(texto: str, opcion: str, *args):
    # 4. Orquesta el procesamiento del texto invocando la subfunción requerida con *args.
    opcion = opcion.lower()

    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) < 2:
            raise ValueError(
                "La opción 'reemplazar' requiere: palabra_vieja y palabra_nueva."
            )
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) < 1:
            raise ValueError(
                "La opción 'eliminar' requiere especificar la palabra_a_eliminar."
            )
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError(
            f"Opción '{opcion}' no válida. Usa 'contar', 'reemplazar' o 'eliminar'."
        )


# Comprobación de funcionamiento:
print(procesar_texto("Hola mundo", "contar"))
print(procesar_texto("Hola mundo", "reemplazar", "Hola", "Adiós"))
print(procesar_texto("Hola mundo", "eliminar", "mundo"))


# EJERCICIO 38: Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.


def determinar_momento_dia(hora: int) -> str:
    """
    Determina la franja horaria del día (día, tarde o noche) según la hora (0-23).
    """
    if not (0 <= hora <= 23):
        return "Hora no válida. Debe estar comprendida entre 0 y 23."

    # Definimos franjas habituales: día (6-13), tarde (14-20), noche (21-5)
    if 6 <= hora <= 13:
        return "Es de día"
    elif 14 <= hora <= 20:
        return "Es por la tarde"
    else:
        return "Es de noche"


# Comprobación de funcionamiento:
print(determinar_momento_dia(8))
print(determinar_momento_dia(15))
print(determinar_momento_dia(22))
print(determinar_momento_dia(25))


# EJERCICIO 39: Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas son: 0-69 insuficiente, 70-79 bien, 80-89 muy bien, 90-100 excelente.


def clasificar_calificacion(nota: float) -> str:
    """
    Traduce una calificación numérica en su correspondiente escala cualitativa.
    """
    if not (0 <= nota <= 100):
        return "Nota fuera de rango. Debe ser entre 0 y 100."

    if nota <= 69:
        return "insuficiente"
    elif nota <= 79:
        return "bien"
    elif nota <= 89:
        return "muy bien"
    else:
        return "excelente"


# Comprobación de funcionamiento:
print(clasificar_calificacion(65))
print(clasificar_calificacion(75))
print(clasificar_calificacion(85))
print(clasificar_calificacion(95))
print(clasificar_calificacion(105))


# EJERCICIO 40: Escribe una función que tome dos parámetros: figura (una cadena
# que puede ser 'rectangulo', 'circulo' o 'triangulo') y datos (una tupla con los
# datos necesarios para calcular el área de la figura).


def calcular_area_figura(figura: str, datos: tuple) -> float:
    """
    Calcula el área geométrica de una figura a partir de una tupla de medidas.
    """
    figura = figura.lower()
    pi_aproximado = 3.1415

    if figura == "rectangulo":
        # datos: (base, altura)
        base, altura = datos
        return float(base * altura)

    elif figura == "circulo":
        # datos: (radio,)
        radio = datos[0]
        return float(pi_aproximado * (radio**2))

    elif figura == "triangulo":
        # datos: (base, altura)
        base, altura = datos
        return float((base * altura) / 2)

    else:
        raise ValueError(
            f"Figura '{figura}' no reconocida. Opciones: rectangulo, circulo, triangulo."
        )


# Comprobación de funcionamiento:
print(calcular_area_figura("rectangulo", (5, 10)))
print(calcular_area_figura("circulo", (7,)))
print(calcular_area_figura("triangulo", (6, 8)))


# EJERCICIO 41: Escribe un programa en Python que utilice condicionales para determinar
# el monto final de una compra en una tienda en línea, después de aplicar un descuento.


def calcular_compra_con_descuento():
    """
    Calcula el total de una compra solicitando precio y valor de cupón mediante condicionales.
    """
    try:
        # 1. Solicita al usuario el precio original
        precio_original = float(
            input("Introduce el precio original del artículo (€): ")
        )
        if precio_original <= 0:
            print("El precio del artículo debe ser un número positivo.")
            return

        # 2. Pregunta si tiene cupón de descuento
        tiene_cupon = (
            input("¿Dispones de un cupón de descuento? (sí/no): ").strip().lower()
        )

        # 3 y 4. Manejo de condicionales con if, elif, else
        if tiene_cupon in ("si", "sí", "s"):
            descuento = float(input("Introduce el valor en euros de tu cupón: "))
            if descuento > 0:
                # El precio final no puede ser menor a 0 si el cupón supera el precio
                precio_final = max(0.0, precio_original - descuento)
                print(f"Descuento de {descuento}€ aplicado correctamente.")
            else:
                print(
                    "El valor del cupón no es válido (debe ser mayor a 0). No se aplicó descuento."
                )
                precio_final = precio_original
        elif tiene_cupon in ("no", "n"):
            print("No se aplicó ningún cupón de descuento.")
            precio_final = precio_original
        else:
            print("Respuesta no reconocida. Se procesa la compra sin descuento.")
            precio_final = precio_original

        # 5. Muestra el precio final
        print(f"Monto final a pagar: {precio_final:.2f}€")

    except ValueError:
        print("Error: Has introducido un valor numérico inválido.")


# Comprobación de funcionamiento:
calcular_compra_con_descuento()
