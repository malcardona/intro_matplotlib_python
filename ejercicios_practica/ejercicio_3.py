# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt

def scat(x, xlabel, y1, ylabel, title, label1):
    # general
    fig = plt.figure()
    fx = fig.add_subplot()
    fx.set_title(title, fontsize=16)
    fx.set_facecolor('whitesmoke')
    fx.set_ylabel(ylabel)
    fx.set_xlabel(xlabel)

    #plot
    fx.scatter(x, y1, color='b', marker='^', label=label1)
    fx.legend()
    plt.show()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Scatter Plot")

    # NOTA: aproveche los ejemplos "scatter_plot" de clase

    # Alumnos: Se desea graficar la función tanh para el siguiente
    # intervalor de valores de "X"
    x = np.arange(-np.pi, np.pi, 0.1)

    # Función y = tanh(x) --> tangente hiperbólica
    y = np.tanh(x)

    # Graficar la función utilizando "scatter"
    # utilizando "x" e "y"

    # Colocar la leyenda y el label con el nombre de la función

    # Elegir un marker a elección

    # Crear acá su gráfico

    disper = scat(x, 'x', y, 'f(x)', 'Scatter Plot', 'tan(x)')

    print("terminamos")