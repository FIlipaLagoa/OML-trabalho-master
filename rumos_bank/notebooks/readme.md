# Notebooks folder

# 1. Correr os notebooks do número 1 ao 5

# 2. Para o mlflow no final de cada notebook correr o seguinte código para visualizar as runs dentro da experiência: Rumos Bank Experiment

A UI do mlflow permite ver de forma visual todas as experiências criadas e permite por exemplo, comparar, filtar e ordenar, as runs dentro de uma experiência de forma visual.

Para correr a UI do mflow é necessário executar, na raiz deste projeto (pasta rumos) e tendo activo o ambiente utilizado neste projeto, o comando:

`mlflow ui --backend-store-uri ./mlruns`

**Nota:** O comando em cima irá iniciar a UI de mlflow na porta 5000. Caso queiram mudar esta porta devem acrescentar `--port <PORT>` ao comando (em que <PORT> deve ser substituido pela porta desejada). 

O comando acima não irá funcionar caso tenham tido alguns problemas no Windows com a instalação do mlflow. Caso tenham problemas, considerem instalar o `mlflow-ui`, ao invés do mlflow.

Após executarem este comando, vão poder ver a UI do mlflow no vosso browser acedendo a 

`http://127.0.0.1:5000`

(se tiverem alterado a porta em que o mlflow UI é iniciado então devem de alterar também aqui o 5000 por essa porta)
