
# Iniciar o Sistema

## Requisitos 
### Ter o Docker instalado

<https://www.docker.com>

### Ter o Docker Compose instalado

<https://docs.docker.com/compose/install/>

## Iniciar o Sistema

Executar o comando abaixo na raiz do projeto

```bash
    docker-compose up -d
```
para verificar se os container foram executados com sucesso, executar o comando abaixo

```bash
    docker ps
```

## Acessando os sistema

### Dashboard

<http://localhost:3000>

### adminer do banco

<http://localhost:8080>

### porta para acesso direto ao postgress

- 5432

### Acesso ao banco 

MB_DB_TYPE: postgres
nome do bd: Coopana
porta: 5432
usuário: Coopana
senha: 1234567890
host: db