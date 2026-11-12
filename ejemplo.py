import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(8, 8))

xs = [0,1,2,3,4,5,6,7,8,9]
ys = [0,1,2,3,4,5,6,7,8,9]
ax1.plot(xs, ys, label="Funcion lineal $y=x$")

xs2 = range(-10, 11)
ys2 = [x**2 for x in xs2]
ax2.plot(xs2, ys2, marker="o", linestyle="-", label="step = 1")

xs3 = np.arange(-10, 10, 0.1)
ys3 = [x**2 for x in xs3]
ax2.plot(xs3, ys3, marker="+", linestyle="-", label="step = 0.1")

xs4 = np.linspace(-10, 10, 1000)
ys4 = xs4 ** 2
ax2.plot(xs4, ys4, linestyle="-", label="continua")

xs5 = xs4
ys5 = np.sin(xs4)
ax1.plot(xs5, ys5, linestyle="-", label="Función de seno $y=\\sin{x}$")

ax1.plot(xs5, [1] * 1000, linestyle="-")
ax1.plot(xs5, [-1] * 1000, linestyle="-")

ax1.set_title("Funciones varias")
ax1.set_xlabel("Eje X")
ax1.set_ylabel("Eje Y")
ax1.legend()

ax2.set_title("Función cuadrática $y=x^2$")
ax2.set_xlabel("Eje X")
ax2.set_ylabel("Eje Y")
ax2.set_xlim(-10,10)
ax2.set_ylim(0,10)
ax2.legend()
ax2.grid(True)

categorias = ["Suma", "Resta", "Multiplicacion"]
conteos = [20, 22, 89]

ax3.pie(conteos, labels=categorias, autopct="%1.1f%%")
ax2.set_title("Grafica de barras")
ax2.set_xlabel("Eje X")
ax2.set_ylabel("Eje Y")
ax2.legend()
ax2.grid(True)


plt.tight_layout()
plt.savefig("grafica.png")