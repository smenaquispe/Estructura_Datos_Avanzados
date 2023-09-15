import matplotlib.pyplot as plt
import os
import time

def histograma(datos, bins, titulo, x, y):
    plt.hist(datos, bins)
    plt.title(titulo)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()

def main():

    if not os.path.exists("distancias.exe"):    
        os.system("g++ distancias.cpp -o distancias.exe")

    cant = input("Cantidad de numeros aleatorios: ")
    os.system("distancias.exe " + str(cant))
    
    time.sleep(1)

    with open("distancias.txt") as archivo:
        datos = []
        for linea in archivo:
            datos.append(float(linea))
    
    histograma(datos, 10, "Distancia de los planetas al sol", "Distancia", "Frecuencia")

if __name__ == "__main__":
    main()