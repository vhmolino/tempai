from pydantic import BaseModel

class ModelFitRequestPair(BaseModel):
    fahrenheit: float
    celsius: float

class ModelFitRequest(BaseModel):
    data: list[ModelFitRequestPair]