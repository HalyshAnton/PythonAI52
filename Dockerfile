FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install fastapi uvicorn[standard]

COPY . .

ENV HOST="0.0.0.0"
ENV PORT=8080

EXPOSE 8080

# run via python (not uvicorn CLI)
CMD ["python", "main.py"]