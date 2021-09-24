# Filename: Dockerfile

# Base Image
FROM python:latest

# Update
RUN apt-get -y update

# Add all python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install mySQL
# RUN apt-get install -y mysql-server

# Expose the API endpoint
 EXPOSE 5000

# Copy the application files
ADD . .
WORKDIR /server

#CMD [ "service mysql start" ]
#CMD [ "mysql" ]
#CMD [ "SOURCE", "./dbms/pizzas_structure.sql;" ]
#CMD [ "SOURCE", "./dbms/pizzas_data.sql;" ]  

#CMD [ "python3","./PizzaService.py" ]

