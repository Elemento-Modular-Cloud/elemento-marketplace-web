# Elemento marketplace

# Specs

- [x] Container per accesso [FTP](https://hub.docker.com/r/stilliard/pure-ftpd/) ([github](https://github.com/stilliard/docker-pure-ftpd?tab=readme-ov-file))
  - [ ] Config of TLS
  - [ ] Define the scope of ftp-data
- [x] Uno o piu' container [DB MySQL](https://hub.docker.com/_/mariadb) con dashboard [phpmyadmin](https://hub.docker.com/_/phpmyadmin)
- [x] Container per esecuzione cronjob [crontab-ui](https://github.com/alseambusher/crontab-ui)
  - [ ] check on x86
- [ ] Uno o piu' container per [mail server](https://docs.postalserver.io/getting-started) con dashboard per creazione account
- [ ] Container per esecuzione PHP FPM da v7 a successive
- [x] Container per gestione certificati SSL (i.e. swag) (nginx)
  - [ ] to be configured 
- [x] Portainer 
- [x] traefik
  - [ ] check configuration
- [x] homepage 
  - [ ] Integration of services in homepage
- [ ] homepage autoconfig

# System design

![System design](./img/system-design.png)

# Conventions

In Elemento we use [Google Style coding conventions](https://google.github.io/styleguide/).

