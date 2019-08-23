''' Funcao que gera redes aleatorias no grafo dos eventos fazendo as permutacoes de comutacao 
    
    Variaveis de entrada:	o dicionario de mutacoes e o grafo de eventos 
	  Variaveis de saida:		o dicionario de mutacoes apos a permutacoes de comutacao	'''

from random import randint
from igraph import *
import copy

# Constante do algoritmo
Q = 100 

def permutacao_comutacao(dicionario_mutacoes_original, grafo_eventos_original):
  dicionario_mutacoes = deepcopy(dicionario_mutacoes_original)
  grafo_eventos = deepcopy(grafo_eventos_original)

# Definindo a permutacao de comutacao 
  A = grafo_eventos.ecount() # numero total de arestas
  for n in range( Q*A ):
    
    arestas = grafo_eventos.get_edgelist() 
    aresta_aleatoria_ab = randint(0, len(arestas) - 1)
    aresta_aleatoria_cd = randint(0, len(arestas) - 1)
    
    while(aresta_aleatoria_cd == aresta_aleatoria_ab):
       aresta_aleatoria_cd = randint(0, len(arestas) - 1)
    
    a = arestas[aresta_aleatoria_ab][0]
    b = arestas[aresta_aleatoria_ab][1]

    c = arestas[aresta_aleatoria_cd][0]
    d = arestas[aresta_aleatoria_cd][1]

    if(grafo_eventos.are_connected(a,d) == False and grafo_eventos.are_connected(c,b) == False):
      #grafo_eventos.es(grafo_eventos.get_eid(a,b))["color"] = ["orange"]
      grafo_eventos.delete_edges(grafo_eventos.get_eid(a,b))
      aux7 = dicionario_mutacoes [ str(grafo_eventos.vs[a]["name"]) ].index(str(grafo_eventos.vs[b]["name"]))
      del dicionario_mutacoes [ str(grafo_eventos.vs[a]["name"]) ][aux7]
    
      #grafo_eventos.es(grafo_eventos.get_eid(c,d))["color"] = ["green"]		
      grafo_eventos.delete_edges(grafo_eventos.get_eid(c,d))
      aux8 = dicionario_mutacoes [ str(grafo_eventos.vs[c]["name"]) ].index(str(grafo_eventos.vs[d]["name"]))
      del dicionario_mutacoes [ str(grafo_eventos.vs[c]["name"]) ][aux8]
    
      grafo_eventos.add_edge(a,d)
      dicionario_mutacoes[ str(grafo_eventos.vs[a]["name"]) ].append(str(grafo_eventos.vs[d]["name"]))
      grafo_eventos.add_edge(c,b)
      dicionario_mutacoes[ str(grafo_eventos.vs[c]["name"]) ].append(str(grafo_eventos.vs[b]["name"]))
      #grafo_eventos.es(grafo_eventos.get_eid(a,d))["color"] = ["red"]
      #grafo_eventos.es(grafo_eventos.get_eid(c,b))["color"] = ["blue"]
  
  return(dicionario_mutacoes)