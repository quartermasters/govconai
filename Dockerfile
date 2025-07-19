# Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend application code
ENV PYTHONPATH=/app
COPY ./backend /app
COPY ./scripts /app/scripts
