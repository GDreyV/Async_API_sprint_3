FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src src
COPY alembic alembic
COPY alembic.ini alembic.ini

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "22738"]
