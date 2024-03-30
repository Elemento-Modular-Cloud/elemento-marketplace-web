# Mailserver Mailu

## Docs
- [Mailu](https://mailu.io/2.0/index.html)

## Setup
To launch:
```
cd /mailu
docker compose -f mailserver-compose.yml up -d
```

In order to setup an account:
```
docker compose -p mailu exec admin flask mailu admin postmaster mail.web.elemento.cloud password
```