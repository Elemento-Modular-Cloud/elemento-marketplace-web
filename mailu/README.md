# Mailserver Mailu

## Docs
- [Mailu](https://mailu.io/2.0/index.html)
- [YouTube Tutorial](https://www.youtube.com/watch?v=ScarlmgD0dU)

## Setup
It is very important to change the SECRET_KEY in the mailu.env with a random generated 16 characters key on every deployment:
```
SECRET_KEY=xxxxxxxxxxxxxxxx
```

To launch:
```
cd mailu

docker compose -f mailserver-compose.yml up -d
```

In order to setup an initial account:
```
docker compose -p mailu exec admin flask mailu admin postmaster mail.web.elemento.cloud password
```

Test admin account (MUST be changed):
E-mail: postmaster@mail.web.elemento.cloud
password: password
