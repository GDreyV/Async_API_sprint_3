FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src .

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# to expose both grpc and http
# anyway we should manage processes on a higher level
CMD ["python", "main.py"]
