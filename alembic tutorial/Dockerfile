FROM python:3.10

WORKDIR /app

COPY ./requirement.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./App /app/App
COPY ./alembic /app/alembic
COPY ./alembic.ini /app/alembic.ini

CMD ["uvicorn", "app.fetch:app", "--host", "0.0.0.0", "--port", "80"]