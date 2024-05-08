# Elemento marketplace

### Specs

- Container [FTP](https://hub.docker.com/r/stilliard/pure-ftpd)
  - User: `admin`
  - Pass: `change_me`
  - `ftp://admin:change_me@leader_node_ip`
- One or more containers DB [MariaDB](https://hub.docker.com/_/mariadb) with dashboard [phpmyadmin](https://hub.docker.com/_/phpmyadmin)

- Container to execute [cronjob](https://github.com/alseambusher/crontab-ui)
- One or more containers for mail server with dashboard [Docker Mailserver](https://github.com/docker-mailserver/docker-mailserver)
- Container front-end (webserser) ([nginx](https://hub.docker.com/_/nginx))
- Container reverse proxy with SSL [traefik](https://doc.traefik.io/traefik/)
- Container [PHP FPM](https://hub.docker.com/layers/library/php/fpm-alpine3.19/images/sha256-4df626957fe8907b11d439553e830fbd815737a2c3ad15af912152ef2958ccf9?context=explore) - v7 or later
- [Portainer](https://docs.portainer.io/user/docker/stacks)
- [traefik](https://doc.traefik.io/traefik/)
  - NOTE: the acme.json file must be set with the 600 permission
- [homepage](https://github.com/gethomepage/homepage)
- homepage autoconfig (traefik-discovery)
  - NOTE: the services.yaml must be set with the 600 permission
  - The container is reachable only inside the docker network, use crontab to do the update (or refresh) of services, here the command:
  ```
  curl -X POST services-discovery:5001/api/v1/homepage/update
  or
  curl -X POST services-discovery:5001/api/v1/homepage/refresh (delete and recreate all services)
  ```


### Environment variables
In order to change the default values and password of the docker compose, you can create a `.env` file in the root of the project and set the variables you want to change. `.env.template` can be used as a template renaming it to `.env`.

### System design

![System design](./img/system-design.png)

### Starting the Stack

Define an `.env` file in order to set the environment variables of ftp server, mariadb and phpmyadmin.<br>
To start the stack using docker stack deploy, run the following command with admin privileges:
```bash
chmod -R 755 php
chmod 600 traefik/acme.json
chmod 600 homepage/config/services.yaml
docker network create --driver overlay net
docker stack deploy --compose-file docker-compose.yml web
```

A setup script is available in the `scripts` folder in order to
- customize the hostname in the docker compose;
- set the credentials (of traefik basic auth) for the services;
- setup the permissions of the acme.json and services.yaml files;
- create the network (optional);
- deploy the stack (optional).

```bash
python3 scripts/setup.py <customer_name> <password> [-p] [path] [-n] [-d] [stack_name] [-h]
```

1. **customer_name:** used to customize the hostname and to define the username for the basic auth
2. **password:** for the basic auth
3. `-p` or `--path`: pass the path to use in order to go to the root of the project
4. `-n` or `--network`: to create the docker network
5. `-d` or `--deploy`: to deploy the stack
6. **stack_name:** the name of the stack (default: production)
7. `-h` or `--help`

## Ansible playbook

```bash
ansible-playbook playbook.yaml -e "customer=my_customer traefik_password=my_password deploy=-d"
```


## Start the Mail service (Server side)
Start the swarm and run the following command to add a user to the mail server (mandatory):
```bash
docker exec -ti <container-name> setup email add user@web.elemento.cloud
```

## Start the Mail service (Client side)
To configure the mail client, use the following settings for Thunderbird:
Open the Thunderbird client and go to the `Account Settings`:
![Thunderbird settings](./img/step-1.png)
Select email esistente, Insert the name, email and password:
![Thunderbird settings](./img/step-2.png)
Then, select `Configura manualmente`:
![Thunderbird settings](./img/step-3.png)
Select `Fatto` and accept the menu pop-up.

### Conventions

In Elemento we use [Google Style coding conventions](https://google.github.io/styleguide/).
