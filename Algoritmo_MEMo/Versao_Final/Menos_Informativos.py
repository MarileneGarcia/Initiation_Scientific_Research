''' Funcao que retorna o pathway apos ter excluido o no menos significativo (sub-clique X)

		Variaveis de entrada:	 uma lista com o pathway, o dicionario de mutacoes e a lista com o nome dos genes
		Variaveis de saida:		uma lista com pathway sem o no menos significativo 	'''

def menos_informativos(sub_clique_X, dicionario_mutacoes):
	# Encontrar o no menos informativos
	menos_informativo = []
	for aux1 in sub_clique_X :
		aux5 = 0
		for aux2 in dicionario_mutacoes [ str(aux1) ]:
			aux6 = 0
			for aux3 in sub_clique_X:
				if(aux3 != aux1):
					if aux2 in dicionario_mutacoes [ str(aux3) ] :
						aux5 += 1
						aux6 += 1
			if (aux6 > 1):
				aux5 = aux5 - aux6 + 1
		menos_informativo.append( len(dicionario_mutacoes[ str(aux1)]) - aux5)
	
	del sub_clique_X[menos_informativo.index(min(menos_informativo))]
	del menos_informativo[menos_informativo.index(min(menos_informativo))]
	return sub_clique_X
	
