# Mailserver Mailu

## Docs
- [Mailu](https://mailu.io/2.0/index.html)

## Setup
In order to setup an account:
```
docker exec -ti mailserver setup email add user@mail.web.elemento.cloud
```

Considering docker swarm, it is possible to do it directly from the container.
```
setup email add user@mail.web.elemento.cloud
```