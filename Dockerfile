FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

EXPOSE 1268

HEALTHCHECK CMD curl --fail http://localhost:1268/_stcore/health

ENTRYPOINT ["streamlit", "run", "Home.py", "--server.port=1268", "--server.address=0.0.0.0"]