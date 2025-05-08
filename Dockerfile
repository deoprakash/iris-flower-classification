# Use official Python image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy project files
COPY app/ /app/


# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Flask app
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
