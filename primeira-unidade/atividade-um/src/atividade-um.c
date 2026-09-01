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


    Uso da inteligência artificial:
        Para este projeto, o uso da IA limitou-se à revisão, correção ortográfica de comentários, organização, planejamento do projeto e esclarecimento de dúvidas ao decorrer do desenvolvimento. 


    ass. Francisco
*/


// Bibliotecas necessárias para o programa
#include <stdlib.h>
#include <stdio.h>
#include <string.h>


// Estrutura dos dados
struct Registros{
    char matricula[15];                 // ID do aluno
    char nome_discente[256];            // Nome completo
    char ano_ingresso[10];              // Ano de ingresso
    char periodo_ingresso[5];           // Semestre de ingresso
    char tipo_discente[15];             // Tipo (Regular, PROEJA, etc)
    char status_discente[10];           // Ativo, Inativo, Egresso
    char nivel_ensino[15];              // Nível de ensino (Graduação, Pós graduação, etc)
    char nome_curso[256];               // Nome do curso
    char modalidade_educacao[15];       // Modalidade (Presencial, EAD, etc)
    char nome_unidade[256];             // Campus
    char nome_unidade_gestora[256];     // Órgão responsável
};


// Procedimentos
int percorrer_linhas(FILE* inp, struct Registros* registros);
void salvar(FILE* out, struct Registros* registros, int qntd);
void imprimir_discente(struct Registros* registros, int quantidade, long long int matricula);


// Procedimento principal que executa os métodos de leitura e escrita dos dados
int main(int argc, char* argv[]){
    
    struct Registros* dados_alunos = (struct Registros*) malloc(sizeof(struct Registros) * 10000);


    FILE* input = fopen(argv[1], "r");
    FILE* output = fopen(argv[2], "w");

    char buffer[1024]; //Buffer global

    int qntd;

    if(input == NULL || output == NULL){
        printf("Erro: Arquivos insuficientes\n");
        printf("Programa encerrado");
    }
    else{
        fgets(buffer, sizeof(buffer), input); //Começa a ler a partir da segunda linha em diante

        qntd = percorrer_linhas(input, dados_alunos);

        printf("Total de alunos: %d\n", qntd);
        printf("%s", dados_alunos[642].nome_unidade);

        salvar(output, dados_alunos, qntd);

        fclose(input);
        fclose(output);
        free(dados_alunos);
    }

    return 0;
}


// procedimento responsável por 
int percorrer_linhas(FILE* inp, struct Registros* registros){
    
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

    return qtd;
}


// Procedimento responsável por salvar os registros já formatados por pecorrer_linhas no arquivo txt
void salvar(FILE* out, struct Registros* registros, int qntd){
    fprintf(out, "Matricula, Nome, Ano de Ingresso, Periodo, Tipo, Status, Nivel, Curso, Modalidade, Unidade, Unidade Gestora\n");

    for(int i = 0; i < qntd; i++){
        fprintf(out, "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n",
            registros[i].matricula,                        
            registros[i].nome_discente,
            registros[i].ano_ingresso,
            registros[i].periodo_ingresso,
            registros[i].tipo_discente,
            registros[i].status_discente,
            registros[i].nivel_ensino,
            registros[i].nome_curso,
            registros[i].modalidade_educacao,
            registros[i].nome_unidade,
            registros[i].nome_unidade_gestora
        );
    }

    printf("Arquivo salvo com sucesso! Todal de registros: %d\n", qntd);
}


// Procedimento para imprimir o discente desejado no terminal 
void imprimir_discente(struct Registros* registros, int quantidade, long long int matricula){

}