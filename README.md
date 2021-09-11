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

### Alguns tipos de [requisições](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods) e [códigos de status de respostas HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status):
- [GET](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods/GET)
- [PUT](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods/PUT)
- [DELETE](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods/DELETE)
- [PATCH](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods/PATCH)
- [200 OK](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/200)
- [201 Created](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/201)
- [404 Not Found](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/404)
- [409 Conflict](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/409)

## Documentação da API REST

### A API REST roda com base no endereço local `http://127.0.0.1:5000/carros/`

### A instalação do arquivo `requirements.txt` deve ser feita antes de iniciar a aplicação da seguinte forma:
```shell
pip install -r requirements.txt
```

## 1. Primeiramente o servidor deve ser iniciado como o exemplo:
`Windows + R -> cmd -> ENTER`
```shell
Microsoft Windows [versão 10.0.19043.1165]
(c) Microsoft Corporation. Todos os direitos reservados.

C:\Users\seu-user>cd Downloads\Mileage-REST-API

C:\Users\seu-user\Downloads\Mileage-REST-API>python main.py
```

## 2. `put(id:int, dados:dict)` - Adicionar novas informações no banco de dados:
```python
>>> from main import *
>>> data = [{'piloto': 'Amaral', 'modelo': 'Senna', 'marca': 'McLaren', 'motor': '4.0'},
...         {'piloto': 'Luciano', 'modelo': '488 Spider', 'marca': 'Ferrari', 'motor': '3.9'},
...         {'piloto': 'Luis', 'modelo': 'Urus', 'marca': 'Lamborghini', 'motor': '4.0'},
...         {'piloto': 'Gustavo', 'modelo': '918 Spyder', 'marca': 'Porsche', 'motor': '4.6'},
...         {'piloto': 'Bruno', 'modelo': 'AMG GT', 'marca': 'Mercedes-benz', 'motor': '4.0'}]
>>> for id in data:
...     put(data.index(id), id)
Iniciando put request no id 0:
{'id': 0, 'piloto': 'Amaral', 'modelo': 'Senna', 'marca': 'McLaren', 'motor': '4.0'}
Pressione ENTER para continuar


Iniciando put request no id 1:
{'id': 1, 'piloto': 'Luciano', 'modelo': '488 Spider', 'marca': 'Ferrari', 'motor': '3.9'}
Pressione ENTER para continuar


Iniciando put request no id 2:
{'id': 2, 'piloto': 'Luis', 'modelo': 'Urus', 'marca': 'Lamborghini', 'motor': '4.0'}
Pressione ENTER para continuar


Iniciando put request no id 3:
{'id': 3, 'piloto': 'Gustavo', 'modelo': '918 Spyder', 'marca': 'Porsche', 'motor': '4.6'}
Pressione ENTER para continuar


Iniciando put request no id 4:
{'id': 4, 'piloto': 'Bruno', 'modelo': 'AMG GT', 'marca': 'Mercedes-benz', 'motor': '4.0'}
Pressione ENTER para continuar
```

Do lado do servidor podemos ver que as requisições de PUT foram bem sucedidas:
```shell
127.0.0.1 - - [10/Sep/2021 13:52:24] "PUT /carros/1 HTTP/1.1" 200 -
127.0.0.1 - - [10/Sep/2021 13:52:24] "PUT /carros/2 HTTP/1.1" 200 -
127.0.0.1 - - [10/Sep/2021 13:52:25] "PUT /carros/3 HTTP/1.1" 200 -
127.0.0.1 - - [10/Sep/2021 13:52:25] "PUT /carros/4 HTTP/1.1" 200 -
```

No caso de já existirem dados nos IDs que estiver tentando dar um PUT, ele retornará:
```shell
Iniciando put request no id 0:
{'message': 'Conflito com o servidor, o id ja esta preenchido'}
Pressione ENTER para continuar


Iniciando put request no id 1:
{'message': 'Conflito com o servidor, o id ja esta preenchido'}
Pressione ENTER para continuar


Iniciando put request no id 2:
{'message': 'Conflito com o servidor, o id ja esta preenchido'}
Pressione ENTER para continuar


Iniciando put request no id 3:
{'message': 'Conflito com o servidor, o id ja esta preenchido'}
Pressione ENTER para continuar


Iniciando put request no id 4:
{'message': 'Conflito com o servidor, o id ja esta preenchido'}
Pressione ENTER para continuar
```

