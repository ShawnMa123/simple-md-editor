# Use official Python runtime as base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose port 5000
EXPOSE 5000

# Set environment variables
ENV UPLOAD_FOLDER=/app/static/images

# Create upload directory
RUN mkdir -p ${UPLOAD_FOLDER}

# Run the application
CMD ["python", "app.py"]