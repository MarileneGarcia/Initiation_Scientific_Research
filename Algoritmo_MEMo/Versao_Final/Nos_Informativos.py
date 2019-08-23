''' Funcao que exclui os nos nao informativos dos cliques maximais 

		Variaveis de entrada: uma lista com os cliques maximais e uma lista com os nomes dos genes
		Variaveis de saida:		uma lista com os cliques maximais sem os nos nao informativos,
													um dicionario com os genes mutados de cada paciente e uma matriz
													gerada a partir do arquivo da matriz de eventos	'''

import Numero_Genes
from collections import defaultdict

def nos_informativos(cliques_maximais, nome_genes):

# Salvar os dados do arquivo dos eventos em uma matriz
	with open('matriz_eventos.txt', 'r') as arquivoUm:       
		matriz = []
		for index in range(Numero_Genes.numero_genes(nome_genes) + 2):
			linha = []
			coluna = arquivoUm.readline().split()
			aux = 0
			for paciente in coluna:
				aux = aux + 1
				try:
					linha.append(paciente)
				except ValueError:
					pass 
			matriz.append(linha)

	# Associar os genes alterados aos pacientes em que foram observadas as alteracoes
	lista_tupla = []
	for i in range (len(matriz) - 1):
		for j in range (len(matriz[i+1]) - 1):
			if(matriz[i+1][j+1] == '1'):
				chave = matriz[i+1][0]
				j = matriz[0][j+1]
				tupla = (chave,j)
				lista_tupla.append(tupla)

	# Criar um dicionario contendo como chave os genes alterados, e os pacientes em que foram 
	# observadas essas alteracoes como valores associados as chaves 
	dicionario_mutacoes = defaultdict(list)  
	for chave, valor in lista_tupla:
		dicionario_mutacoes[chave].append(valor)
	
	# Converter a tuples dos pathways em uma lista, para poder excluir os nos não informativos
	for aux8 in range (len(cliques_maximais)):
		cliques_maximais[aux8] = list(cliques_maximais[aux8])
	
	# Encontrar os nos não informativos 
	for aux1 in range (len(cliques_maximais) - 1, -1, -1):
		informativos = []
		nao_informativos = []
		for aux2 in range (len(cliques_maximais[aux1])):
			aux5 = 0
			for aux3 in dicionario_mutacoes[str(cliques_maximais[aux1][aux2])]:
				aux6 = 0
				for aux4 in range (len(cliques_maximais[aux1])):
					if(aux4 != aux2):
						if aux3 in dicionario_mutacoes[str(cliques_maximais[aux1][aux4])]:
							aux5 += 1
							aux6 += 1
				if (aux6 > 1):
					aux5 = aux5 - aux6 + 1
			informativos.append(len(dicionario_mutacoes[str(cliques_maximais[aux1][aux2])]) - aux5)
			nao_informativos.append(aux5)

		# Excluir os nos não informativos
		for aux7 in range(len(cliques_maximais[aux1]) - 1,-1,-1):
			if(informativos[aux7] < nao_informativos[aux7] or (informativos[aux7] == 0)):
				del cliques_maximais[aux1][aux7]

		# Se os genes de um pathway inteiro foram excluidos, então excluir o pathway
		if(cliques_maximais[aux1] == [] or len(cliques_maximais[aux1]) < 2):
			del cliques_maximais[aux1]
			
	# Retornar os cliques maximos com apenas os nos informativos, e o dicionario de mutacoes	
	lista_retorno = []
	lista_retorno.append(cliques_maximais)
	lista_retorno.append(dicionario_mutacoes)
	lista_retorno.append(matriz)
	
	return lista_retorno
