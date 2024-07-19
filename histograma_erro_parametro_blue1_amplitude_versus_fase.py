# EXPERIMENTO ATLAS - Reconstrução de sinal - Melhor Estimador Linear Não Enviesado - Best Linear Unbiased Estimator (BLUE 1) - Estimação da amplitude versus a fase.
# Autor: Guilherme Barroso Morett.
# Data: 16 de julho de 2024.

# Objetivo do código: análise do erro absoluto do parâmetro da amplitude versus a fase pelo método Best Linear Unbiased Estimator (BLUE 1).

"""
Organização do Código:

Importação de arquivos.
Método BLUE 1 formatado para o cálculo do termo da amplitude versus a fase: metodo_BLUE1_amplitude_versus_fase.py

Funções presentes:

1) Função para o cálculo da estatística do erro de estimação da amplitude versus a fase.
Entrada: lista com os erros de estimação da amplitude versus a fase.
Saída: a média, a variância e o desvio padrão do erro de estimação da amplitude versus a fase.

2) Instrução para o plote do histograma do erro de estimação da amplitude versus a fase.
Entrada: lista com os erros de estimação da amplitude versus a fase e seus dados estatísticos.
Saída: nada.

3) Instrução principal.
Entrada: nada.
Saída: nada.
"""

# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import os
from termcolor import colored

# Importação dos arquivos.
from metodo_BLUE1_amplitude_versus_fase import *

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Análise do erro de estimação da amplitude versus a fase pelo método Best Linear Unbiased Estimator (BLUE 1):\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### -------------------- 1) FUNÇÃO PARA O CÁLCULO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO DA AMPLITUDE VERSUS A FASE ----------------------- ###

# Definição da função para o cálculo dos dados estatísticos do erro de estimação da amplitude versus a fase.
def dados_estatisticos_BLUE1_erro_amplitude_versus_fase(lista_erro_amplitude_versus_fase):
    
    # A lista do erro de estimação da amplitude versus a fase é convertida para o tipo numpy array.
    vetor_erro_amplitude_versus_fase = np.array(lista_erro_amplitude_versus_fase)

    # Cálculo da média do erro de estimação da amplitude versus a fase.
    media_erro_amplitude_versus_fase = np.mean(vetor_erro_amplitude_versus_fase)

    # Cálculo da variância do erro de estimação da amplitude versus a fase.
    var_erro_amplitude_versus_fase = np.var(vetor_erro_amplitude_versus_fase)

    # Cálculo do desvio padrão do erro de estimação da amplitude versus a fase.
    desvio_padrao_erro_amplitude_versus_fase = np.std(vetor_erro_amplitude_versus_fase)
    
    # A função retorna a média, a variância e o desvio padrão dos dados do erro de estimação da amplitude versus a fase.
    return media_erro_amplitude_versus_fase, var_erro_amplitude_versus_fase, desvio_padrao_erro_amplitude_versus_fase
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ----------------------- 2) INSTRUÇÃO PARA A CONSTRUÇÃO DO HISTOGRAMA DO ERRO DE ESTIMAÇÃO DA AMPLITUDE VERSUS A FASE -------------------------- ###

# Definição de instrução para o plot do histograma do erro de estimação da amplitude versus a fase.
def histograma_BLUE1_erro_amplitude_versus_fase(n_ocupacao, lista_erro_amplitude_versus_fase, media_erro_amplitude_versus_fase, var_erro_amplitude_versus_fase, desvio_padrao_erro_amplitude_versus_fase):
    
    # A lista do erro de estimação da amplitude versus fase é convertida para o tipo numpy array.
    vetor_erro_amplitude_versus_fase = np.array(lista_erro_amplitude_versus_fase)

    # Nomeação do eixo x de acordo com o termo da amplitude versus a fase.
    plt.xlabel(r'Erro de estimação de A$\tau$ (ADC Count x ns)', fontsize = 18)
        
    # Definição do tamanho dos números do eixo x.    
    plt.xticks(fontsize = 16)

    # Nomeação do eixo y.
    plt.ylabel('Número de eventos', fontsize = 18)
    
    # Definição do tamanho dos números do eixo y.
    plt.yticks(fontsize = 16)

    # A variável texto recebe uma string com as informações de interesse.
    texto = f"Média: {round(media_erro_amplitude_versus_fase, 6)} \n Variância: {round(var_erro_amplitude_versus_fase, 6)} \n Desvio padrão: {round(desvio_padrao_erro_amplitude_versus_fase, 6)}"

    # Comando para exibir o título do gráfico.
    #plt.title(f"Ocupação {n_ocupacao}", fontsize = 18)

    # Definição do histograma a partir do vetor vetor_erro_parametro.
    plt.hist(vetor_erro_amplitude_versus_fase, bins = 100, range = [-10000, 10000], edgecolor = 'black', linewidth = 1.2)
    
    # Posicionamento do texto no gráfico.
    plt.text(0.99, 0.98, texto, horizontalalignment = 'right',
    verticalalignment = 'top',
    transform = plt.gca().transAxes,
    bbox = dict(facecolor = 'white', alpha = 0.5),
    fontsize = 14)

    # Criação de grid.
    plt.grid()

    # Exibição do gráfico.
    plt.show()

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### -------------------------------------- 3) INSTRUÇÃO PRINCIPAL DO CÓDIGO (MAIN) ------------------------------------------------------------- ###

