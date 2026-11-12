import csv, re, json
from pathlib import Path

def validar_entrada(entrada):
    try:
        return int(entrada)
    except ValueError:
        try:
            return float(entrada)
        except ValueError:
            raise ValueError("La entrada no se puede convertir a un numero")

def recibir_entrada(texto):
    entrada = input(texto)
    return validar_entrada(entrada)

def validar_opcion(entrada, opciones):
    if entrada in opciones:
        return entrada
    else:
        raise KeyError("La opción que ingresó no es valida.")

def recibir_opcion(texto, opciones):
    entrada = input(texto)
    return validar_opcion(entrada, opciones)

def recibir_ruta(texto):
    entrada = input(texto)
    ruta = Path(entrada)
    return ruta.resolve()

def procesar_archivo(ruta):
    path = Path(ruta)

    extension = path.suffix.lower()

    if extension == ".csv":
        yield from procesar_csv(path)
    elif extension == ".json":
        yield from procesar_json(path)
    else:
        raise NotImplemented

def procesar_csv(path):
    with open(path, mode="r", encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo)
        for row in reader:
            yield row

def procesar_json(path):
    with open(path, mode="r", encoding="utf-8") as archivo:
        data = json.load(archivo)
        operaciones = data["operaciones"]
        for operacion in operaciones:
            yield operacion

def recibir_lenguaje_natural(texto):
    entrada = input(texto)

    patron = r"""(?xi)
    \b
    (?P<operacion>
        sum(?:a|ar|o|e)?|
        rest(?:a|ar|o|e)?|
        multipli(?:ca|car|co|que|cacion)?|
        divi(?:da|dir|do|de)?|
        promedio?|
        mediana?|
        moda?
    )

    \b
    (?:
        [^.]*?
        
        (?P<a>(?:\d+(?:\.\d+)?|\.\d+))

        \b
        [^.]*?

        (?P<b>(?:\d+(?:\.\d+)?|\.\d+))
    )?
    \b
    """

    regex = re.compile(patron)
    busqueda = regex.search(entrada)
    resultado = busqueda.groupdict()
    print(resultado)

    operacion = resultado.get("operacion", None)
    if "sum" in operacion:
        operacion = "suma"
    elif "rest" in operacion:
        operacion = "resta"
    elif "multipli" in operacion:
        operacion = "multiplicacion"
    elif "divi" in operacion:
        operacion = "division"

    A = resultado.get("a", 0)
    B = resultado.get("b", 0)

    if A is None: A = 0
    if B is None: B = 0

    a = validar_entrada(A)
    b = validar_entrada(B)

    return [operacion, a, b]