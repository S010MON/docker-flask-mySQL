## Installation Guide

Ensure that docker and docker-compose are installed

        docker version
        docker-compose --version
        
### To run both containers
Navigate to the `docker-flask-mySQL/` root directory

Build the container:

        sudo docker-compose build
        
Run the container:
        
        sudo docker-compose up

Done!

--------------------------------------------------

## Troubleshooting
### To check that MySQL database has loaded
List all running containers:

        sudo docker ps

Take the name of the container running the database and insert it into the below command in a new terminal

        sudo docker exec -it [CONTAINER_NAME] bash

The command should look like, or very similar to this:

        sudo docker exec -it docker-flask-mysql_db_1 bash

Your prompt should change to a `#` now log into mysql

        $ mysql -u root -p
        $ Enter password: password

If the `SHOW DATABASES` command doesn't show the correct databases load in the database script from the init.sql file 

        SOURCE /docker-entrypoint-initdb.d/init.sql