# Definição da instrução principal (main) do código.
def principal_histograma_BLUE1_erro_amplitude_versus_fase():
    
    # A variável parametro recebe a string "amplitude_versus_fase".
    parametro = "amplitude_versus_fase"
    
    # A variável n_ocupacao armazena o valor digitado da ocupação desejada no terminal pelo usuário.
    n_ocupacao = float(input("Digite o valor da ocupação desejada: "))

    # A variável valores_ocupacao é uma lista com os valores aceitáveis de ocupação de 0 até 100 com incremento de 10.
    valores_ocupacao = list(range(0,101,10))

    # Caso o valor digitado armazenado na variável numero_ocupacao não estiver presente na lista valores_ocupacao.
    if n_ocupacao not in valores_ocupacao:
    
        # Exibição de uma mensagem de alerta de que a ocupação solicitada é inválida.
        print("\nNúmero de ocupação inválida!\n")
        # A execução do programa é interrompida.
        exit(1) 

    # O tipo da variável n_ocupacao é convertida para inteiro.
    # Obs.: essa conversão possibilita que a leitura do arquivo possa ser feita corretamente.
    n_ocupacao = int(n_ocupacao)
    
    # A variável n_janelamento armazena a quantidade de janelamento especificada no terminal pelo usuário.
    n_janelamento = int(input("Digite a quantidade de janelamento: "))

    # A variável valores_janelamento é uma lista com os valores aceitáveis do janelamento de 7 até 19 com incremento de 2.
    valores_janelamento = list(range(7,20,2))

    # Caso o valor digitado armazenado na variável n_janelamento não estiver presente na lista valores_janelamento.
    if n_janelamento not in valores_janelamento:
    
        # Exibição de uma mensagem de alerta de que a quantidade de janelamento solicitada é inválida.
        print("Quantidade de janelamento inválida! Opções de janelamento: 7, 9, 11, 13, 15, 17, 19.")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
        
    # Chamada ordenada das funções.
    
    Matriz_Dados_OC = leitura_dados_ocupacao(n_ocupacao)
    
    Matriz_Dados_OC_Sem_Pedestal = retirada_pedestal(Matriz_Dados_OC)
    
    vetor_amostras_pulsos, vetor_amplitude_referencia, vetor_fase_referencia = amostras_pulsos_e_referencia(Matriz_Dados_OC_Sem_Pedestal)
        
    Matriz_Pulsos_Sinais, vetor_amplitude_referencia = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento)
        
    Matriz_Pulsos_Sinais, vetor_fase_referencia = amostras_janelamento(vetor_amostras_pulsos, vetor_fase_referencia, n_janelamento)
              
    Matriz_Pulsos_Sinais_Treino, Matriz_Pulsos_Sinais_Teste, vetor_amplitude_referencia_treino, vetor_amplitude_referencia_teste = dados_treino_teste_histograma(Matriz_Pulsos_Sinais, vetor_amplitude_referencia)
    
    Matriz_Pulsos_Sinais_Treino, Matriz_Pulsos_Sinais_Teste, vetor_fase_referencia_treino, vetor_fase_referencia_teste = dados_treino_teste_histograma(Matriz_Pulsos_Sinais, vetor_fase_referencia)
    
    lista_erro_estimacao_amplitude_versus_fase = metodo_BLUE1_amplitude_versus_fase(Matriz_Pulsos_Sinais_Treino, Matriz_Pulsos_Sinais_Teste, vetor_amplitude_referencia_teste, vetor_fase_referencia_teste, n_janelamento)
    
    media_erro_estimacao_amplitude_versus_fase, var_erro_estimacao_amplitude_versus_fase, desvio_padrao_erro_estimacao_amplitude_versus_fase = dados_estatisticos_BLUE1_erro_amplitude_versus_fase(lista_erro_estimacao_amplitude_versus_fase)
    
    histograma_BLUE1_erro_amplitude_versus_fase(n_ocupacao, lista_erro_estimacao_amplitude_versus_fase, media_erro_estimacao_amplitude_versus_fase, var_erro_estimacao_amplitude_versus_fase, desvio_padrao_erro_estimacao_amplitude_versus_fase)
    
# Chamada da função principal (main) do código.
principal_histograma_BLUE1_erro_amplitude_versus_fase()

### -------------------------------------------------------------------------------------------------------------------------------------------- ###
# Impressão de uma linha que representa o fim do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

