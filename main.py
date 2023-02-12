import psycopg2
from fastapi import FastAPI, HTTPException, Depends
from apa_dataclasses import AccountResponse, TransferResponse
from models import Account, Transfer
from database import get_db
from sqlalchemy.orm import Session

app = FastAPI()


# Create a new account
@app.post("/accounts", response_model=None)
async def create_account(account: AccountResponse, session: Session = Depends(get_db)):
    try:
        new_account = Account(balance=account.balance)
        session.add(new_account)
        session.commit() 
        return AccountResponse(id=new_account.id, balance=new_account.balance)
    except:
        session.rollback()
        raise HTTPException(status_code=400, detail="Failed to create account")

# Retrieve account information
@app.get("/accounts/{id}", response_model=None)
async def get_account(id: int, session: Session = Depends(get_db)):
    account = session.query(Account).filter(Account.id == id).first()
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"id": account.id, "balance": account.balance}

# Transfer money from one account to another
@app.post("/transfers")
async def transfer_money(transfer: TransferResponse, session: Session = Depends(get_db)):
    try:
        # Check if the source account has enough funds
        source_account = session.query(Account).filter(Account.id == transfer.source_id).with_for_update().first()
        if source_account is None:
            raise HTTPException(status_code=404, detail="Source account not found")
        if source_account.balance < transfer.amount:
            raise HTTPException(status_code=400, detail="Insufficient funds")
        
        # Check if the target account exists
        target_account = session.query(Account).filter(Account.id == transfer.target_id).with_for_update().first()
        if target_account is None:
            raise HTTPException(status_code=404, detail="Target account not found")
        
        # Perform the transfer
        source_account.balance -= transfer.amount
        target_account.balance += transfer.amount
        session.commit()
        return TransferResponse(detail="Transfer successful")
    except:
        session.rollback()
        raise HTTPException(status_code=400, detail="Failed to transfer money")


@app.get("/")
async def root():
    return {"message": "Hello World"}

