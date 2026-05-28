FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY crm/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY crm/ .

RUN mkdir -p logs

EXPOSE 3042

ENV PYTHONUNBUFFERED=1

CMD ["python", "-m", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "3042"]