/*
    Para os desenvolvedores:
    
    Bons caminhos:
        *   Se usar IA durante a construção do código, por favor, cite;
        *   Mantenha a arquitetura prevista do projeto;
        *   Faça comentários breves.
    

    Para compilar:
        g++ atividade-um.cpp -o builds/atividade
        

    Para executar (exemplo de arquivo .csv):
        builds/atividade input/dis-csv-discentes-de-graduacao-de-2026.csv


    ass. Francisco
*/


// Importando as bibliotecas necessárias para o programa
#include <iostream>
#include <fstream>
#include <string>



// Função principal completa com os parâmetros definidos para leitura de um arquivo que será passado como argumento para o programa
int main(int argc, char* argv[]){
    
    // Para a execução do programa caso o arquivo passado como argumento não exista
    if(argc < 2){
        std::cerr << "Erro: atividade caminho/para/o/arquivo.csv";
        return EXIT_FAILURE;
    }    

    // Pega o nome do primeiro arquivo passado como argumento
    std::string arquivo = argv[1];


    // Para a execução do programa caso o arquivo passado como argumento para o mesmo não seja csv
    if(arquivo.substr(arquivo.length() - 4) != ".csv"){
        std::cerr << "Erro: Apenas arquivos .csv são permitidos";
        return EXIT_FAILURE;
    }

    // abrindo o arquivo dentro do programa para ser possível realizar as operações
    std::ifstream file(arquivo);


    // Finaliza a execução programa
    return EXIT_SUCCESS;
}