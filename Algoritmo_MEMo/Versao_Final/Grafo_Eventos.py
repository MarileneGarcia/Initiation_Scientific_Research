''' Funcao que utiliza os dados da relacao dos genes mutados em cada paciente para gerar um grafo 
		
		Variaveis de entrada:	uma matriz referente ao arquivo dos genes mutados e uma lista do nome dos genes 
		Variaveis de saida:		um grafo da relacao dos eventos 	'''

import Numero_Genes
import Numero_Pacientes
from igraph import *

def grafo_eventos(matriz, nome_genes):
	numero_genes = Numero_Genes.numero_genes(nome_genes)
	numero_pacientes =  Numero_Pacientes.numero_pacientes()
	nome_genes_eventos = []
	
	# Utilizar os dados da matriz completa de eventos para montar uma matriz binaria em um arquivo 
	matriz_binaria = []
	with open ('matriz_binaria_eventos' , 'w') as arquivoDois:
		for indexUm in range (numero_genes):
			linha_matriz = []
			nome_genes_eventos.append(matriz[indexUm + 2][0])
			for indexDois in range (numero_pacientes):
				linha_matriz.append(int(matriz[indexUm + 2][indexDois + 1]))
				arquivoDois.write(matriz[indexUm + 2][indexDois + 1])
				arquivoDois.write(' ')		
			matriz_binaria.append(linha_matriz)
			arquivoDois.write('\n')
				
	# Gerar o grafo bipartido a partir de uma matriz binaria
	grafo = Graph.Incidence(matriz_binaria, directed = False, multiple = False)
	grafo.vs[0:(numero_genes)]["color"] = ["lightblue"] #genes
	grafo.vs[(numero_genes):(numero_pacientes + numero_genes)]["color"] = ["pink"] #pacientes
	
	# Nomear vertices 
	nome_vertices = []
	nome_vertices.extend(nome_genes_eventos)
	del matriz[0][0]
	nome_vertices.extend(matriz[0])	

	# Atribuir o nome dos vertices e a cor das arestas
	grafo.vs["name"] = nome_vertices
	grafo.vs["label"] = grafo.vs["name"]
	grafo.es["color"] = ["gray"]
	
	# Plotar o grafo bipartido 
	#layout = grafo.layout_bipartite(types="type", hgap=1, vgap=1, maxiter=100)
	#plot(grafo, layout = layout) 
	
	return grafo