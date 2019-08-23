''' Funcao que retorna o P valor 

		Variaveis de entrada:	uma lista com as somas de P, uma lista com os pathways, o numero de iteracoes do laco de repeticao, 
                          o dicionario de mutacoes e o grafo dos eventos 
		Variaveis de saida:		uma lista com todos os P valores 	'''

import Menos_Informativos
import Redes_Aleatorias

def cliques_significativos(P, pathways, iteracoes, dicionario_mutacoes, grafo_eventos):

  for aux in range (len(P)):
    P[aux] = P[aux] / (iteracoes)
    while(P[aux] > 0.05 and (len(pathways[aux])) > 2):
      pathways_aux = []
      pathways[aux] = Menos_Informativos.menos_informativos(pathways[aux], dicionario_mutacoes)
      pathways_aux.append(pathways[aux])
      aux1 = Redes_Aleatorias.redes_aleatorias(pathways_aux, dicionario_mutacoes, grafo_eventos)
      P[aux] = aux1[0][0] / aux1[1] 

  return P
      

  