FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything from root context
COPY . .

# Expose port (Render ignores this but good practice)
EXPOSE 8000

# Set pythonpath so Uvicorn can find ai, recommendation, etc.
ENV PYTHONPATH=/app

# Command to run (working dir is /app/backend to run app.main)
WORKDIR /app/backend
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