E no servidor:
```shell
127.0.0.1 - - [10/Sep/2021 13:55:23] "PUT /carros/0 HTTP/1.1" 409 -
127.0.0.1 - - [10/Sep/2021 13:55:26] "PUT /carros/1 HTTP/1.1" 409 -
127.0.0.1 - - [10/Sep/2021 13:55:26] "PUT /carros/2 HTTP/1.1" 409 -
127.0.0.1 - - [10/Sep/2021 13:55:27] "PUT /carros/3 HTTP/1.1" 409 -
127.0.0.1 - - [10/Sep/2021 13:55:27] "PUT /carros/4 HTTP/1.1" 409 -
```

## 3. `patch(id:int, dados:dict)` - Atualizar as informações de um carro com base no id:
```python
>>> patch(4, {'piloto': 'Vinícius',
...          'marca': 'Koenigsegg',
...          'modelo': 'Regera',
...          'motor': '5.0'})
Iniciando patch request no id 4:
{'id': 4, 'piloto': 'Vinícius', 'modelo': 'Regera', 'marca': 'Koenigsegg', 'motor': '5.0'}
Pressione ENTER para continuar
```

E no servidor (200 = OK):
```shell
127.0.0.1 - - [10/Sep/2021 13:57:55] "PATCH /carros/4 HTTP/1.1" 200 -
```

## 4. `put_input(id:int)` - Adicionar novas informações no banco de dados com base em inputs:
```python
>>> put_input(5)
Iniciando put_input request no id 5:
Nome do piloto: Bruno
Marca do carro: Italdesign
Modelo do carro: Zerouno
Motor do carro (exemplo: 1.0): 5.2
{'id': 5, 'piloto': 'Bruno', 'modelo': 'Zerouno', 'marca': 'Italdesign', 'motor': '5.2'}
Pressione ENTER para continuar
```

E no servidor:
```shell
127.0.0.1 - - [10/Sep/2021 14:08:43] "PUT /carros/5 HTTP/1.1" 200 -
```

No caso de já existirem dados nos IDs que estiver tentando dar um PUT, ele retornará:
```shell
Iniciando put_input request no id 5:
Nome do piloto: Bruno
Marca do carro: Italdesign
Modelo do carro: Zerouno
Motor do carro (exemplo: 1.0): 5.2
{'message': 'Conflito com o servidor, o id ja esta preenchido'}
Pressione ENTER para continuar
```

E no servidor (409 = Conflito):
```shell
127.0.0.1 - - [10/Sep/2021 14:15:43] "PUT /carros/5 HTTP/1.1" 409 -
```

## 5. `patch_input(id:int)` - Atualizar as informações de um carro com base no id por meio de inputs:
```python
>>> patch_input(id:int)
Iniciando patch_input request no id 4:
Nome do piloto:
Marca do carro:
Modelo do carro:
Motor do carro (exemplo: 1.0):

Os dados não podem estar todos vazios, tente novamente
Nome do piloto: Ricardo
Marca do carro: Aston Martin
Modelo do carro: Vulcan
Motor do carro (exemplo: 1.0): 7.0
{'id': 4, 'piloto': 'Ricardo', 'modelo': 'Vulcan', 'marca': 'Aston Martin', 'motor': '7.0'}
```

E no servidor:
```shell
127.0.0.1 - - [10/Sep/2021 14:19:09] "PATCH /carros/4 HTTP/1.1" 200 -
```

## 6. `delete(id:int)` - Deletar os dados de um carro com base no id:
```python
>>> delete(5)
Iniciando delete request no id 5:
Deletando o carro de id 5
{
    "id": 0,
    "piloto": null,
    "modelo": null,
    "marca": null,
    "motor": null
}

Pressione ENTER para continuar
```

