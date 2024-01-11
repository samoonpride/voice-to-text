# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app/voice-to-text

# Add the current directory contents into the container at /app
ADD . .

# Upgrade pip
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 8001

# Run gunicorn when the container launches
CMD ["gunicorn", "-w", "4", "-b", ":8001", "voice-to-text:app"]