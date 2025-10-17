FROM python:3.10-slim

RUN apt-get update && apt-get install -y python3-tk python3-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY piiista.py .

CMD ["python", "piiista.py"]

