import pytest
import pandas as pd
import mlflow
import requests



@pytest.fixture(scope="module")
def model() -> mlflow.pyfunc.PyFuncModel:
    # Definindo o caminho do MLflow
    mlflow.set_tracking_uri("http://localhost:5000")  
    model_name = "random_forest"  # Nome do modelo
    model_version = 1  # Versão do modelo
    # Carregar o modelo do MLflow
    return mlflow.pyfunc.load_model(
        model_uri=f"models:/{model_name}/{model_version}"
    )


def test_model_out(model: mlflow.pyfunc.PyFuncModel):
    # Exemplo de input para o modelo (um cliente sem calote)
    input_data = pd.DataFrame.from_records([{
        "ID": 1,
        'LIMIT_BAL': 50000,  # Quantidade de crédito
        'SEX': 1,  # Gênero (1 = masculino, 2 = feminino)
        'EDUCATION': 2,  # Grau de educação (1 = pós-graduação, 2 = universitário, ...)
        'MARRIAGE': 1,  # Estado civil (1 = casado, 2 = solteiro, ...)
        'AGE': 30,  # Idade
        'PAY_0': 0,  # Status de pagamento (0 = pagamento em dia)
        'PAY_2': 0,  # Status de pagamento mês anterior
        'PAY_3': 0,  # Status de pagamento 2 meses atrás
        'PAY_4': 0,  # Status de pagamento 3 meses atrás
        'PAY_5': 0,  # Status de pagamento 4 meses atrás
        'PAY_6': 0,  # Status de pagamento 5 meses atrás
        'BILL_AMT1': 1000,  # Fatura do mês atual
        'BILL_AMT2': 900,  # Fatura do mês anterior
        'BILL_AMT3': 950,  # Fatura 2 meses atrás
        'BILL_AMT4': 980,  # Fatura 3 meses atrás
        'BILL_AMT5': 1000,  # Fatura 4 meses atrás
        'BILL_AMT6': 1100,  # Fatura 5 meses atrás
        'PAY_AMT1': 200,  # Pagamento feito no mês atual
        'PAY_AMT2': 200,  # Pagamento feito no mês anterior
        'PAY_AMT3': 150,  # Pagamento 2 meses atrás
        'PAY_AMT4': 180,  # Pagamento 3 meses atrás
        'PAY_AMT5': 200,  # Pagamento 4 meses atrás
        'PAY_AMT6': 190   # Pagamento 5 meses atrás
    }])

    # Prever o valor de "default.payment.next.month"
    prediction = model.predict(data=input_data)

    # Verificar se a previsão foi 0 (sem calote) ou 1 (com calote)
    assert prediction[0] in [0, 1]


def test_model_inv(model: mlflow.pyfunc.PyFuncModel):
    # Exemplo de input para o modelo (um cliente com pagamento atrasado)
    input_data = pd.DataFrame.from_records([{
        "ID": 1,
        'LIMIT_BAL': 50000,  # Quantidade de crédito
        'SEX': 1,  # Gênero (1 = masculino, 2 = feminino)
        'EDUCATION': 2,  # Grau de educação
        'MARRIAGE': 1,  # Estado civil
        'AGE': 30,  # Idade
        'PAY_0': 2,  # Status de pagamento (2 = pagamento com atraso de 2 meses)
        'PAY_2': 2,  # Status de pagamento mês anterior (2 meses de atraso)
        'PAY_3': 1,  # Status de pagamento 2 meses atrás (1 mês de atraso)
        'PAY_4': 0,  # Status de pagamento 3 meses atrás (pagamento em dia)
        'PAY_5': 0,  # Status de pagamento 4 meses atrás (pagamento em dia)
        'PAY_6': 0,  # Status de pagamento 5 meses atrás (pagamento em dia)
        'BILL_AMT1': 1000,  # Fatura do mês atual
        'BILL_AMT2': 900,  # Fatura do mês anterior
        'BILL_AMT3': 950,  # Fatura 2 meses atrás
        'BILL_AMT4': 980,  # Fatura 3 meses atrás
        'BILL_AMT5': 1000,  # Fatura 4 meses atrás
        'BILL_AMT6': 1100,  # Fatura 5 meses atrás
        'PAY_AMT1': 200,  # Pagamento feito no mês atual
        'PAY_AMT2': 200,  # Pagamento feito no mês anterior
        'PAY_AMT3': 150,  # Pagamento 2 meses atrás
        'PAY_AMT4': 180,  # Pagamento 3 meses atrás
        'PAY_AMT5': 200,  # Pagamento 4 meses atrás
        'PAY_AMT6': 190   # Pagamento 5 meses atrás
    }])

    # Prever o valor de "default.payment.next.month"
    prediction = model.predict(data=input_data)

    # Verificar se a previsão foi 0 (sem calote) ou 1 (com calote)
    assert prediction[0] in [0, 1]


