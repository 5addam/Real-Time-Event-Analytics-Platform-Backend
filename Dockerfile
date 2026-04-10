#parent image
FROM python:3.13.7-alpine3.21

# Set enviornment variables to prevent Python from writing pyc files and to buffer output
ENV PYTHONDONTWRITEBYTECODE=1
#Ensure stdou and stderr are not buffered, which is important for logging in Docker containers
ENV PYTHONUNBUFFERED=1

#Set the working directory in the container
WORKDIR /EVENT_ANALYTICS_PLATFORM_BE

#Install system dependencies
RUN apk update && apk add --no-cache \
    build-base \
    postgresql-dev \
    && rm -rf /var/cache/apk/*

#Copy the requirements file into the container
COPY requirements.txt /EVENT_ANALYTICS_PLATFORM_BE
#Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Copy the rest of the application code into the container
COPY . /EVENT_ANALYTICS_PLATFORM_BE

#Expose the port that the application will run on
EXPOSE 8000