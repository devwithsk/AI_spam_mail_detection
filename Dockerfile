FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs

# Copy backend files
COPY app.py .
COPY main.py .
COPY requirements.txt .
COPY mail_data.csv .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Train the model
RUN python main.py

# Copy frontend files
COPY frontend ./frontend

WORKDIR /app/frontend

# Install frontend dependencies
RUN npm install

# Build frontend
RUN npm run build

# Back to app root
WORKDIR /app

EXPOSE 5000 3000

# Run both backend and frontend
CMD ["sh", "-c", "python app.py & cd frontend && npx serve -s build -l 3000"]
