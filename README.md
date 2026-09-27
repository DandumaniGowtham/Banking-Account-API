# 🏦 Banking App - FastAPI & MongoDB

A simple Banking REST API developed using **Python, FastAPI, and MongoDB**.

This project provides APIs to manage bank accounts and perform basic banking operations such as creating accounts, updating account details, depositing money, withdrawing money, and retrieving account information.

## 🚀 Features

- Create a new bank account
- Get all bank accounts
- Get a specific account by ID
- Update account details
- Delete an account
- Deposit money
- Withdraw money
- Automatic MongoDB ObjectId generation
- Request validation using Pydantic
- RESTful API endpoints

## 🔗 Available APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/accounts` | Get all bank accounts |
| `GET` | `/accounts/{id}` | Get a specific account by ID |
| `POST` | `/accounts` | Create a new bank account |
| `PUT` | `/accounts/{id}` | Update account details |
| `DELETE` | `/accounts/{id}` | Delete a bank account |
| `POST` | `/accounts/{id}/deposit` | Deposit money into an account |
| `POST` | `/accounts/{id}/withdraw` | Withdraw money from an account |



## 🛠️ Technologies Used

- **Python 3.10**
- **FastAPI**
- **MongoDB**
- **PyMongo**
- **Pydantic**
- **Uvicorn**
- **Postman** for API testing

## 📁 Project Structure

```text
Banking_App/
│
├── main.py
├── README.md
└── requirements.txt
```
