################################################################################
# Sobre este arquivo
################################################################################
# Este Makefile foi gerado com assistência do Claude (Haiku 4.5) da Anthropic.
# O código foi revisado, verificado e aprovado por um desenvolvedor humano com 
# conhecimentos prévios.
#
# Desenvolvedor responsável: Francisco (FrankSteps)
# Data de criação: 2026-09-01
#
# Disclaimer: O desenvolvedor humano assume total responsabilidade pelo uso e
# manutenção deste arquivo. A IA foi utilizada como ferramenta assistiva para
# geração e otimização, mas todas as decisões finais foram tomadas pelo humano.
################################################################################

# Compilador e flags
CC = gcc
CFLAGS = -std=c11 -Wall -Wextra -O2
LDFLAGS = 

# Diretórios
SRC_DIR = src
BUILD_DIR = builds
INPUT_DIR = input
OUTPUT_DIR = output

# Arquivos
TARGET = $(BUILD_DIR)/atividade
SOURCE = $(SRC_DIR)/atividade-um.c
CSV_INPUT = $(INPUT_DIR)/dis-csv-discentes-de-graduacao-de-2026.csv
TXT_OUTPUT = $(OUTPUT_DIR)/output.txt

# Targets
.PHONY: all clean run help

# Build padrão
all: $(TARGET)

# Compilação
$(TARGET): $(SOURCE)
	@mkdir -p $(BUILD_DIR)
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)
	@echo "Compilado com sucesso: $@"

# Execução
run: $(TARGET)
	@echo "Executando programa..."
	@mkdir -p $(OUTPUT_DIR)
	$(TARGET) $(CSV_INPUT) $(TXT_OUTPUT)

# Limpeza
clean:
	@rm -rf $(BUILD_DIR)
	@echo "Arquivos de build removidos"

# Limpeza completa (inclui output)
distclean: clean
	@rm -rf $(OUTPUT_DIR)/output.txt
	@echo "Limpeza completa realizada"

# Ajuda
help:
	@echo "Targets disponíveis:"
	@echo "  make all       - Compila o programa"
	@echo "  make run       - Compila e executa"
	@echo "  make clean     - Remove arquivos de build"
	@echo "  make distclean - Remove build e output"
	@echo "  make help      - Mostra esta mensagem"