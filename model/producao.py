from pydantic import BaseModel, Field
from typing import Optional

class Producoes(BaseModel):
    producoes_id: Optional[str] = None
    pesquisadores_id: str
    issn: str
    nomeartigo: str
    anoartigo: int
