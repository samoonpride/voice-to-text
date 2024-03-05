# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

ENV WORKERS=2

# Set the working directory in the container to /app
WORKDIR /app/voice-to-text

# Add the current directory contents into the container at /app
ADD . .

# Upgrade pip
RUN pip install --upgrade pip

# Install production dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8001 available to the world outside this container
EXPOSE 8001

# Create a non-root user to run the application
RUN useradd -m myuser
USER myuser

# Run gunicorn when the container launches
CMD gunicorn -w ${WORKERS} -b :8001 voice_to_text:app
