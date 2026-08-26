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
#include <stdlib.h>
#include <stdio.h>

void percorrer_linhas();
void imprimir_discente();
void salvar();
void mainProcess();

struct Registros{
    long long int matricula;
    char nome_discente[256];
    int ano_ingresso;
    int periodo_ingresso;
    char tipo_discente[10];
    char status_discente[9];
    char nivel_ensino[10];
    char nome_curso[128];
};


//Função principal que executa os métodos de leitura e escrita dos dados
int main(int argc, char* argv[]){
    
    struct Registros* dados_alunos = (struct Registros*) malloc(sizeof(struct Registros)*10);

    if(argc < 2){
        printf("Erro, Arquivos insuficientes");
    }
    else{
        mainProcess();

    }

    return 0;
}

void percorrer_linhas(){

}

void imprimir_discente(){

}

void salvar(){
    
}

void mainProcess(){
    percorrer_linhas();
    imprimir_discente();
}
