''' Funcao que utiliza os dados da relacao entre os genes para criar um grafo 
		
		Variaveis de entrada:	--
		Variaveis de saida:		um grafo da relacao entre os genes	'''
		
from igraph import *

def grafo_genes():	
	# Gerar o grafo a partir de um arquivo de relacao entre os genes
	grafo = Graph.Read_Edgelist('rede_filtrada.txt', directed=False)

	# Plotar o grafo
	#grafo.vs["color"] = "lightgreen"
	#layout = grafo.layout("kk")
	#plot(grafo, layout = layout)

	# Retornar o grafo
	return grafo