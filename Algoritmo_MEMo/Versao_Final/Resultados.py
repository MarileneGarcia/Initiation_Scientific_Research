''' Funcao que salva os resultados do metodo em um arquivo texto
	
    Variaveis de entrada:	 dicionario que associa o nome do gene ao numero dele, os pathways e os p valores respectivos
	  Variaveis de saida:		--- 	'''
import pandas as pd
import numpy as np

def resultados(dicionario_nomes, pathways, P_valor):
  with open('Resultados do metodo.txt', 'w') as arquivoUm:
    for aux1 in range (len(pathways)) :
      arquivoUm.write("O P valor do pathway que contem os genes : ")
      for aux2 in pathways[aux1] :
        if(aux2 in dicionario_nomes):
          if(len(list(set(dicionario_nomes[aux2]))) > 1):
            raise NameError('Há mais de um Hugo_Symbol associado ao mesmo Entrez_Gene_Id ' + str(aux2) + ' no arquivo maf')
          else:
            arquivoUm.write(str(dicionario_nomes[aux2][0]) + " ") 
      arquivoUm.write("é equivalente a : " + str(P_valor[aux1]) + "\n")
  arquivoUm.close()