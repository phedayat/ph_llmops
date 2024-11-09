from pydantic import BaseModel

from src.ph_llmops.prompting.builder import get_schema_from_model

def test_get_schema_from_model():
    class Test(BaseModel):
        p1: str
        p2: int
        p3: float
    
    assert get_schema_from_model(Test) == {
        "p1": "annotation=str required=True",
        "p2": "annotation=int required=True",
        "p3": "annotation=float required=True",
    }