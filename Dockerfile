# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /usr/src/code

# Copy the current directory contents into the container at /app
COPY requirements.txt /usr/src/code

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP main.py
ENV FLASK_ENV development
ENV FLASK_RUN_PORT 8000
ENV FLASK_RUN_HOST 0.0.0.0

# Make port 80 available to the world outside this container
EXPOSE 8000

CMD ["flask", "run"]