from pydantic import BaseModel


class ModelFitResponse(BaseModel):
    result: bool