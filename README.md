*** Prerequisites ***

fastapi / uvicorn:

pip install fastapi uvicorn

python3 -m venv path/to/venv
source path/to/venv/bin/activate
python3 -m pip install fastapi uvicorn

pip install sqlalchemy
pip install "sqlalchemy[asyncio]"
pip install psycopg2-binary  # for PostgreSQL

pip install requests

all:

pip install fastapi uvicorn sqlalchemy psycopg2-binary requests

*** to run example get api server ***

uvicorn main:app --reload




## temp notes - todo move to separate location before github push

curl http://localhost:8000/API_PATH



create virtual environment: python3 -m venv venv
activate virtual environment: source myenv/bin/activate
run python file: python3 name.py

running uvicorn application server: uvicorn gateway:app --port 8000 --reload
running uvicorn backend seevice - uvicorn service_user:app --port 8001 --reload

run fastapi in dev mode: fastapi dev main.py
run fastapi in production mode: fastapi run

Go to url/docs to see auto-generated docs

Testing - https://fastapi.tiangolo.com/tutorial/testing/#extended-testing-file

Debugging - https://fastapi.tiangolo.com/tutorial/debugging/

for production - run with gunicorn - gunicorn -k uvicorn.workers.UvicornWorker main:app

for production - set this up to run with docker containers on the host machine
for production - add a frontend to use the api 

install all standard dependencies: pip install "fastapi[standard]"    

more venv stuff:
python3 -m venv path/to/venv 
source path/to/venv/bin/activate