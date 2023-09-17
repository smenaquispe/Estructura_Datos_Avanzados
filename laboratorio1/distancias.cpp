#include<iostream>
#include<random>
#include<vector>
#include<fstream>

using namespace std;

struct Punto {
    vector<float> coordenadas;
    Punto(int dimension) {
        coordenadas = vector<float>(dimension);
    }
};

float distancia_euclidiana(const Punto * a, const Punto * b) {
    double distancia = 0.0;
    for (size_t i = 0; i < a->coordenadas.size(); i++) {
        double diff = a->coordenadas[i] - b->coordenadas[i];
        distancia += diff * diff;
    }
    return sqrt(distancia);
}

int main(int argc, char * argv[]) {

    int cant_dimensiones = atoi(argv[1]);
    const int cant_numeros = 100;

    random_device rd;
    mt19937 gen(rd());

    uniform_real_distribution<> dis(0, 1.0);

    vector<Punto> puntos;

    for(int i = 0; i < cant_numeros; i++) {
        Punto punto(cant_dimensiones);
        for(int j = 0; j < cant_dimensiones; j++) {
            punto.coordenadas[j] = dis(gen);   
        }
        puntos.push_back(punto);
    }


    vector<float> distancias;

    for(int i = 0; i < cant_numeros; i++) {
        Punto * punto_actual = &puntos[i];
        for(int j = i + 1; j < cant_numeros; j++) {
            Punto * punto_siguiente = &puntos[j];
            float distancia = distancia_euclidiana(punto_actual, punto_siguiente);
            distancias.push_back(distancia);
        }
    }

    ofstream archivo("distancias.txt");

    for(int i = 0; i < distancias.size(); i++) {
        archivo << distancias[i] << endl;
    }

    archivo.close();

    return 0;
}