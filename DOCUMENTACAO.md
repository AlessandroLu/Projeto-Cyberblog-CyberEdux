# Documentação

## Criação do Ambiente Virtual do Python Linux/Windows

Windows

```python
py -m venv nome_ambiente # Cria ambiente

```

```python
nome_ambiente/scripts/activate # Ativar ambiente
```

Linux

```python
virtualenv nome_ambiente # Cria  ambiente
```

```python
source .venv/bin/activate # Ativar ambiente
```

# Inicializando Projeto

### Instalação pacote necessários no projeto

```python
pip install -r requirements.txt
```

### Criando as Migrações e o Banco de Dados Db.sqlite
####  \*caso esteja pelo CMD

```python
py manage.py makemigrations && py manage.py migrate
```

Ou

```python
py manage.py makemigrations
```

```python
py manage.py migrate
```

## Criação superuser para acesso inicial ao sistema

```python
 py manage.py createsuperuser
```

### Inicializando Servidor Django

```python
py manage.py runserver
```

