/*
    Para os desenvolvedores:
    
    Bons caminhos:
        *   Se usar IA durante a construção do código, por favor, cite;
        *   Mantenha a arquitetura prevista do projeto;
        *   Faça comentários breves.
    

    Para compilar:
        gcc -std=c11 -o builds/atividade src/atividade-um.c
        

    Para executar (exemplo de arquivo .csv):
        builds/atividade input/dis-csv-discentes-de-graduacao-de-2026.csv


    ass. Francisco
*/


// Importando as bibliotecas necessárias para o programa
#include <stdlib.h>
#include <stdio.h>

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

void percorrer_linhas();
void imprimir_discente(struct Registros* registros, int quantidade, long long int matricula);
void salvar();
void mainProcess();



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

void imprimir_discente(struct Registros* registros, int quantidade, long long int matricula){
    /*
    função para imprimir os dados do discente no terminal,
    caso a matricula não seja encontrada, a função deve gerar um erro.
    */

    for(int i = 0; i < quantidade; i++){
        if (registros[i].matricula == matricula){ 
            printf("Discente: %s(%lld)\n", registros[i].nome_discente, registros[i].matricula);
            printf("Periodo de ingresso: %d/%d\n", registros[i].ano_ingresso, registros[i].periodo_ingresso);
            printf("Tipo de discente: %s\n", registros[i].tipo_discente);
            printf("Status do discente: %s\n", registros[i].status_discente);
            printf("Nivel de ensino: %s\n", registros[i].nivel_ensino);
            printf("Curso: %s\n", registros[i].nome_curso);

            return;
        }
    }
    printf("Erro: Matrícula não encontrada.\n");

}

void salvar(){
    
}

/*
void mainProcess(){
    percorrer_linhas();
    imprimir_discente();
}
*/