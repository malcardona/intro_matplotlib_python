# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt

def two_plt(x, xlabel, y1, y2, ylabel, title, label1, label2):
    # general
    fig = plt.figure()
    fx = fig.add_subplot()
    fx.set_title(title, fontsize=16)
    fx.set_facecolor('whitesmoke')
    fx.set_ylabel(ylabel)
    fx.set_xlabel(xlabel)

    #plot 1
    fx.plot(x, y1, color='b', marker='^', label=label1)
    #plot 2
    fx.plot(x, y2, color='c', marker='+', label=label2)
    fx.legend()
    plt.show()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot")

    # NOTA: aproveche los ejemplos "multi_line_plot" de clase

    # Alumno: Se desea graficar varias funciones en un mismmo gráfico (fige)

    # Las funciones que se desean implementar y graficar son:
    # y1 = x**2
    # y2 = x**3

    # Su implementación es la siguiente:
    x = list(np.linspace(-4, 4, 20))

    y1 = []
    for i in x:
        y1.append(i**2)

    y2 = []
    for i in x:
        y2.append(i**3)

    # Realizar un gráfico que representen las dos funciones
    # Para ello se debe llamar dos veces a "plot" con el mismo "fig"

    # Se debe colocar en la leyenda la función que representa
    # cada función

    # Cada función dibujarla con un color distinto
    # a su elección

    # Crear acá su gráfico

    graf = two_plt(x, 'x', y1, y2, 'f(x)', 'Dos Funciones', 'y**2', 'y**3')

    print("terminamos")