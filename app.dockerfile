# Base image
FROM python:3.7-slim

# install python
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*

RUN mkdir ./mlops
WORKDIR ./mlops

COPY requirements.txt requirements.txt
COPY setup.py setup.py
COPY src/ src/
COPY data/ data/
COPY models/ models/
COPY tests/ tests/
RUN chmod 777 ./models

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
RUN pip install --ignore-installed uvicorn==0.20.0

EXPOSE 80
CMD ["uvicorn", "src.deployment.main:app", "--reload", "--port", "80", "--host", "0.0.0.0"]
