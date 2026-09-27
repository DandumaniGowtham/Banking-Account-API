from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from pymongo import MongoClient
from bson.objectid import ObjectId


connection = MongoClient("mongodb://localhost:27017/")
db = connection["banking_db"]
collection = db["accounts"]

class Account_Model(BaseModel):
    name: str = Field(..., description="Enter Account holder name: ")
    account_no : str = Field(..., description="Enter Account Number: ")
    balance: Optional[int] = Field(default=0, ge=0)

class Update_Account(BaseModel):
    name: str = Field(..., description="Enter Account holder name")
    account_no: str = Field(..., description="Enter Account Number")

class Deposit_Model(BaseModel):
    amount: int = Field(..., gt=0, description="Enter amount to deposit")


app = FastAPI()

@app.get("/accounts")
def get_accounts():
    collection_cursor = collection.find()

    result = []
    for account in collection_cursor:
        account["_id"] = str(collection["_id"])
        result.append(account)

    if not result:
        return "no accounts found"
    
    return result

@app.get("/accounts/{id}")
def get_account(id: str):
    collection_cursor = collection.find_one({"_id":ObjectId(id)})

    if not collection_cursor:
        return "invalid account id"

    collection_cursor["_id"] = str(collection_cursor["_id"])
    return collection_cursor

@app.post("/accounts")
def create_Account(account_Details: Account_Model):
    if not account_Details:
        return "Values Missing"

    account_data = account_Details.model_dump()
    insert = collection.insert_one(account_data)

    return {
        "Message: ": "Account created",
        "Account_Id ": str(insert.inserted_id)
    }


@app.put("/accounts/{id}")
def update_account(id:str, account: Update_Account):
    if not account:
        return "Required user details to update"

    account_data = account.model_dump()

    updated_info = collection.find_one_and_update({"_id": ObjectId(id)}, {"$set" : account_data})

    updated_info["_id"] = str(updated_info["_id"])

    return {
        "Message ": " Updated Successfully",
        "Account_Id ": updated_info["_id"]
    }

@app.delete("/accounts/{id}")
def delete_account(id:str):

    deleted_info = collection.find_one_and_delete({"_id": ObjectId(id)})

    return {
        "Message: ": "Account Deleted Successfully",
        "Account: ": deleted_info
    }


@app.post("/accounts/{id}/deposit")
def deposit_amount(id:str, deposit: Deposit_Model):

    result = collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$inc":{"balance" : deposit.amount} }
    )

    if not result:
        return "No Account Found"

    account = collection.find_one({
        "_id": ObjectId(id)
    })

    return {
        "Message :" : "Amount Deposited Successfully",
        "Amount Deposited :" : deposit.amount,
        "Total Balance :": account["balance"]
    }

@app.post("/accounts/{id}/withdraw")
def withdraw_amount(id:str, deposit: Deposit_Model):

    result = collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$inc":{"balance" : -deposit.amount} }
    )
                        
    if not result:
        return "No Account Found"

    account = collection.find_one({
        "_id": ObjectId(id)
    })

    return {
        "Message :" : "Amount withdrawn Successfully",
        "Amount Withdrawn :" : deposit.amount,
        "Total Balance :": account["balance"]
    }


