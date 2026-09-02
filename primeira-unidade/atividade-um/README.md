# RELATÓRIO DE DESENVOLVIMENTO DA PRIMEIRA ATIVIDADE PARA A PRIMEIRA UNIDADE

## Árvore de diretórios

```bash
atividade-um
├── builds      # executável
├── docs        # orientações em PDF do professor
│   └── Engenharia_de_Dados__-_Atividade_1-1.pdf
├── input       # arquivo que será passado como parâmetro de entrada
│   └── dis-csv-discentes-de-graduacao-de-2026.csv
├── output      # arquivo gerado pelo programa
├── src         # programa
│   └── atividade-um.c
├── makefile # arquivo para executar o programa
└── README.md
```

> 1° Nota: Matenha essa estrurura para o projeto
> 2° Nota: Atualize este README sempre que possível

# Modo de uso

```bash
Objetivo do programa: O objetivo do programa é pegar as informações de um arquivo.csv e
mandar para um arquivo.txt. É possível também buscar discentes através da matrícula.

Como executar: Para executar o programa é só abrir o terminal no diretório /atividade-um e rodar
 o comando "make run". Também é possível rodar o comando "make help" para abrir o painel com todos os comandos.

Modo de uso: O programa ira exportar todas as informações do arquivo.csv para um arquivo.txt. É possível também
procurar um discente expecifíco fornecendo a matrícula do mesmo no terminal quando solicitado. Para encerrar o
programa é só enviar ".." no mesmo campo onde é solicitado a matrícula.
```
