#include <iostream>
#include <list>

class Carta{
    public:
        std::string palo;
        std::string valor;
};

class Mazo{
    public:
        std::list<Carta> generar_mazo(){
            const std::string palos[] = {"Corazones", "Diamantes", "Tréboles", "Picas"};
            const std::string valores[] = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"};

            std::list<Carta> mazo;

            for (const auto& palo : palos) {
                for (const auto& valor : valores) {
                    mazo.push_back(Carta{palo, valor});
                }
            }
            return mazo;
        }
};