''' Funcao que retorna o numero de pacientes 
    
    Variaveis de entrada:	-- 
	Variaveis de saida:		uma variavel que contem o numero de pacientes	'''
    
def numero_pacientes():
    with open('matriz_eventos.txt','r') as arquivo:
        numero_pacientes = arquivo.readline().split()
        arquivo.close()
    return ( len(numero_pacientes) - 1 )