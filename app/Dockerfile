# Filename: Dockerfile

# Base Image
FROM python:latest

# Update
RUN apt-get -y update
RUN apt-get -y install vim nano

# Add all python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Expose the API endpoint
EXPOSE 5000

# Copy the application files
ADD . .
WORKDIR /app
ENTRYPOINT [ "python" ]
CMD [ "./tests/test.py" ]
CMD [ "./PizzaService.py" ]