def test_model_out_shape(model: mlflow.pyfunc.PyFuncModel):
    # Exemplo de input para o modelo
    input_data = pd.DataFrame.from_records([{
        "ID": 1,
        'LIMIT_BAL': 50000,  # Quantidade de crédito
        'SEX': 1,  # Gênero
        'EDUCATION': 2,  # Grau de educação
        'MARRIAGE': 1,  # Estado civil
        'AGE': 30,  # Idade
        'PAY_0': 0,  # Status de pagamento
        'PAY_2': 0,  # Status de pagamento mês anterior
        'PAY_3': 0,  # Status de pagamento 2 meses atrás
        'PAY_4': 0,  # Status de pagamento 3 meses atrás
        'PAY_5': 0,  # Status de pagamento 4 meses atrás
        'PAY_6': 0,  # Status de pagamento 5 meses atrás
        'BILL_AMT1': 1000,  # Fatura do mês atual
        'BILL_AMT2': 900,  # Fatura do mês anterior
        'BILL_AMT3': 950,  # Fatura 2 meses atrás
        'BILL_AMT4': 980,  # Fatura 3 meses atrás
        'BILL_AMT5': 1000,  # Fatura 4 meses atrás
        'BILL_AMT6': 1100,  # Fatura 5 meses atrás
        'PAY_AMT1': 200,  # Pagamento feito no mês atual
        'PAY_AMT2': 200,  # Pagamento feito no mês anterior
        'PAY_AMT3': 150,  # Pagamento 2 meses atrás
        'PAY_AMT4': 180,  # Pagamento 3 meses atrás
        'PAY_AMT5': 200,  # Pagamento 4 meses atrás
        'PAY_AMT6': 190   # Pagamento 5 meses atrás
    }])

    # Prever o valor de "default.payment.next.month"
    prediction = model.predict(data=input_data)

    # Verificar a forma da previsão (se deve ser um vetor de uma única previsão)
    assert prediction.shape == (1, )

# Testar a API
def test_api_prediction():
    response = requests.post("http://localhost:5003/predict_default", json={
        "ID": 1,
        "LIMIT_BAL": 50000,
        "SEX": 1,
        "EDUCATION": 2,
        "MARRIAGE": 1,
        "AGE": 30,
        "PAY_0": 0,
        "PAY_2": 0,
        "PAY_3": 0,
        "PAY_4": 0,
        "PAY_5": 0,
        "PAY_6": 0,
        "BILL_AMT1": 1000,
        "BILL_AMT2": 900,
        "BILL_AMT3": 950,
        "BILL_AMT4": 980,
        "BILL_AMT5": 1000,
        "BILL_AMT6": 1100,
        "PAY_AMT1": 200,
        "PAY_AMT2": 200,
        "PAY_AMT3": 150,
        "PAY_AMT4": 180,
        "PAY_AMT5": 200,
        "PAY_AMT6": 190
    })

    assert response.status_code == 200
    assert "default_prediction" in response.json()
    assert response.json()["default_prediction"] in [0, 1]



def test_always_passes():
    assert True

def test_always_fails():
    assert False