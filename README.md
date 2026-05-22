# FastAPI APP WITH CRUD ENDPOINTS FOR ITEMS

A simple CRUD (Create, Read, Update, Delete) API built using FastAPI and Pydantic.

## Features

- Create Item
- Get All Items
- Get Single Item
- Update Item
- Delete Item
- Swagger API Documentation

---

## Technologies Used

- FastAPI
- Pydantic
- Uvicorn
- Python

---

## Installation

### Clone Repository

```bash
git clone https://github.com/ChadubulaVani/fastapi-crud-api.git
```

### Go to Project Folder

```bash
cd fastapi-crud-api
```

### Install Dependencies

```bash
pip install fastapi uvicorn
```

---

## Run Server

```bash
uvicorn main:app --reload
```

Server runs at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Redoc:

```text
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

### Home Route

```http
GET /
```

---

### Create Item

```http
POST /items
```

Example Body:

```json
{
  "id": 1,
  "name": "Laptop",
  "price": 50000
}
```

---

### Get All Items

```http
GET /items
```

---

### Get Single Item

```http
GET /items/{item_id}
```

---

### Update Item

```http
PUT /items/{item_id}
```

---

### Delete Item

```http
DELETE /items/{item_id}
```

---

## Author

Chadubula Vani