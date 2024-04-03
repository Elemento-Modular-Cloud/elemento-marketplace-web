# Elemento marketplace

### Specs

- Container per accesso [FTP](https://hub.docker.com/r/stilliard/pure-ftpd)
- Uno o piu' container DB [MySQL](https://hub.docker.com/_/mysql) con dashboard [phpmyadmin](https://hub.docker.com/_/phpmyadmin)
- Container per esecuzione [cronjob](https://github.com/alseambusher/crontab-ui)
- Uno o piu' container per mail server con dashboard per creazione account [Mailu](https://mailu.io/2.0/index.html)
- Container di front-end per webserver ([nginx](https://hub.docker.com/_/nginx))
- Container per gestione certificati SSL (i.e. swag) - via [traefik](https://doc.traefik.io/traefik/)
- Container per esecuzione [PHP FPM](https://hub.docker.com/layers/library/php/fpm-alpine3.19/images/sha256-4df626957fe8907b11d439553e830fbd815737a2c3ad15af912152ef2958ccf9?context=explore) da v7 a successive
- [Portainer](https://docs.portainer.io/user/docker/stacks)
- [traefik](https://doc.traefik.io/traefik/)
  - NOTE: the acme.json file must be set with the 600 permission
- [homepage](https://github.com/gethomepage/homepage)
- [homepage autoconfig](https://hub.docker.com/r/nicolagutierrez/traefik-discovery)
  - NOTE: the services.yaml must be set with the 600 permission
  - The container is reachable only inside the docker network, use crontab to do the update of services, here the command:
  ```
  curl -X POST services-discovery:5001/api/v1/homepage/update
  ```



### System design

![System design](./img/system-design.png)

### Starting the Stack

To start the stack using `docker stack deploy`, run the following command:
```bash
docker stack deploy --compose-file docker-compose.yml web
```

## Start the Mail service
To start the mail stack use another VM and run the commands as explained in the "mailu" folder.
That service works on docker-compose.

### Conventions

In Elemento we use [Google Style coding conventions](https://google.github.io/styleguide/).

