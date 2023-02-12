from pydantic import BaseModel
from typing import Optional, List

# Define the account model
class AccountResponse(BaseModel):
    id: Optional[int] = None
    balance: Optional[float] = None

# Define the transfer model
class TransferResponse(BaseModel):
    source_id: Optional[int] = None
    target_id: Optional[int] = None
    amount: Optional[float] = None
