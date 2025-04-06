# Rumos Bank going live
## DL: 1 Maio de 2025

### Contexto do Problema

The Rumos Bank é um banco que tem perdido bastante dinheiro devido à quantidade de créditos que fornece e que não são pagos dentro do prazo devido. 

Depois do banco te contratar, como data scientist de topo, para ajudares a prever os clientes que não irão cumprir os prazos, os resultados exploratórios iniciais são bastante promissores!

Mas o banco está algo receoso, já que teve uma má experiência anterior com uma equipa de data scientists, em que a transição dos resultados iniciais exploratórios até de facto conseguirem ter algo em produção durou cerca de 6 meses, bem acima da estimativa inicial.

Por causa desta prévia má experiência, o banco desta vez quer ter garantias que a passagem dos resultados iniciais para produção é feita de forma mais eficiente. O objetivo é que a equipa de engenharia consegue colocar o vosso modelo em produção em dias em vez de meses!


## Requisitos

- [ ] Python 3.9+
- [ ] Conda ou Miniconda
- [ ] Docker 

## Instalação do ambiente de trabalho e a sua configuração

1. Criar uma cópia local do repositório que está no github:

   ```
   git clone https://github.com/FIlipaLagoa/RumosBank-FinalProject.git
   cd OML-trabalho-master
   ```
2. Cria e ativa um ambiente virtual:

   ```
   conda env create -f conda.yaml
   conda activate OML01
   
   ```
3. Dependências:
## O ficheiro conda.yaml já tem as dependencias necessárias entre as quais:
# -c conda-forge uvicorn fastapi pandas numpy scikit-learn mlflow mlflow-ui

