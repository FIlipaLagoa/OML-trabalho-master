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

# 1. Criar uma cópia local do repositório que está no github:

   ```
   git clone https://github.com/FIlipaLagoa/RumosBank-FinalProject.git
   cd OML-trabalho-master
   ```
# 2. Criar e ativa um ambiente virtual:

```
conda create -n OML python=3.12
```
# 2.1. Ativar o ambiente acabado de criar
```
conda activate OML
```
# 2.2. Instalar as dependências necessárias:

```
conda install -c conda-forge uvicorn
conda install -c conda-forge fastapi
conda install -c conda-forge pandas
conda install -c conda-forge numpy
conda install -c conda-forge scikit-learn
conda install -c conda-forge mlflow
conda install -c conda-forge mlflow-ui
```
# 2.3. De forma a tornar a minha experiência reproduzível, exportar o meu ambiende para um ficheiro conda.yaml:
```
conda env export --file conda.yaml
```

# 2.4. Agora que temos o ficheiro conda.yml, conseguimos facilmente recriar o nosso ambiente em qualquer altura. Por isso vamos desativar e eliminar o ambiente que acabamos de criar:
```
conda deactivate
conda env remove --name OML
```

# 2.5. Podemos verificar que foi mesmo eliminado com
```
conda env list
```

# 2.6.E agora vamos criar um novo ambiente a partir do conda.yaml, e ativa-lo:
```
conda env create -f conda.yaml
conda activate OML



