''' Funcao que extrai os cliques maximais de um grafo 
		
		Variaveis de entrada:	um grafo 
		Variaveis de saida:		uma lista com os cliques maixmais do grafo			'''

def clique_maximal(grafo):
  # Selecionar os cliques maximais do grafo da relacao entre genes (pathways)
	cliques_maximais = []
	cliques_maximais = grafo.maximal_cliques(min = 2, max = 0)
	
	return cliques_maximais
