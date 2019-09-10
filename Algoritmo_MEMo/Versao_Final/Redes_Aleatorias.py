''' Funcao que faz as operacoes necessarias para encontrar o p valor
    
    Variaveis de entrada:	uma lista com os pathways, o dicionario de mutacoes e o grafo de eventos 
	  Variaveis de saida:		uma lista contendo as somas que serao usadas no calculo final de P valor e uma variavel 
  com a quantidade de iteracoes do laco de repeticao	'''

from igraph import *
import Permutacao_Comutacao

# Constante do algoritmo
N = 10000

def redes_aleatorias(pathways, dicionario_mutacoes_original, grafo_eventos_original):
  P_valor = []
  pacientes_mutados_dados_reais = []

  # Encontrando o P valor para cada um dos pathways (modulo X) da matriz de dados reais
  verificacao_dados_reais = []
  for aux1 in range (len(pathways)):
    P_valor.append(0)
    pacientes_mutados_dados_reais.append(0)
    aux5 = 0
    for aux2 in pathways[aux1]:
      for aux3 in dicionario_mutacoes_original[str(aux2)]:
        verificacao_dados_reais.append(aux3)
    for aux4 in verificacao_dados_reais:
      if(verificacao_dados_reais.count(aux4) == 1):
        pacientes_mutados_dados_reais[aux1] += 1
      if(verificacao_dados_reais.count(aux4) > 1 and aux5 == 0):
        pacientes_mutados_dados_reais[aux1] += 1
        aux5 += 1
	
  for aux6 in range(N):
    dicionario_mutacoes = Permutacao_Comutacao.permutacao_comutacao(dicionario_mutacoes_original, grafo_eventos_original)
    
    # Encontrando o P valor para cada um dos pathways
    verificacao_permutacoes = []
    pacientes_mutados_permutacoes = []
    for aux7 in range (len(pathways)):
      pacientes_mutados_permutacoes.append(0)
      aux8 = 0
      for aux9 in pathways[aux7]:
        for aux10 in dicionario_mutacoes[str(aux9)]:
          verificacao_permutacoes.append(aux10)
      for aux11 in verificacao_permutacoes:
        if(verificacao_permutacoes.count(aux11) == 1):
          pacientes_mutados_permutacoes[aux7] += 1
        if(verificacao_permutacoes.count(aux11) > 1 and aux8 == 0):
          pacientes_mutados_permutacoes[aux7] += 1
          aux8 += 1

      if(pacientes_mutados_permutacoes[aux7] >= pacientes_mutados_dados_reais[aux7]):
        P_valor[aux7] += 1
        
  lista_retorno = []
  lista_retorno.append(P_valor)
  lista_retorno.append(N)
  return lista_retorno

  
