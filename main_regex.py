from matematicas.aritmetica import operaciones as aritmetica_operaciones, division, multiplicacion, resta, suma
from matematicas.estadistica import operaciones as estadistica_operaciones, promedio, mediana, moda
from es.entrada import recibir_opcion, recibir_entrada, recibir_lenguaje_natural
from es.salida import producir_archivo
from matematicas.graficas import graficar_historial

if __name__ == "__main__":
    print(f"{"*" * 6} MENU {"*" * 6}")

    historial = []

    while True:
        opcion, a, b = recibir_lenguaje_natural("¿Qué operación quieres hacer? ")

        try:
            if opcion in aritmetica_operaciones:
                resultado = aritmetica_operaciones[opcion](a, b)
            elif opcion in estadistica_operaciones:
                resultado = estadistica_operaciones[opcion]([h["Resultado"] for h in historial])
        except KeyError:
            print(f"La opción que ingresó no es valida. Las opciones disponibles son: {', '.join(operaciones.keys())}.")
        except ZeroDivisionError:
            print("No se puede ejecutar la operación de división con un denominador 0.")
        except (TypeError, NameError):
            print("Ocurrió un error fatal. Vuelve a intentarlo.")
        else:
            historial.append({
                "Operacion": opcion,
                "A": a,
                "B": b,
                "Resultado": resultado
            })

            print([h["Resultado"] for h in historial])

            print(f"#=> {resultado}")

            graficar_historial(historial)

            producir_archivo("historial.csv", historial)
        finally:
            print("El programa continua")