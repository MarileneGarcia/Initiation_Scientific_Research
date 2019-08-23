# Projeto de Iniciacao cientifica 
# Metodo MEMo (Mutual Exclusivity Modules in cancer) 

O projeto foi baseado em um artigo academico, ha um relatorio associado a ele e esta e a primeira versao do software desenvolvido.

##  Pre requisitos 
O software foi implementado utilizando a linguagem de programacao Python (versão 3.6.7), logo devera ser executado em maquinas com interpretadores adequados.

E necessario instalar a biblioteca igraph(versão 0.7.1), disponivel em https://igraph.org/

E necessario instalar a biblioteca Pandas(versão 0.24.2), disponivel em https://pandas.pydata.org/

Quando executado, o algoritmo necessitara do fornecimento do nome dos arquivos do genes mutados em determinados pacientes (geralmente um arquivo maf), da rede de associacao de pares de genes (HRN) e tambem do que contem os genes que serao analisados (genes que passaram nos filtros). E necessario ler o relatorio do projeto para saber como devem ser os modelos desses arquivos descritos na secao de desenvolvimento (terceira secao). **Esses arquivos devem estar na mesma pasta na qual estao todos os codigos e o nome deles deve ser preenchido no script**

** Vale ressaltar que o codigo foram executados em dois computadores, com as seguintes especificacoes: **
1. Intel Core i5-7300HQ @ 3.50GHz, quad-core, 8192MB RAM, LinuxMint 18.3 operating system
2. Intel Core i7-5500U @ 2.30GHz, quad-core, 8192MB RAM, Ubuntu 18.04 operating system

## Guia de execucao
Considerando que o usuario esteja utilizando a versao correta do Python, e que o interpretador seja o python3, deve-se digitar o seguinte comando no terminal do Linux:
**python3 script_MEMo.py**

## Resultados
Os resultados estaram disponiveis no arquivo texto *Resultados do metodo.txt*

