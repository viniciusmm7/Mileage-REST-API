from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Mileage.db'
db  = SQLAlchemy(app)
BASE = 'http://127.0.0.1:5000/carros/'

class Carros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    piloto = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    marca = db.Column(db.String(20), nullable=False)
    motor = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Car(piloto = {piloto}, modelo = {modelo}, marca = {marca}, motor = {motor})"

car_put_args = reqparse.RequestParser()
car_put_args.add_argument("piloto", type=str, help="O nome do piloto é obrigatório (string)", required=True)
car_put_args.add_argument("modelo", type=str, help="O modelo do carro é obrigatório (string)", required=True)
car_put_args.add_argument("marca", type=str, help="A marca do carro é obrigatória (string)", required=True)
car_put_args.add_argument("motor", type=str, help="O motor é obrigatório (float)", required=True)

car_update_args = reqparse.RequestParser()
car_update_args.add_argument("piloto", type=str, help="O nome do piloto deve ser do tipo String")
car_update_args.add_argument("modelo", type=str, help="O modelo do carro deve ser do tipo String")
car_update_args.add_argument("marca", type=str, help="A marca do carro deve ser do tipo String")
car_update_args.add_argument("motor", type=str, help="O motor do carro deve ser do tipo String")

resource_fields = {
    'id': fields.Integer,
    'piloto': fields.String,
    'modelo': fields.String,
    'marca': fields.String,
    'motor': fields.String
}

db.create_all()

class Car(Resource):
    @marshal_with(resource_fields)
    def order_by(self, column=Carros.motor):
        result = Carros.query.order_by(column).all()
        if not result:
            abort(404, message=f"Não foi possível ordenar pela coluna {column} pois ela não existe")
        return result
    
    @marshal_with(resource_fields)
    def get(self, id_carro:int):
        return Carros.query.get_or_404(id_carro)

    @marshal_with(resource_fields)
    def put(self, id_carro):
        args = car_put_args.parse_args()
        result = Carros.query.filter_by(id=id_carro).first()
        if result:
            abort(409, message="Conflito com o servidor, o id ja esta preenchido")

        carro = Carros(id=id_carro, piloto=args['piloto'], modelo=args['modelo'], marca=args['marca'], motor=args['motor'])
        db.session.add(carro)
        db.session.commit()
        return carro

    @marshal_with(resource_fields)
    def patch(self, id_carro):
        args = car_update_args.parse_args()
        result = Carros.query.filter_by(id=id_carro).first()
        if not result:
            abort(404, message="O carro não existe, não é possível atualizar")
        
        if args["piloto"]:
            result.piloto = args["piloto"]
        if args["modelo"]:
            result.modelo = args["modelo"]
        if args["marca"]:
            result.marca = args["marca"]
        if args["motor"]:
            result.motor = args["motor"]
        
        db.session.commit()

        return result

    @marshal_with(resource_fields)
    def delete(self, id_carro):
        db.session.delete(Carros.query.get_or_404(id_carro))
        db.session.commit()

def _verifica_vazio(valor):
    while not valor:
        print('O valor não pode estar vazio')
        valor = input('Tente novamente: ')
    return valor

def get(id:int):
    print('\nIniciando get request:', end='\n')
    response = requests.get(BASE + str(id))
    print(response.json())

def get_by(column=Carros.motor):
    print('\nIniciando get_by request:', end='\n')
    response = Car.order_by(Car, column)
    for i in response:
        print(i, end='\n\n')

def get_all():
    print('\nIniciando get_all request:', end='\n')
    response = Car.order_by(Car, Carros.id)
    for i in response:
        print(i, end='\n\n')

def put(id:int, dados:dict):
    print(f'\nIniciando put request no id {id}:', end='\n')
    response = requests.put(BASE + str(id), dados)
    print(response.json())

def put_input(id:int):
    print(f'\nIniciando put_input request no id {id}:', end='\n')
    dados = {}

    piloto = input('Nome do piloto: ')
    piloto = _verifica_vazio(piloto)

    marca = input('Marca do carro: ')
    marca = _verifica_vazio(marca)

    modelo = input('Modelo do carro: ')
    modelo = _verifica_vazio(modelo)

    motor = input('Motor do carro (exemplo: 1.0 turbo): ')
    motor = _verifica_vazio(motor)

    dados['piloto'] = piloto
    dados['modelo'] = modelo
    dados['marca'] = marca
    dados['motor'] = motor

    response = requests.put(BASE + str(id), dados)
    print(response.json())

def patch(id:int, dados:dict):
    print(f'\nIniciando patch request no id {id}:', end='\n')
    response = requests.patch(BASE + str(id), dados)
    print(response.json())

def patch_input(id:int):
    print(f'\nIniciando patch_input request no id {id}:', end='\n')
    dados = {}

    piloto = input('Nome do piloto: ')
    marca = input('Marca do carro: ')
    modelo = input('Modelo do carro: ')
    motor = input('Motor do carro (exemplo: 1.0 turbo): ')

    while not piloto and not marca and not modelo and not motor:
        print('\nOs dados não podem estar todos vazios, tente novamente')
        piloto = input('Nome do piloto: ')
        marca = input('Marca do carro: ')
        modelo = input('Modelo do carro: ')
        motor = input('Motor do carro (exemplo: 1.0 turbo): ')

    dados['piloto'] = piloto
    dados['modelo'] = modelo
    dados['marca'] = marca
    dados['motor'] = motor

    response = requests.patch(BASE + str(id), dados)
    print(response.json())

def delete(id:int):
    print(f'\nIniciando delete request no id {id}:', end='\n')
    response = requests.delete(BASE + str(id))
    print(f'Deletando o carro de id {str(id)}' + '\n' + response.text)
    response = requests.get(BASE + str(id))
    if response == False:
        print(response.text)
        pass
    elif response == True:
        print(f'Carro {str(id)} deletado com sucesso')

api.add_resource(Car, "/carros/<int:id_carro>")

if __name__ == '__main__':
    app.run(debug=True)