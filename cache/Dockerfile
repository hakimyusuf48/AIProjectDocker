# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /cache

# Install required packages
# It's a good practice to copy requirements first to leverage Docker layer caching
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Command to run the application
CMD [ "python3", "cach.py" ]