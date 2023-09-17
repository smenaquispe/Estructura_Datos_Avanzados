import matplotlib.pyplot as plt
import os
import time
import numpy as np

def histograma(datos, titulo, x, y, nombre):
    
    bins = 10
    
    plt.hist(datos, bins)
    plt.title(titulo)
    plt.xlabel(x)
    plt.ylabel(y)

    plt.savefig("./images/" + str(nombre) + ".png")

    plt.close()

def main():

    if not os.path.exists("distancias.exe"):    
        os.system("g++ distancias.cpp -o distancias.exe")

    dimensiones = [10, 50, 100, 500, 1000, 2000, 5000]

    for d in dimensiones:
        os.system("distancias.exe " + str(d))
        time.sleep(1)

        with open("distancias.txt") as archivo:
            datos = []
            for linea in archivo:
                datos.append(float(linea))
    
        histograma(datos, f"Distancia entre puntos de dimension {d}", "Distancia", "Frecuencia", d)
        
        time.sleep(1)

if __name__ == "__main__":
    main()