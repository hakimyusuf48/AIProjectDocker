# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /cache

# Install required packages
COPY requirements.txt .
RUN python -m venv cache \
    source cache/bin/activate \
    pip install -r requirements.txt

# Copy the application code into the container
COPY . .

# Command to run the application
CMD [ "python3", "cach.py" ]
