[Vinícius Matheus Morales](https://github.com/viniciusmm7), [Insper](https://www.insper.edu.br/), 2021

[![Insper Mileage logo](mileage-logo.svg)](https://inspermileage.netlify.app/)

# Mileage REST API

### Enunciado do case

 1. Criar uma API REST utilizando os frameworks [Flask](https://flask.palletsprojects.com/en/2.0.x/) e [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/);
 2. Utilizar um Database relacional (para este projeto foi utilizado o [SQLite](https://www.sqlite.org/index.html)), atualizando esse database localmente. A API deve conter uma tabela `Carros`, com informações como: `modelo`, `marca`, `motor`, `nome de piloto`.
 3. A API deve conter rotas capazes de:
    - Acessar a informação de todos os carros;
    - Adicionar um novo modelo a tabela;
    - Alterar o valor do motor de algum dos modelos;
    - Deletar um dos modelos;
    - Filtrar os carros pelo motor.
 4. `[BÔNUS]` Hospedar a aplicação no "Heroku" ou outro serviço de nuvem para aplicações.

### Documentação da API REST

#### Primeiramente o código deve ser rodado:
```shell
python main.py
```

#### Acessar a informação de todos os carros (no terminal, rode):
```python
get_all()
```

#### Acessar as informações ordenadas pela coluna desejada (`Carros.motor` é o padrão):
```python
get_by(column=Carros.motor)
```

#### Acessar as informações de um carro pelo seu id no banco de dados:
```python
get(id:int)
```

#### Adicionar novas informações no banco de dados:
```python
put(id:int, dados:dict)
```

#### Adicionar novas informações no banco de dados com base em inputs:
```python
put_input(id:int)
```

#### Atualizar as informações de um carro com base no id:
```python
patch(id:int, dados:dict)
```

#### Atualizar as informações de um carro com base no id por meio de inputs:
```python
patch_input(id:int)
```

#### Deletar os dados de um carro com base no id:
```python
delete(id:int)
```
