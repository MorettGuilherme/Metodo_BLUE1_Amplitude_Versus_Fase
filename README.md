A primeira versão do método Melhor Estimador Linear Não Enviesado (BEst Linear Blue Estimador - BLUE 1) tem o objetivo de encontrar um vetor de parâmetro estimados, cujos componentes são respectivamente: amplitude, amplitude vezes a fase e pedestal.
Nesse repositório, o algoritmo foi desenvolvido para o cálculo do esrro de estimação do termo da amplitude versus a fse pela técnica de validação cruzada K-Fold.
Comentários sobre os resultados: de acordo com a análise estatística pelo K-Fold notou-se que o janelamento 15 pode ser considerado como ideal para a estimação do erro do termo da amplitude versus a fase. 
Obs.: o comportamento do desvio padrão do termo da amplitude versus a fase foi conforme o esperado. Entretento, há dispersão dos dados em relação a média continua alta.

A seguir são listadas as pastas e também os arquivos contidos nesse repositório, assim como suas respectivas funções:

1. Dados_Estatisticos_BLUE1_amplitude_versus_fase_OC
  * Essa pasta contém arquivos para cada um dos janelamento com os valores das ocupações e médias, variâncias e desvios padrões associados para o erro de estimação da amplitude.
  
2. Dados_Ocupacoes_Free_Running
  * Essa pasta contém arquivos com os dados para cada uma das ocupações referentes ao pulso de sinal, amplitude de referência, fase de referência e ruído computados a cada 25 ns (perído das colisões no LHC).
  
3. K_Fold_amplitude_versus_fase_DP_Dados_Estatisticos_BLUE1_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão dos desvios padrão dos erros de estimação da amplitude calculados pela técnica de validação cruzada K-Fold.

4. K_Fold_amplitude_versus_fase_media_Dados_Estatisticos_BLUE1_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação da amplitude calculados pela técnica de validação cruzada K-Fold.

5. K_Fold_amplitude_versus_fase_variancia_Dados_Estatisticos_BLUE1_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das variâncias dos erros de estimação da amplitude calculados pela técnica de validação cruzada K-Fold.

6. Resultados_BLUE1_Amplitude_versus_fase
   * Essa pasta com os gráficos dos dados estatísticos (média, variância e desvio padrão) para o erro de estimação da amplitude pela técnica da validação cruzada K-Fold, assim como os histogramas para cada janelamento e ocupações.
   
7. arquivo arquivo_saida_dados_estatisticos_blue1_amplitude_versus_fase.py
   * Função para o cálculo dos dados estatísticos do erro de estimação pelo método Best Linear Unbiased Estimator (BLUE 1).
   * Instrução para salvar os dados estatísticos do erro de estimação da amplitude, fase ou pedestal para determinada ocupação em um arquivo de saída.
   * Instrução principal do código.
   
8. arquivo grafico_dado_estatistico_janelamento_blue1_amplitude_versus_fase.py
   * Função para a leitura dos dados estatísticos de todas as ocupações para um determinado janelamento.
   * Instrução para o plote do gráfico do dado estatístico ao longo das ocupações para um determinado janelamento.
   * Instrução principal do código.

9. arquivo grafico_k_fold_blue1_amplitude_versus_fase.py
   * Função para a leitura dos dados estatísticos da validação cruzada K-Fold.
   * Instrução para a construção do gráfico tipo A da validação cruzada K-Fold.
   * Instrução para a construção do gráfico tipo B da validação cruzada K-Fold.
   * Instrução principal (main) do código.
   
10. arquivo histograma_erro_amplitude_versus_fase_blue1.py
   * Função para o cálculo da estatística do erro de estimação da amplitude, fase ou pedestal.
   * Função para o plote do histograma do erro de estimação da amplitude, fase ou pedestal.
   * Função principal.
   
11. arquivo k_fold_blue1_amplitude_versus_fase.py
   * Instrução para salvar em arquivos os dados estatísticos pela validação cruzada k-Fold.
   * Instrução da validação cruzada K-Fold.
   * Instrução principal do código.
   
12. arquivo leitura_dados_ocupacao_blue1_amplitude_versus_fase.py
   * Função para a leitura dos dados de ocupação.
   * Função para a retirada do pedestal dos pulsos de sinais.
   * Função para a construção da matriz dos pulsos de sinais e o vetor do parâmetro de referência.
   * Função para separação em dados de treino e teste.

13. arquivo leitura_dados_ruidos_blue1_amplitude_versus_fase.py
   * Função para a leitura dos dados de ruídos de acordo com a ocupação.
   * Função para a organização dos dados de ruídos de acordo com o janelamento.
   * Função para separação em dados de treino e teste.
   * Função para a construção da matriz de covariância.
   * Função para a construção da matriz de covariância como identidade.

14. arquivo metodo_blue1_amplitude_versus_fase.py
   * Função para a definição do vetor pulso de referência.
   * Função para a definição do vetor da derivada temporal do pulso de referência.
   * Função para o método BLUE 1.
   
IMPORTANTE: os dados das ocupações foram simulados computacionalmente. As características das distribuições são:

* Distribuição amplitude: exponencial com média 100 ADC Count.
* Distribuição Fase: uniforme com números inteiros no intervalo de -5 a 5 ns.
* Pedestal: 30 ADC Count.
* Nível de deformação: 0,01 ADC Count.
* Número de eventos: 2000000.
* Fold: 100.
* Os dados de ruídos para a construção da matriz de covariância foram os mesmo que para os pulsos de sinais.
