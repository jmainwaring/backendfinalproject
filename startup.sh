# startup.sh: script to create docker containers

# Stop containers that are running 
docker stop web mysql-server


# Prune
docker system prune -f



# Create network
docker network create sql-network


# Run SQL container
docker run -d --name mysql-server --network sql-network -e MYSQL_ROOT_PASSWORD=secret mysql --default-authentication-plugin=mysql_native_password



# Build and create container with web app
docker build -t webserver .
docker run --network sql-network --name web -d -e FLASK_APP=webapp.py -p 5000:5000 webserver


# Launching the SQL shell
sleep 12
docker run -it --rm --network sql-network mysql sh -c 'exec mysql -h"mysql-server" -P"3306" -uroot -p"secret"'