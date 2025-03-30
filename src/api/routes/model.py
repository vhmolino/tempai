from fastapi import APIRouter, HTTPException
from models.model_fit_response import ModelFitResponse
from models.model_fit_request import ModelFitRequest
from models.model_predict_response import ModelPredictResponse

from ai.tempai import model_fit, model_predict

router = APIRouter(prefix="/model", tags=["model"])

@router.post("/fit", response_model=ModelFitResponse)
async def fit(
    payload: ModelFitRequest
) -> ModelFitResponse:
    model_fit(train_data=payload.data)
    
    response = ModelFitResponse(result=True)
    return response

@router.get("/predict", response_model=ModelPredictResponse)
async def predict(celsius: float) -> ModelPredictResponse:
    try:
        response: float = model_predict(celsius=celsius)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return ModelPredictResponse(result=response)
    