E no servidor:
```shell
127.0.0.1 - - [10/Sep/2021 14:20:56] "DELETE /carros/5 HTTP/1.1" 200 -
127.0.0.1 - - [10/Sep/2021 14:20:56] "GET /carros/5 HTTP/1.1" 404 -
```

## 7. `get(id:int)` - Acessar as informações de um carro pelo seu id no banco de dados:
```python
>>> get(3)
Iniciando get request:
{'id': 3, 'piloto': 'Gustavo', 'modelo': '918 Spyder', 'marca': 'Porsche', 'motor': '4.6'}
Pressione ENTER para continuar
```

E no servidor:
```shell
127.0.0.1 - - [10/Sep/2021 14:25:08] "GET /carros/3 HTTP/1.1" 200 -
```

## 8. `get_by(column=Carros.motor)` - Acessar as informações ordenadas pela coluna desejada (`Carros.motor` é o padrão):
```python
>>> get_by(column=Carros.piloto)
Iniciando get_by request:
OrderedDict([('id', 0), ('piloto', 'Amaral'), ('modelo', 'Senna'), ('marca', 'McLaren'), ('motor', '4.0')])

OrderedDict([('id', 3), ('piloto', 'Gustavo'), ('modelo', '918 Spyder'), ('marca', 'Porsche'), ('motor', '4.6')])

OrderedDict([('id', 1), ('piloto', 'Luciano'), ('modelo', '488 Spider'), ('marca', 'Ferrari'), ('motor', '3.9')])

OrderedDict([('id', 2), ('piloto', 'Luis'), ('modelo', 'Urus'), ('marca', 'Lamborghini'), ('motor', '4.0')])

OrderedDict([('id', 4), ('piloto', 'Ricardo'), ('modelo', 'Vulcan'), ('marca', 'Aston Martin'), ('motor', '7.0')])

Pressione ENTER para continuar
```

O padrão para o parâmetro `Column` é `Carros.motor`, então solicitar:
```python
>>> get_by()
```
Retornará ordenado pelo motor:
```
Iniciando get_by request:
OrderedDict([('id', 1), ('piloto', 'Luciano'), ('modelo', '488 Spider'), ('marca', 'Ferrari'), ('motor', '3.9')])

OrderedDict([('id', 0), ('piloto', 'Amaral'), ('modelo', 'Senna'), ('marca', 'McLaren'), ('motor', '4.0')])

OrderedDict([('id', 2), ('piloto', 'Luis'), ('modelo', 'Urus'), ('marca', 'Lamborghini'), ('motor', '4.0')])

OrderedDict([('id', 3), ('piloto', 'Gustavo'), ('modelo', '918 Spyder'), ('marca', 'Porsche'), ('motor', '4.6')])

OrderedDict([('id', 4), ('piloto', 'Ricardo'), ('modelo', 'Vulcan'), ('marca', 'Aston Martin'), ('motor', '7.0')])

Pressione ENTER para continuar
```

## 9. `get_all()` - Acessar a informação de todos os carros (ordenando com base dos IDs):
```python
>>> get_all()
Iniciando get_all request:
OrderedDict([('id', 0), ('piloto', 'Amaral'), ('modelo', 'Senna'), ('marca', 'McLaren'), ('motor', '4.0')])

OrderedDict([('id', 1), ('piloto', 'Luciano'), ('modelo', '488 Spider'), ('marca', 'Ferrari'), ('motor', '3.9')])

OrderedDict([('id', 2), ('piloto', 'Luis'), ('modelo', 'Urus'), ('marca', 'Lamborghini'), ('motor', '4.0')])

OrderedDict([('id', 3), ('piloto', 'Gustavo'), ('modelo', '918 Spyder'), ('marca', 'Porsche'), ('motor', '4.6')])

OrderedDict([('id', 4), ('piloto', 'Ricardo'), ('modelo', 'Vulcan'), ('marca', 'Aston Martin'), ('motor', '7.0')])

Pressione ENTER para continuar
```
