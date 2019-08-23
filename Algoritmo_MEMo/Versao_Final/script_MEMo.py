# Metodo MEMo #

# Forneca o nome dos arquivos:

# Arquivo maf
nome_arquivo_maf = "data_mutations_MAF.txt"

# Arquivo da rede 
nome_arquivo_rede = "HUMAN_REFERENCE_NETWORK.sif"

# Arquivo dos genes filtrados
nome_arquivo_filtro ="filtro20.txt"

import time
import MEMo

tempo_inicio = time.time()
MEMo.MEMo(nome_arquivo_maf,nome_arquivo_rede, nome_arquivo_filtro)
with open('Resultados do metodo.txt', 'a+') as arquivo:
    arquivo.write("\nO tempo de execução do código foi de: " + str(time.time() - tempo_inicio) + " segundos")
arquivo.close()
