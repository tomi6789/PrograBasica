import matplotlib.pyplot as plt
import numpy as np

from matematicas.graficas.barras import barras
from matematicas.graficas.pastel import pastel
from matematicas.estadistica.frequencia import frequencias

operaciones = {
    "barras": barras,
    "pastel": pastel,
}

def generar_figuras():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))
    return ax1, ax2

def graficar_historial(historial, nombre="grafica_sesion.png"):
    operaciones = [operacion["Operacion"] for operacion in historial]

    frequencias_operaciones = frequencias(operaciones)

    fig_pastel, fig_barras = generar_figuras()
    
    pastel(fig_pastel, frequencias_operaciones.keys(), frequencias_operaciones.values())
    barras(fig_barras, frequencias_operaciones.keys(), frequencias_operaciones.values())

    fig_barras.set_title("Grafica de Barras")
    fig_barras.set_xlabel("Operaciones")
    fig_barras.set_ylabel("Frecuencia")

    fig_pastel.set_title("Grafica de Pastel")

    plt.savefig(nombre)
