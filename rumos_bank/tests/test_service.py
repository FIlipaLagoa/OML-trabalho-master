import pytest
import requests

BASE_URL = "http://localhost:5003"  # URL do servidor FastAPI

def test_predict_default_prediction():
    """
    Test for the /predict_default endpoint with valid input data.
    It should return a prediction in the response.
    """
    response = requests.post(f"{BASE_URL}/predict_default", json={
        'LIMIT_BAL': 200000,              # Limite de crédito em NT dólares
        'SEX': 1,                         # Sexo (1=masculino, 2=feminino)
        'EDUCATION': 2,                   # Educação (2=universitário)
        'MARRIAGE': 1,                    # Estado civil (1=casado)
        'AGE': 30,                        # Idade do cliente
        'PAY_0': 1,                       # Status de pagamento (1=atraso de 1 mês)
        'PAY_2': 1,                       # Status de pagamento (1=atraso de 1 mês)
        'PAY_3': 0,                       # Status de pagamento (0=sem atraso)
        'PAY_4': 0,                       # Status de pagamento (0=sem atraso)
        'PAY_5': 0,                       # Status de pagamento (0=sem atraso)
        'PAY_6': 0,                       # Status de pagamento (0=sem atraso)
        'BILL_AMT1': 1000,                # Valor da fatura em setembro de 2005
        'BILL_AMT2': 1000,                # Valor da fatura em agosto de 2005
        'BILL_AMT3': 1000,                # Valor da fatura em julho de 2005
        'BILL_AMT4': 1000,                # Valor da fatura em junho de 2005
        'BILL_AMT5': 1000,                # Valor da fatura em maio de 2005
        'BILL_AMT6': 1000,                # Valor da fatura em abril de 2005
        'PAY_AMT1': 500,                  # Pagamento anterior em setembro de 2005
        'PAY_AMT2': 500,                  # Pagamento anterior em agosto de 2005
        'PAY_AMT3': 500,                  # Pagamento anterior em julho de 2005
        'PAY_AMT4': 500,                  # Pagamento anterior em junho de 2005
        'PAY_AMT5': 500,                  # Pagamento anterior em maio de 2005
        'PAY_AMT6': 500                   # Pagamento anterior em abril de 2005
    })
    assert response.status_code == 200
    assert "default_prediction" in response.json()
    assert isinstance(response.json()["prediction"], (int, float))
    assert response.json()["prediction"] == 0
