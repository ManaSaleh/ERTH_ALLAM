# Use an official Python runtime as the base image
FROM python:3.12.5

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container
COPY . .

# Expose port 8000 (or the port FastAPI uses)
EXPOSE 8000

# Run the FastAPI app with Uvicorn
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["fastapi" , "run" , "app.py"]