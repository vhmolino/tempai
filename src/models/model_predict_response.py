from pydantic import BaseModel

class ModelPredictResponse(BaseModel):
    result: float