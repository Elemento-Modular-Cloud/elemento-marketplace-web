bash -c "cd php && sudo docker build -t php-custom ."
sudo docker network create --driver overlay net
sudo docker stack deploy --compose-file docker-compose.yml web


