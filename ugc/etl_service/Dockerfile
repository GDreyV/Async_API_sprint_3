FROM python:3.11-alpine

WORKDIR /opt/app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

ENTRYPOINT ["python", "etl.py"]
