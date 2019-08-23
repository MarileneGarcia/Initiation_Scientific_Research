''' Funcao que faz a filtragem de dados, criando uma matriz de eventos (genes mutados em cada paciente) e 
      um arquivo da rede usando o coeficiente de Jaccard
	 
    Variaveis de entrada:	tres arquivos, um com o genes mutados nos pacientes (maf), um com a relacao entre os genes (HRN)
                           e um com os genes filtrados
	 Variaveis de saida:	   uma lista com o nome de todos os genes que serao analisados e um dicionario associando
                           o numero dos genes ao nome deles '''
import pandas as pd
import numpy as np
from collections import defaultdict

# Definindo o limite inferior do coeficiente de Jaccard
jaccard_threshold = 0.025

def filtragem_dados(nome_arquivo_maf, nome_arquivo_redes, nome_arquivo_genes_filtados):
   # Criando os dataFrames da rede inicial e do arquivo maf
   maf = pd.read_table(nome_arquivo_maf, usecols=["Hugo_Symbol", "Entrez_Gene_Id", "Tumor_Sample_Barcode"])
   maf["Hugo_Symbol"] = maf["Hugo_Symbol"].str.strip()
   maf["Tumor_Sample_Barcode"] = maf["Tumor_Sample_Barcode"].str.strip()
   
   rede = pd.read_table(nome_arquivo_redes, sep=" ", header=None, usecols=[0,2])
   #rede[0] = rede[0].astype(str).str.strip()
   #rede[2] = rede[2].astype(str).str.strip()

   mutSig = pd.read_table(nome_arquivo_genes_filtados, usecols=["gene"])
   mutSig["gene"] = mutSig["gene"].str.strip()

   # Salvando os genes listados pelo mutSig em uma lista
   lista_mutSig = []
   for index, row in mutSig.iterrows():
      lista_mutSig.append(row["gene"])
      
   # Excluindo do dataFrame maf os genes que não foram filtrados pelo algoritmo MutSig
   for index,row in maf.iterrows():
      if(row["Hugo_Symbol"] in lista_mutSig):
         pass
      else:
         maf.drop(index, inplace=True)

   # Criando uma lista dos genes presentes no dataFrame maf 
   lista_genes_maf = []
   for index,row in maf.iterrows():
      try:
         lista_genes_maf.append(row["Entrez_Gene_Id"])
      except KeyError:
         pass
   lista_genes_maf = list(set(lista_genes_maf))
   
   #Etapa 2 
   # Criando uma lista dos genes presentes no dataFrame da rede inicial e um dicionario asociando aos genes que eles se relacionam 
   lista_genes_rede = []
   for index,row in rede.iterrows():  
      try:
         tupla_aux = (row[0], row[2])
         lista_genes_rede.append(tupla_aux) 
      except KeyError:
         pass
   dicionario_relacao_genes = defaultdict(list)  
   for chave, valor in lista_genes_rede:
	   dicionario_relacao_genes[chave].append(valor)

   # Criando o arquivo com a rede dos genes prensentes no maf que sao funcionalmente conectados de acordo com o coeficiente de Jaccard
   lista_genes_rede = []
   arquivo_rede = open('rede_filtrada.txt', 'w')
   for chave, valor in dicionario_relacao_genes.items():
      for chave_aux, valor_aux in dicionario_relacao_genes.items():
         if( ( (len(set(valor).intersection(valor_aux)) / len(set(valor).union(valor_aux))) >= jaccard_threshold) and (chave in lista_genes_maf) and (chave_aux in lista_genes_maf) ):
            arquivo_rede.write('%s %s \n' % (chave,chave_aux))
            lista_genes_rede.append(chave)
            lista_genes_rede.append(chave_aux)   
         else:
            pass
   arquivo_rede.close()
   lista_genes_rede = list(set(lista_genes_rede))
   
   lista_nome_genes = []
   # Excluindo do dataFrame maf os genes que não estao na rede criada e e um criando dicionario associando o Id dos genes ao nome deles
   for index,row in maf.iterrows():
      if( (row["Entrez_Gene_Id"] in lista_genes_rede) ):
         tupla_nome_genes = (row["Entrez_Gene_Id"], row["Hugo_Symbol"])
         lista_nome_genes.append(tupla_nome_genes)
      else:
         maf.drop(index, inplace=True)
      
   dicionario_nome_genes = defaultdict(list)  
   for chave, valor in lista_nome_genes:
	   dicionario_nome_genes[chave].append(valor)
   
   # Salvando a matriz binaria que originara o grafo de eventos em um arquivo
   mut = pd.crosstab(maf.Entrez_Gene_Id, maf.Tumor_Sample_Barcode).clip_upper(1)
   arquivo_aux3 = open('matriz_eventos.txt', 'w')
   arquivo_aux3.write(mut.to_string())
   arquivo_aux3.close()
   
   # Retornando a lista com o nome dos genes e o dicionario que associa o nome deles e o numero
   lista_retorno = []
   lista_retorno.append(lista_genes_rede)
   lista_retorno.append(dicionario_nome_genes)
   return lista_retorno