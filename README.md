# FastAPI Product API

A simple RESTful API built with **FastAPI** and **MySQL** for managing products.  
This project demonstrates CRUD operations on a product database using SQLAlchemy ORM and Pydantic models.



## Features

- Create, Read, Update, Delete (CRUD) product records
- Data validation with Pydantic schemas
- SQLAlchemy ORM integration with MySQL
- FastAPI for fast and easy API development


## Technology

- Python 3.10+
- FastAPI
- Uvicorn (ASGI server)
- SQLAlchemy
- MySQL (with `mysql-connector-python` driver)
- Pydantic


Setup MySQL database named products_db to store product data.

Created SQLAlchemy models to represent the Product table schema.

Configured database connection URL (DATABASE_URL) to connect FastAPI to MySQL.

Defined Pydantic schemas to validate and serialize product data for API endpoints.

Created FastAPI routes (endpoints) to handle CRUD operations:

Add new products

Get product details

Update existing products

Delete products

Started the FastAPI server using Uvicorn to serve the API on your local machine.
