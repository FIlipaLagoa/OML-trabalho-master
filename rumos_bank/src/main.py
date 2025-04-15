import fastapi
from fastapi.middleware.cors import CORSMiddleware
import mlflow
from pydantic import BaseModel, conint
import pandas as pd
import json
import uvicorn

# Define the inputs expected in the request body as JSON

"""
Atributos do modelo:
    LIMIT_BAL: float Amount of given credit in NT dollars (includes individual and family/supplementary credit
    SEX: int Gender (1=male, 2=female)
    EDUCATION: int (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)
    MARRIAGE: int Marital status (1=married, 2=single, 3=others)
    AGE: int Age in years
    PAY_0: int Repayment status in September, 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, ... 8=payment delay for eight months, 9=payment delay for nine months and above)
    PAY_2: int Repayment status in August, 2005 (scale same as above)
    PAY_3: int Repayment status in July, 2005 (scale same as above)
    PAY_4: int Repayment status in June, 2005 (scale same as above)
    PAY_5: int Repayment status in May, 2005 (scale same as above)
    PAY_6: int Repayment status in April, 2005 (scale same as above)
    BILL_AMT1: float Amount of bill statement in September, 2005 (NT dollar)
    BILL_AMT2: float Amount of bill statement in August, 2005 (NT dollar)
    BILL_AMT3: float Amount of bill statement in July, 2005 (NT dollar)
    BILL_AMT4: float Amount of bill statement in June, 2005 (NT dollar)
    BILL_AMT5: float Amount of bill statement in May, 2005 (NT dollar)
    BILL_AMT6: float Amount of bill statement in April, 2005 (NT dollar)
    PAY_AMT1: float Amount of previous payment in September, 2005 (NT dollar)
    PAY_AMT2: float Amount of previous payment in August, 2005 (NT dollar)
    PAY_AMT3: float Amount of previous payment in July, 2005 (NT dollar)
    PAY_AMT4: float Amount of previous payment in June, 2005 (NT dollar)
    PAY_AMT5: float Amount of previous payment in May, 2005 (NT dollar)
    PAY_AMT6: float Amount of previous payment in April, 2005 (NT dollar)

"""
class LendingRequest(BaseModel):
    LIMIT_BAL: float = 20000.0 
    SEX: conint(ge=1, le=2) = 2  
    EDUCATION: conint(ge=1, le=6) = 2  
    MARRIAGE: conint(ge=1, le=3) = 1  
    AGE: conint(ge=18) = 30  

    PAY_0: int = 0
    PAY_2: int = 0
    PAY_3: int = 0
    PAY_4: int = 0
    PAY_5: int = 0
    PAY_6: int = 0

    BILL_AMT1: float = 5000.0
    BILL_AMT2: float = 5000.0
    BILL_AMT3: float = 5000.0
    BILL_AMT4: float = 5000.0
    BILL_AMT5: float = 5000.0
    BILL_AMT6: float = 5000.0

    PAY_AMT1: float = 1000.0
    PAY_AMT2: float = 1000.0
    PAY_AMT3: float = 1000.0
    PAY_AMT4: float = 1000.0
    PAY_AMT5: float = 1000.0
    PAY_AMT6: float = 1000.0


# Create a FastAPI application
app = fastapi.FastAPI()

# Add CORS middleware to allow all origins, methods, and headers for local testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():

    """
    Set up actions to perform when the app starts.

    Configures the tracking URI for MLflow to locate the model metadata
    in the local mlruns directory.
    """

    mlflow.set_tracking_uri("./mlruns")
    
    with open('./config/app.json') as f:
        config = json.load(f)

    app.model = mlflow.pyfunc.load_model(
        model_uri=f"models:/{config['model_name']}/{config['model_version']}"
    )

    print(f"Modelo carregado: {config['model_name']}/{config['model_version']}")


@app.post("/predict_default")
async def predict(input: LendingRequest):
    # Build a DataFrame from the request data
    input_df = pd.DataFrame.from_dict({k: [v] for k, v in input.dict().items()})
    
    # Predict using the model and retrieve the first item in the prediction list
    prediction = app.model.predict(input_df)

    # Return the prediction result as a JSON response
    return {"default_prediction": prediction.tolist()[0]}

# Run the app on port 5003
if __name__ == "__main__":
    uvicorn.run(app=app, port=5003)
