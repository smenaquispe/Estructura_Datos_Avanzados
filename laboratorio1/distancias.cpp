#include<iostream>
#include<random>
#include<vector>
#include<fstream>

using namespace std;

struct Punto {
    float x;
    float y;
};

float distancia_euclidiana(const Punto * a, const Punto * b) {
    return sqrt(pow(a->x - b->x, 2) + pow(a->y - b->y, 2));
}

int main(int argc, char * argv[]) {

    int cant = atoi(argv[1]);

    random_device rd;
    mt19937 gen(rd());

    uniform_real_distribution<> dis(0, 1.0);

    vector<Punto> puntos;

    for(int i = 0; i < cant; i++) {
        float x = dis(gen);
        float y = dis(gen);

        puntos.push_back({x, y});
    }


    vector<float> distancias;

    for(int i = 0; i < cant; i++) {
        Punto * punto_actual = &puntos[i];
        for(int j = i + 1; j < cant; j++) {
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