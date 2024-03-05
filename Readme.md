# Elemento coding conventions

Use this repo as template for new and existing repos


#Specs

- Container per accesso FTP
- Uno o piu' container DB MySQL con dashboard phpmyadmin
- Container per esecuzione cronjob
- Uno o piu' container per mail server con dashboard per creazione account
- Container di front-end per webserver (nginx)
- Container per gestione certificati SSL (i.e. swag)
- Container per esecuzione PHP FPM da v7 a successive
- Portainer
- traefik
- homepage
- homepage autoconfig

# Conventions

In Elemento we use [Google Style coding conventions](https://google.github.io/styleguide/).

## Examples

### Environment variables

`ELEMENTO_ENVIRONMENT_VARIABLE`

### Git repositories

`elemento-function-{client,server}`

### Python
Use flake8 and autopep8 to refactor your code.

```python
class ElementoClass():
    def __init__():
        self.dataMember = None
    
    def get_function():
        pass

```

### C++

### React

### Rust

### Others
