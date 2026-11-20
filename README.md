# DOCUMENTACIÓN DE PROYECTO FINAL

## Introducción

Este repositorio corresponde al proyecto final de **Programación Básica**. Implementa una calculadora modular en Python que ha evolucionado a lo largo del semestre hasta integrar operaciones aritméticas y estadísticas, validación de entradas con manejo robusto de excepciones, lectura y escritura de archivos (`.csv` y `.json`), procesamiento de instrucciones en lenguaje natural mediante expresiones regulares (`regex`) y generación automática de gráficas con `Matplotlib` y `NumPy`.

---

## Contenido / Índice

1. [¿Qué hace el código?](#qué-hace-el-código)
2. [Estructura del repositorio](#estructura-del-repositorio)
3. [¿Cómo fue construido? (Arquitectura y evolución)](#cómo-fue-construido-arquitectura-y-evolución)
   - [Paquete `matematicas`](#paquete-matematicas)
   - [Paquete `es` (Entrada y Salida)](#paquete-es-entrada-y-salida)
   - [Programas principales y ejemplos](#programas-principales-y-ejemplos)
   - [Evolución en el historial de Git](#evolución-en-el-historial-de-git)
4. [Dependencias](#dependencias)
5. [Instrucciones de instalación y ejecución](#instrucciones-de-instalación-y-ejecución)
6. [Notas técnicas sobre el código actual](#notas-técnicas-sobre-el-código-actual)
7. [Conclusión](#conclusión)

---

## ¿Qué hace el código?

El sistema permite ejecutar cálculos matemáticos a través de **tres modos de entrada** y un **script de demostración gráfica**:

1. **Modo interactivo paso a paso (`main.py`):**
   - Muestra un menú en consola y solicita al usuario el nombre de la operación (`suma`, `resta`, `division`, `multiplicacion`) y dos operandos numéricos (enteros o decimales).
   - Valida entradas y maneja errores con bloques `try / except / else / finally` (`KeyError`, `ValueError`, `ZeroDivisionError`, `TypeError`, `NameError`).
   - Guarda cada operación en memoria (`historial`), actualiza el archivo `historial.csv` y genera la imagen `grafica_sesion.png` con gráficas de pastel y de barras mostrando la frecuencia de cada operación realizada en la sesión.

2. **Modo por lotes desde archivos (`main_archivo.py`):**
   - Solicita la ruta a un archivo `.csv` (como `csvs/programa.csv`) o `.json` (como `jsons/programa.json`).
   - Lee las operaciones fila por fila mediante generadores (`yield`), valida cada operación y sus operandos, y muestra el resultado en consola continuando con las siguientes entradas aun si alguna contiene datos inválidos (por ejemplo `potencia` en `csvs/programa.csv`).

3. **Modo en lenguaje natural con Regex (`main_regex.py`):**
   - Permite al usuario escribir frases en español como `"suma 5 y 3"`, `"multiplicar 4 por 2"` o `"promedio"`.
   - Extrae la operación y hasta dos números utilizando expresiones regulares compiladas en `es/entrada.py` (`recibir_lenguaje_natural`).
   - Soporta tanto operaciones **aritméticas** (usando `a` y `b`) como **estadísticas** (`promedio`, `mediana`, `moda` calculadas sobre los resultados acumulados en `historial`).
   - Registra el historial completo (incluyendo `Resultado`) en `historial.csv` y actualiza `grafica_sesion.png`.

4. **Demostración de visualización (`ejemplo.py`):**
   - Script independiente que construye una figura de 3 subgráficas (`ax1`, `ax2`, `ax3`) para ilustrar funciones lineales, trigonométricas (`sin(x)`), cuadráticas (`x^2` con distintas resoluciones) y una gráfica de pastel, exportando el resultado a `grafica.png`.

---

## Estructura del repositorio

```text
programacionBasica/
├── .gitattributes
├── .gitignore
├── .python-version                  # Versión base especificada: 3.10
├── README.md                        # Documentación del proyecto
├── main.py                          # Modo interactivo por menú en consola
├── main_archivo.py                  # Modo lectura por lotes (.csv / .json)
├── main_regex.py                    # Modo de lenguaje natural con expresiones regulares
├── ejemplo.py                       # Script de ejemplo con Matplotlib y NumPy
├── historial.csv                    # Registro acumulado de operaciones ejecutadas
├── grafica_sesion.png               # Gráfica de pastel y barras generada por sesión
├── hola.png                         # Imagen de ejemplo en el repositorio
├── csvs/
│   └── programa.csv                 # Archivo CSV de prueba con operaciones
├── jsons/
│   └── programa.json                # Archivo JSON de prueba con operaciones
├── es/                              # Paquete de Entrada/Salida (I/O)
│   ├── __init__.py
│   ├── entrada.py                   # Validación, lectura de consola, CSV, JSON y Regex
│   └── salida.py                    # Escritura/anexado del historial en CSV
└── matematicas/                     # Paquete principal de lógica y visualización
    ├── __init__.py                  # Une operaciones de aritmética y estadística
    ├── aritmetica/
    │   ├── __init__.py              # Diccionario `operaciones` aritméticas
    │   ├── suma.py                  # suma(a, b)
    │   ├── resta.py                 # resta(a, b)
    │   ├── multiplicacion.py        # multiplicacion(a, b)
    │   └── division.py              # division(a, b)
    ├── estadistica/
    │   ├── __init__.py              # Diccionario `operaciones` estadísticas
    │   ├── promedio.py              # promedio(lista) usando statistics.mean
    │   ├── mediana.py               # mediana(lista) usando statistics.median
    │   ├── moda.py                  # moda(lista) usando statistics.mode
    │   └── frequencia.py            # frequencias(lista) usando collections.Counter
    └── graficas/
        ├── __init__.py              # generar_figuras() y graficar_historial()
        ├── barras.py                # barras(figura, xs, ys)
        └── pastel.py                # pastel(figura, xs, ys)
```

---

## ¿Cómo fue construido? (Arquitectura y evolución)

El proyecto sigue una **arquitectura modular** que separa las operaciones matemáticas, la entrada/salida de datos y la capa de ejecución:

### Paquete `matematicas`

- **`matematicas/__init__.py`**: Combina los diccionarios de operaciones de aritmética y estadística usando el operador de unión `|`:
  ```python
  operaciones = aritmetica_operaciones | estadistica_operaciones
  ```
- **`matematicas/aritmetica/`**: Cada operación (`suma`, `resta`, `multiplicacion`, `division`) vive en su propio módulo y acepta dos argumentos `(a, b)`. `__init__.py` las centraliza en el diccionario `operaciones` para despacharlas dinámicamente por nombre sin usar cadenas largas de `if/elif`.
- **`matematicas/estadistica/`**:
  - `promedio(lista)`, `mediana(lista)` y `moda(lista)` envuelven funciones del módulo estándar `statistics` (`mean`, `median`, `mode`).
  - `frequencias(lista)` en `frequencia.py` utiliza `collections.Counter` para contar cuántas veces se ejecutó cada operación.
- **`matematicas/graficas/`**:
  - `barras(figura, xs, ys)` y `pastel(figura, xs, ys)` dibujan sobre ejes (`Axes`) de Matplotlib.
  - `generar_figuras()` crea una figura de 1×2 subgráficas (`figsize=(12, 8)`).
  - `graficar_historial(historial, nombre="grafica_sesion.png")` extrae las operaciones del historial, calcula sus frecuencias y guarda ambas gráficas en un archivo `.png`.

### Paquete `es` (Entrada y Salida)

- **`es/entrada.py`**:
  - `validar_entrada(entrada)`: intenta convertir la entrada a `int`; si falla con `ValueError`, intenta convertirla a `float`; si vuelve a fallar, lanza `ValueError("La entrada no se puede convertir a un numero")`.
  - `recibir_entrada(texto)`: solicita un valor por `input()` y lo valida con `validar_entrada`.
  - `validar_opcion(entrada, opciones)` / `recibir_opcion(texto, opciones)`: comprueban que la clave exista en el diccionario `opciones` o lanzan `KeyError`.
  - `recibir_ruta(texto)`: convierte la ruta ingresada a un objeto `pathlib.Path` resuelto (`ruta.resolve()`).
  - `procesar_archivo(ruta)`: detecta la extensión (`.csv` o `.json`) y delega con `yield from` a `procesar_csv(path)` (usando `csv.DictReader`) o `procesar_json(path)` (usando `json.load` y leyendo la clave `"operaciones"`). Si la extensión no coincide, lanza `NotImplemented`.
  - `recibir_lenguaje_natural(texto)`: compila una expresión regular (`re.compile` con banderas `(?xi)` para ignorar mayúsculas/minúsculas y permitir formato multilínea comentado) con grupos nombrados `(?P<operacion>...)`, `(?P<a>...)` y `(?P<b>...)`. Normaliza variantes verbales en español (por ejemplo, `sumar`/`sumo`/`sume` → `"suma"`) y retorna `[operacion, a, b]`.
- **`es/salida.py`**:
  - `producir_archivo(ruta, historial)`: abre el archivo en modo `"a"` (anexar) si ya existe, o en modo `"w"` (escribir con encabezados) si es nuevo, guardando las filas mediante `csv.DictWriter` con los campos `["Operacion", "A", "B", "Resultado"]`.

### Programas principales y ejemplos

- `main.py`: ciclo interactivo `while True` con bloques `try / except / else / finally` separados para capturar la opción, los dos operandos y la ejecución de la operación, actualizando `grafica_sesion.png` y `historial.csv`.
- `main_regex.py`: ciclo interactivo basado en `recibir_lenguaje_natural`, capaz de alternar entre operaciones aritméticas (`a`, `b`) y estadísticas (calculadas sobre `[h["Resultado"] for h in historial]`).
- `main_archivo.py`: ciclo `for` sobre `procesar_archivo(ruta)` con manejo de errores por cada fila procesada.
- `ejemplo.py`: ejemplo autónomo de graficación con `matplotlib.pyplot` y `numpy`.

### Evolución en el historial de Git

El repositorio refleja el desarrollo incremental visto en clase:
1. **`Initial commit` → `Cuarta clase`**: creación de la calculadora básica y separación inicial de operaciones aritméticas en módulos.
2. **`reescritura` → `excepciones` → `csv program`**: incorporación del paquete `es/` para entrada/salida, soporte de archivos CSV y control de excepciones con `try/except/else/finally`.
3. **`up to date` → `actualizacion final`**: reorganización bajo el paquete `matematicas/` (`aritmetica`, `estadistica`, `graficas`), soporte para archivos JSON (`jsons/programa.json`), análisis de lenguaje natural (`main_regex.py`) y generación de gráficas (`ejemplo.py`, `grafica_sesion.png`).

---

## Dependencias

### Requisitos de Python

- **Python**: en `.python-version` se indica `3.10`.
  - *Nota de compatibilidad:* el operador de unión de diccionarios `|` (`matematicas/__init__.py`) requiere **Python >= 3.9**, y los f-strings con comillas dobles anidadas (`print(f"{"*" * 6} MENU {"*" * 6}")` en `main.py`, `main_archivo.py` y `main_regex.py`) utilizan PEP 701, disponible a partir de **Python >= 3.12**.

### Módulos de la biblioteca estándar de Python

| Módulo | Uso en el proyecto |
|---|---|
| `csv` | Lectura (`DictReader`) y escritura (`DictWriter`) de archivos CSV (`es/entrada.py`, `es/salida.py`) |
| `json` | Lectura de archivos JSON (`es/entrada.py`) |
| `re` | Expresión regular con grupos nombrados para lenguaje natural (`es/entrada.py`) |
| `pathlib` | Manejo y resolución de rutas con `Path` (`es/entrada.py`, `es/salida.py`) |
| `statistics` | Cálculo de `mean`, `median` y `mode` (`matematicas/estadistica/`) |
| `collections` | Conteo de frecuencias con `Counter` (`matematicas/estadistica/frequencia.py`) |

### Paquetes externos

El repositorio no incluye un archivo `requirements.txt` o `pyproject.toml` con versiones fijadas, pero el código importa los siguientes paquetes de terceros:

| Paquete | Versión | Uso en el proyecto |
|---|---|---|
| `numpy` | Sin versión fijada (compatible con Python actual) | Generación de arreglos y función `sin` en `ejemplo.py`; importado en `matematicas/graficas/` |
| `matplotlib` | Sin versión fijada (compatible con Python actual) | Creación de figuras, gráficas de barras, pastel y exportación a `.png` (`matematicas/graficas/`, `ejemplo.py`) |

---

## Instrucciones de instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/tomi6789/PrograBasica.git
cd PrograBasica
```

### 2. Crear un entorno virtual e instalar dependencias

En Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install matplotlib numpy
```

En Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install matplotlib numpy
```

### 3. Ejecutar los programas

#### A) Calculadora interactiva por menú (`main.py`)

```bash
python main.py
```

Ejemplo de interacción:

```text
****** MENU ******
Introduce una opción: suma
Introduce un numero: 10
Introduce otro numero: 5
#=> 15
El programa continua
```

- Operaciones válidas: `suma`, `resta`, `division`, `multiplicacion`.
- Genera/actualiza `historial.csv` y `grafica_sesion.png`.
- Para salir del ciclo infinito, presiona `Ctrl + C`.

#### B) Calculadora en lenguaje natural (`main_regex.py`)

```bash
python main_regex.py
```

Ejemplos de frases aceptadas:

```text
¿Qué operación quieres hacer? suma 12 y 8
¿Qué operación quieres hacer? multiplicar 4 por 5
¿Qué operación quieres hacer? promedio
```

- Al ingresar operaciones aritméticas se acumulan sus resultados en `historial`; después puedes pedir `promedio`, `mediana` o `moda` sobre esos resultados.

#### C) Procesamiento por lotes desde archivo (`main_archivo.py`)

```bash
python main_archivo.py
```

Cuando solicite la ruta, puedes probar con los archivos incluidos:

- `csvs/programa.csv`
- `jsons/programa.json`

#### D) Script de ejemplo de gráficas (`ejemplo.py`)

```bash
python ejemplo.py
```

Genera el archivo `grafica.png` en la raíz del proyecto.

---

## Notas técnicas sobre el código actual

Al revisar el código fuente en la rama `main` se observan los siguientes detalles técnicos útiles para mantenimiento futuro:

1. **Importación en `main_archivo.py`:** la línea 1 importa `from aritmetica import ...`, pero en la reorganización del commit `up to date` la carpeta `aritmetica/` pasó a estar dentro de `matematicas/aritmetica/`. Para ejecutar `main_archivo.py` sin errores de `ModuleNotFoundError`, esa importación debe apuntar a `matematicas.aritmetica`.
2. **Escritura repetida en `es/salida.py`:** `producir_archivo` abre `historial.csv` en modo `"a"` (anexar) y escribe la lista `historial` completa en cada iteración, por lo que las filas previas de la sesión se duplican conforme avanza el ciclo; además `main.py` no incluye la clave `"Resultado"` al construir el diccionario de `historial`, aunque `es/salida.py` define `"Resultado"` en `fieldnames`.
3. **Referencia en `except KeyError` de `main_regex.py`:** la línea 21 intenta mostrar `operaciones.keys()`, aunque las variables importadas en ese archivo se llaman `aritmetica_operaciones` y `estadistica_operaciones`.
4. **Coincidencias sin operación en `recibir_lenguaje_natural` (`es/entrada.py`):** si el texto ingresado no coincide con el patrón regex, `busqueda` será `None` y `busqueda.groupdict()` lanzará `AttributeError`.

---

## Conclusión

El repositorio muestra una progresión clara desde scripts básicos de aritmética hasta una aplicación modular con paquetes propios (`matematicas` y `es`), validación de datos con manejo de excepciones, persistencia en CSV, lectura de múltiples formatos (CSV/JSON), análisis de lenguaje natural con expresiones regulares y visualización estadística de uso mediante `Matplotlib` y `NumPy`. Esta estructura facilita ampliar nuevas operaciones matemáticas, formatos de archivo o tipos de gráficas sin reescribir la lógica principal.
