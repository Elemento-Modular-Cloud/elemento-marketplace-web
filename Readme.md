# Elemento marketplace

# Specs

- [x] Container per accesso [FTP](https://github.com/delfer/docker-alpine-ftp-server) ([github](https://github.com/delfer/docker-alpine-ftp-server))
  - [ ] Config of users
  - [ ] Config of the address
  - [ ] Check if the volume is shared and usable
- [x] Uno o piu' container [DB MySQL](https://hub.docker.com/_/mariadb) con dashboard [phpmyadmin](https://hub.docker.com/_/phpmyadmin)
  - [ ] Are there some specific requirements (security? speed? ...)?
  - [ ] Lookup on how to handle multiple instances
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

# Conventions

In Elemento we use [Google Style coding conventions](https://google.github.io/styleguide/).

