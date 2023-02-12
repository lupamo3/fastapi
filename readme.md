
# Money Transfer API
This is a FastAPI application for money transfer between accounts. The application uses SQLAlchemy as the ORM and psycopg2 as the PostgreSQL adapter.

### Clone the repository:

```
git clone https://github.com/lupamo3/money-transfer-api.git
Navigate to the repository:
cd money-transfer-api
Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate
Install the required dependencies:
pip install -r requirements.txt
Set up the PostgreSQL database:
createdb money_transfer
psql -d money_transfer -f db/schema.sql
```

### Usage
```
Start the application:
uvicorn main:app --reload
Open your browser and navigate to http://localhost:8000/docs to see the API documentation.
Endpoints
```

### The following endpoints are available in the API:
```http
  GET /accounts/{id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id of the account` | `int` | **Retrieve** information about an account. |

#### POST /accounts

```http
  POST /accounts
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `balance`      | `string` | Create a new account. |
| `id`      | `string` | Create a new account. |

#### POST /transfers

```http
  POST /transfers
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `source_id`      | `int` | The ID of the source account. |
| `target_id`      | `int` | The ID of the target account. |
| `amount`      | `string` | The amount of money to transfer. |



### Response:
```

200 OK: The transfer was successful.

400 Bad Request: Failed to transfer money.

404 Not Found: Source account or target account was not found.
```


