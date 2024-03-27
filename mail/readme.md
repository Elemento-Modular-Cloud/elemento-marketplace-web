
To start your compose project, simply run the Docker Compose `up` command using `-p mailu` flag for project name.

```
cd /mailu
docker compose -p mailu up -d
```

Before you can use Mailu, you must create the primary administrator user account. This should be admin@elemento.cloud. Use the following command, changing PASSWORD to your liking:
```
docker compose -p mailu exec admin flask mailu admin admin elemento.cloud PASSWORD
```

Login to the admin interface to change the password for a safe one, at one of the hostnames elemento.mail.cloud. Also, choose the "Update password" option in the left menu.
