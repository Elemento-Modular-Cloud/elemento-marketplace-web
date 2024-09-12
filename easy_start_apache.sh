bash -c "cd php && sudo docker build -t php-custom-apache -f Dockerfile-apache ."
sudo docker network create --driver overlay net-apache
sudo docker stack deploy --compose-file docker-compose-apache.yml web-apache


