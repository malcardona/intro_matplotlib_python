# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt

def nxn_plt(x, xlabel, y1, label1, y2, label2, y3, label3, y4, label4, ylabel, title):
    # general
    fig = plt.figure()
    fig.suptitle(title, fontsize=16)
    fig.set_facecolor('whitesmoke')
    
    #grid 4x4
    fx1 = fig.add_subplot(2, 2, 1)
    fx2 = fig.add_subplot(2, 2, 2)
    fx3 = fig.add_subplot(2, 2, 3)
    fx4 = fig.add_subplot(2, 2, 4)

    #graf1
    fx1.scatter(x, y1, color='b', marker='^', label=label1)
    fx1.set_ylabel(ylabel)
    fx1.legend()
    #graf2
    fx2.scatter(x, y2, color='c', marker='*', label=label2)
    fx2.legend()
    #graf3
    fx3.scatter(x, y3, color='g', marker='.', label=label3)
    fx3.set_ylabel(ylabel)
    fx3.set_xlabel(xlabel)
    fx3.legend()
    #graf4
    fx4.scatter(x, y4, color='k', marker='+', label=label4)
    fx4.set_xlabel(xlabel)
    fx4.legend()
    plt.show()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot: Figura con múltiples gráficos")

    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Alumnos: Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(-10, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Esos cuatro gráficos deben estar colocados
    # en la diposición de 2 filas y 2 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección

    # Crear acá su gráfico

    grafico = nxn_plt(x, 'x', y1, 'x**2', y2, 'x**3', y3, 'x**4', y4, 'raiz(x)', 'f(x)', 'Figura con múltiples gráficos')

    print("terminamos")
