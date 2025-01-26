FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y net-tools curl iputils-ping && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 6999

CMD ["uvicorn", "fastapi_main:app", "--host", "0.0.0.0", "--port", "6999"]