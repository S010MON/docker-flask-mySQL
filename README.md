#### Installation Guide

Ensure that docker and docker-compose are installed

        docker version
        docker-compose --version
        
#### To run just the API  (Ensure to remove links to database)
Navigate to the `docker-flask-mySQL` top level directory

        sudo docker build
        sudo docker run .

#### To run both containers (ie with db)
Build the container

        sudo docker-compose build
        
Run the container
        
        sudo docker-compose up
       
#### TEMPORARILY [While docker auto-initdb isn't working]
List all running containers:

        sudo docker ps

Take the name of the container running the database and insert it into the below command in a new terminal

        sudo docker exec -it [CONTAINER_NAME] bash

The command should look like, or very similar to this:

        sudo docker exec -it docker-flask-mysql bash

Your prompt should change to a `#` now log into mysql

        mysql -u root -p
        password: password
        
Load in the database script from db/init.sql
