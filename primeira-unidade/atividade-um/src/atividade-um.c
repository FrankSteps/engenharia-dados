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
#include <string.h>

struct Registros{
    char matricula[15];
    char nome_discente[256];
    char ano_ingresso[10];
    char periodo_ingresso[5];
    char tipo_discente[15];
    char status_discente[10];
    char nivel_ensino[15];
    char nome_curso[256];
    char modalidade_educacao[15];
    char nome_unidade[256];
    char nome_unidade_gestora[256];
};

void percorrer_linhas(FILE* inp, struct Registros* registros);
void imprimir_discente(struct Registros* registros, int quantidade, long long int matricula);
void salvar();



//Função principal que executa os métodos de leitura e escrita dos dados
int main(int argc, char* argv[]){
    
    struct Registros* dados_alunos = (struct Registros*) malloc(sizeof(struct Registros) * 10000);

    FILE* input = fopen(argv[1], "r");
    FILE* output = fopen(argv[2], "w");
    char buffer[1024]; //Buffer global

    if(input == NULL || output == NULL){
        printf("Erro, Arquivos insuficientes\n");
        printf("Programa encerrado");
    }
    else{
        fgets(buffer, sizeof(buffer), input); //Começa a ler a partir da segunda linha em diante
        percorrer_linhas(input, dados_alunos);
        printf("%s", dados_alunos[642].nome_unidade);
        fclose(input);
        free(dados_alunos);
    }

    return 0;
}

void percorrer_linhas(FILE* inp, struct Registros* registros){
    
    char word[1024];
    int qtd = 0;
    char* token;

    while(fgets(word, sizeof(word), inp) != NULL)
    {
        //Remove o \n
        word[strcspn(word, "\n")] = '\0';

        //Trata aspas
        for(int j = 0; word[j] != '\0'; j++)
        {
            if(word[j] == '"')
            {
                memmove(&word[j], &word[j + 1], strlen(word) - j);
                j--;
            }
        }

        //Trata campos vazios
        for(int i = 0; i < strlen(word) - 1; i++)
        {
            if(word[i] == ',' && word[i + 1] == ',')
            {
                memmove(&word[i + 2],
                        &word[i + 1],
                        strlen(word) - i);

                word[i + 1] = ' ';
            }
        }

        //Separa os campos
        token = strtok(word, ",");

        if(token != NULL)
            strcpy(registros[qtd].matricula, token);

        token = strtok(NULL, ",");
        if(token != NULL)
            strcpy(registros[qtd].nome_discente, token);

        token = strtok(NULL, ",");
        if(token != NULL)
            strcpy(registros[qtd].ano_ingresso, token);

        token = strtok(NULL, ",");
        if(token != NULL)
            strcpy(registros[qtd].periodo_ingresso, token);

        token = strtok(NULL, ",");
        if(token != NULL)
            strcpy(registros[qtd].tipo_discente, token);

        token = strtok(NULL, ",");
        if(token != NULL)
            strcpy(registros[qtd].status_discente, token);

        token = strtok(NULL, ",");
        if(token != NULL)
            strcpy(registros[qtd].nivel_ensino, token);

        token = strtok(NULL, ",");
        if(token != NULL)
            strcpy(registros[qtd].nome_curso, token);

        token = strtok(NULL, ",");
        if(token != NULL)
            strcpy(registros[qtd].modalidade_educacao, token);

        token = strtok(NULL, ",");
        if(token != NULL)
            strcpy(registros[qtd].nome_unidade, token);

        token = strtok(NULL, ",");
        if(token != NULL)
            strcpy(registros[qtd].nome_unidade_gestora, token);

        qtd++;
    }
}

/*void imprimir_discente(struct Registros* registros, int quantidade, long long int matricula){
    
    função para imprimir os dados do discente no terminal,
    caso a matricula não seja encontrada, a função deve gerar um erro.
    

    for(int i = 0; i < quantidade; i++){
        if (registros[i].matricula){ 
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

}*/

void salvar(){
    
}
