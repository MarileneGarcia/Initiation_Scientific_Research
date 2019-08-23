''' Funcao que estrutura o algoritmo MEMo (Mutual Exclusivity Modules in cancer)
	
    Variaveis de entrada:	 tres arquivos, um com os genes mutados nos pacientes (maf) um com a relacao entre os genes (HRN)
                             e um com os genes filtrados
	Variaveis de saida:		--- 	'''

import Filtragem_Dados
import time
import Grafo_Genes
import Clique_Maximal
import Nos_Informativos
import Grafo_Eventos
import Redes_Aleatorias
import Cliques_Significativos
import Resultados

def MEMo(nome_arquivo_maf, nome_arquivo_redes, nome_arquivo_genes_filtados):
    
# Etapas 1 e 2:
    # Construir uma matriz de eventos (genes mutados em cada paciente) e 
    # criar o arquivo da rede usando o coeficiente de Jaccard
    aux1 = Filtragem_Dados.filtragem_dados(nome_arquivo_maf, nome_arquivo_redes, nome_arquivo_genes_filtados)
    nome_genes = aux1[0]
    dicionario_nome_genes = aux1[1]

# Etapa 3:
    # Construir um grafo da relacao entre os genes
    grafo_genes = Grafo_Genes.grafo_genes()
    
    # Extrair os cliques maximais do grafo
    pathways = Clique_Maximal.clique_maximal(grafo_genes)

    # Excluir os nos não informativos
    aux2 = Nos_Informativos.nos_informativos(pathways, nome_genes)
    pathways = aux2[0]
    dicionario_mutacoes = aux2[1]
    matriz_eventos = aux2[2]

# Etapa 4:
    #Construir um grafo bipartido com dois conjuntos de nos, um representado os genes e outros as amostras
    grafo_eventos = Grafo_Eventos.grafo_eventos(matriz_eventos, nome_genes)
    
    # Gerar as redes aleatorias para o grafo dos eventos
    aux3 = Redes_Aleatorias.redes_aleatorias(pathways, dicionario_mutacoes, grafo_eventos)
    P_valor = aux3[0]
    iteracoes = aux3[1]

    # Calcular o P valor de cada pathway
    P_valor = Cliques_Significativos.cliques_significativos(P_valor, pathways, iteracoes, dicionario_mutacoes, grafo_eventos)
    # Salvando os resultados
    Resultados.resultados(dicionario_nome_genes, pathways, P_valor)