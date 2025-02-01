FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies required for building packages like psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first to leverage Docker cache if requirements don't change
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the application port
EXPOSE 1268

# Define a healthcheck (modify the URL if needed)
HEALTHCHECK CMD curl --fail http://localhost:1268/_stcore/health || exit 1

# Set the entrypoint to run the Streamlit app
ENTRYPOINT ["streamlit", "run", "Home.py", "--server.port=1268", "--server.address=0.0.0.0"]
