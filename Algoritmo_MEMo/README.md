# Projeto de Iniciação científica 
# Método MEMo (Mutual Exclusivity Modules in cancer) 

O projeto foi baseado em um artigo acadêmico, há um relatório associado a ele e esta é a primeira versão do software desenvolvido.

##  Pré requisitos 
O software foi implementado utilizando a linguagem de programação Python (versão 3.6.7), logo deverá ser executado em máquinas com interpretadores adequados.

E necessário instalar a biblioteca igraph(versão 0.7.1), disponível em https://igraph.org/

E necessário instalar a biblioteca Pandas(versão 0.24.2), disponível em https://pandas.pydata.org/

Quando executado, o algoritmo necessitará do fornecimento do nome dos arquivos do genes mutados em determinados pacientes (geralmente um arquivo maf), da rede de associação de pares de genes (HRN) e também do que contém os genes que serão analisados (genes que passaram nos filtros). É necessário ler o relatório do projeto para saber como devem ser os modelos desses arquivos descritos na seção de desenvolvimento (terceira seção). **Esses arquivos devem estar na mesma pasta na qual estão todos os códigos e o nome deles deve ser preenchido no script (script_MEMo.py).**

**Vale ressaltar que os códigos foram executados em dois computadores, com as seguintes especificações:**
1. Intel Core i5-7300HQ @ 3.50GHz, quad-core, 8192MB RAM, LinuxMint 18.3 operating system
2. Intel Core i7-5500U @ 2.30GHz, quad-core, 8192MB RAM, Ubuntu 18.04 operating system

## Guia de execução
Considerando que o usuário esteja utilizando a versão correta do Python, e que o interpretador seja o python3, deve-se estar no diretório *Iniciacao_Cientifica/Algoritmo_MEMo/Versao_Final/* e digitar o seguinte comando no terminal do Linux:
**python3 script_MEMo.py**

## Resultados
Os resultados estarão disponíveis no arquivo texto *Resultados do metodo.txt*

