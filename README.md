# Repo Contents

- gateway.py: API gateway
- backend_service.py: backend service, handling requests
- models.py: database table(s)
- crud.py: database operations
- database.py: create a database
- test_requests.py: send test requests to API gateway

# Dependencies 

## setup a virtual environment for development:

setup:
python3 -m venv path/to/venv
source path/to/venv/bin/activate

dependencies:
python3 -m pip install fastapi uvicorn

## fastapi & uvicorn:

pip install fastapi uvicorn

install all standard dependencies: pip install "fastapi[standard]"   

## sqlalchemy

pip install sqlalchemy
pip install "sqlalchemy[asyncio]"
pip install psycopg2-binary  # for PostgreSQL

## requests

pip install requests

## all dependencies

pip install fastapi uvicorn sqlalchemy psycopg2-binary requests

# running the services

## API gateway: gateway.py

uvicorn gateway:app --port 8000 --reload

## Backend Service: backend_service.py

uvicorn backend_service:app --port 8001 --reload

# running tests

python3 test_requests.py

curl http://localhost:8000/users/

# additional notes

- run fastapi in dev mode: fastapi dev main.py
- run fastapi in production mode: fastapi run
- Go to url/docs to see auto-generated docs
- Testing - https://fastapi.tiangolo.com/tutorial/testing/#extended-testing-file
- Debugging - https://fastapi.tiangolo.com/tutorial/debugging/
- for production - run with gunicorn - gunicorn -k uvicorn.workers.UvicornWorker main:app
- curl http://localhost:8000/API_PATH

