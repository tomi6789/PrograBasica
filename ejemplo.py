""" import re

email = "rt-nnoc@gmail.com"
pattern = r"^([\w.-]+)@([\w.-]+\.[a-zA-Z]{2,})$"

busqueda = re.search(pattern, email)
usuario = busqueda.group(1)
dominio = busqueda.group(2)

print(usuario, dominio) """

# import requests, pandas, json

# url = "https://fake.jsonmockapi.com/products?length=1"

# with requests.get(url) as response:
#     data = response.json()

#     print(data)

#     dataframe = pandas.json_normalize(data)

#     print(dataframe["shipping.estimatedDeliveryDays.minimum"])
#     print(dataframe[["productName", "description", "shipping.estimatedDeliveryDays.minimum", "shipping.estimatedDeliveryDays.maximum"]].to_markdown())

import pandas, numpy

alumnos = [
    {
        "nombre": "Roberto",
        "matricula": 1,
        "materia": {
            "nombre": "español",
            "calificacion": 1
        }
    },
    {
        "nombre": "Andrea",
        "matricula": 2,
        "materia": {
            "nombre": "matematicas",
            "calificacion": 10
        }
    },
    {
        "nombre": "Claudia",
        "matricula": 3,
        "materia": {
            "nombre": "ciencias",
            "calificacion": 8
        }
    },
    {
        "nombre": "Paulina",
        "matricula": 4,
        "materia": {
            "nombre": "religion",
            "calificacion": 7
        }
    },
    {
        "nombre": "Sergio",
        "matricula": 5,
        "materia": {
            "nombre": "programacion",
            "calificacion": 10
        }
    },
]

#calificaciones = [alumno["calificacion"] for alumno in alumnos]

# promedio = statistics.mean(calificaciones)
# mediana = statistics.median(calificaciones)
# moda = statistics.mode(calificaciones)

# print("*** ESTADISTICA ***")
# print(f"Calificaciones {",".join([str(c) for c in calificaciones])}.")
# print(f"Promedio: {promedio}")
# print(f"Mediana: {mediana}")
# print(f"Moda: {moda}")

#df = pandas.DataFrame(calificaciones, columns=["calificacion"])

df = pandas.json_normalize(alumnos)

print(df)
print(df.describe())

#df = df.astype('float32')

# print(f"Promedio: {df['calificacion'].mean()}")
# print(f"Mediana: {df['calificacion'].median()}")
# print(f"Moda: {df['calificacion'].mode()[0]}")
# print(f"StdDev: {df['calificacion'].std()}")
# print(f"Varianza: {df['calificacion'].var()}")
# print(f"Minimo: {df['calificacion'].min()}")
# print(f"Maximo: {df['calificacion'].max()}")

# print(df['calificacion'].describe().astype('float32'))


x = 1234567890123456789012345678901234567890123456789012345678901234567890123456789.234567890123456789
df = pandas.DataFrame({
    'float64': numpy.array([x], dtype='float64'),
    'float32': numpy.array([x], dtype='float32')
})

print(df.to_string(float_format=lambda x: f"{x:.17f}"))

for dtype in [numpy.float32, numpy.float64]:
    info = numpy.finfo(dtype)
    print(dtype.__name__)
    print(info.bits)
    print(info.tiny)
    print(info.max)