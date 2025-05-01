# Rumos Bank going live
## DL: 1 Maio de 2025

### Contexto do Problema

The Rumos Bank é um banco que tem perdido bastante dinheiro devido à quantidade de créditos que fornece e que não são pagos dentro do prazo devido. 

Depois do banco te contratar, como data scientist de topo, para ajudares a prever os clientes que não irão cumprir os prazos, os resultados exploratórios iniciais são bastante promissores!

Mas o banco está algo receoso, já que teve uma má experiência anterior com uma equipa de data scientists, em que a transição dos resultados iniciais exploratórios até de facto conseguirem ter algo em produção durou cerca de 6 meses, bem acima da estimativa inicial.

Por causa desta prévia má experiência, o banco desta vez quer ter garantias que a passagem dos resultados iniciais para produção é feita de forma mais eficiente. O objetivo é que a equipa de engenharia consegue colocar o vosso modelo em produção em dias em vez de meses!

## Nota
NOTA
Esta secção contém observações relevantes para garantir a correta execução do projeto. A imagem Docker do serviço não se conseguiu publicar no token do GitHub Container Registry devido ao facto de não ter sido possível migrar todos os ficheiros do projeto para o Git. Ocorreram erros sucessivos como:
```

remote: error: Trace: 453c1ed95e8e2ab304d5c97c2c861da9a7c340413220328565b3261073b664c3
remote: error: See https://gh.io/lfs for more information.
remote: error: File mlruns/840766384340770077/307ba259c68349e98a1b10753f4a15e7/artifacts/rf_pipeline/model.pkl is 155.18 MB; this exceeds GitHub's file size limit of 100.00 MB
remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.

```

Ainda se tentou instalar o Git LFS seguindo as sugestões do Visual Studio Code, e foram criados os respetivos ficheiros .gitattributes, que se podem encontrar neste projeto, mas mesmo assim não foi possível resolver o problema.

De qualquer forma, foi feito um model registry para o modelo escolhido com melhor performance no notebook1, o Random Forest. Este modelo revelou-se mais económico para o banco Rumos e, no notebook2, utilizou-se uma pipeline para não só normalizar o modelo, mas também para criar um modelo registado. A versão utilizada foi determinada como champion do modelo Random Forest.

Serviços concluídos:
Uma instância do MLflow que pode ser acedida localmente em http://localhost:5000.

Docker Compose, também acessível localmente em http://localhost:5003.

O ficheiro conda.yaml define todas as dependências necessárias para reproduzir o ambiente localmente.

Contudo, o ambiente conda-mini.yaml foi necessário adicionar ao projeto para que o Docker conseguisse correr sem problemas, visto que é dependente de Linux.

### O que consegui fazer:
- MLflow com model registry e pipeline
- Champion definido: random_forest
- Docker Compose
- conda-minimal.yaml (dependências Linux)
- conda.yaml para os notebooks
- Proposta de ficheiro para a pipeline cicd

### O que não consegui fazer:
Não consegui correr a pipeline porque só fica disponível quando se transita tudo com sucesso para o GitHub — e tal não foi possível.

Apesar de ter contactado o professor, o mesmo não me respondeu e, por isso, não consegui avançar mais com o projeto.

## Estrutura do Projeto

OML-trabalho-master/
├──.gits
├── mlruns
├── OML-trabalho.master.git
├── .gitattributes
├── README.md (estrutura do projeto)
├── rumos_bank
│   └── .github/
│       └── workflows/
│           ├── .github/
│                └── workflows/
│                    └── simpleci.yaml
│   ├── config/
│       └── app.json
│   │── data/
│       └── lending_data.csv
│   │── mlruns/
│   ├── notebooks/
│       └── lending_data.csv
│   └── mlflow/
│       ├── notebook1_mlflow.ipynby
│       ├── notebook2_pipeline.ipynby
│       ├── readme.md
│   ├── src/
│       └── main.py
│   ├── tests/
│       ├── test_model.py
│       └── test_service.py
│   ├── conda.yaml
│   ├── conda-minimal.yaml
│   ├── docker-compose.yml
│   ├── Dockerfile.Service
│   └── README_OML.md


## Requisitos

- [ ] Python 3.9+
- [ ] Conda ou Miniconda
- [ ] Docker 

## Instalação do ambiente de trabalho e a sua configuração

# 1. Criar uma cópia local do repositório que está no github:

   ```
   git clone https://github.com/FIlipaLagoa/OML-trabalho-master
   
   ```
# 2. Criar e ativar um ambiente virtual:

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

```



### Próximos Passos
Apesar dos objetivos principais terem sido atingidos, existem ainda algumas tarefas por concluir, que poderão ser desenvolvidas como próximos passos:

### Publicação completa do projeto no GitHub
A publicação do projeto não foi concluída devido ao erro com ficheiros de grande dimensão (ex. model.pkl com mais de 100MB). Apesar de se ter tentado usar o Git LFS, não foi possível resolver o problema. Como tal, a imagem Docker não pôde ser publicada no GitHub Container Registry.

### Execução completa da pipeline CI/CD com GitHub Actions
Estava prevista uma pipeline de CI/CD que incluía testes com pytest, construção da imagem com docker-compose, e publicação automática no GHCR. No entanto, essa automação não foi concluída por depender da publicação do repositório e da imagem.

### Execução da pipeline ML em ambiente remoto
A pipeline de ML com o modelo registado não pôde ser totalmente testada, pois depende de todos os artefactos estarem versionados e disponíveis remotamente, o que não foi possível garantir devido às limitações já mencionadas.

