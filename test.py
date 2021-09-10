from main import *
data = [{"piloto": "Amaral", "modelo": "Senna", "marca": "McLaren", "motor": 4.0},
        {"piloto": "Luciano", "modelo": "488 Spider", "marca": "Ferrari", "motor": 3.9},
        {"piloto": "Luis", "modelo": "Urus", "marca": "Lamborghini", "motor": 4.0},
        {"piloto": "Gustavo", "modelo": "918 Spyder", "marca": "Porsche", "motor": 4.6},
        {"piloto": "Lister", "modelo": "AMG GT", "marca": "Mercedes-benz", "motor": 4.0}]

# ----- Testes -----
print('======================================================================================')
print('                                        Testes')

for i in data:
    put(data.index(i), i)

patch_input(4)

patch(4, {'piloto': 'Vinícius',
          'marca': 'McLaren',
          'modelo': 'Speedtail',
          'motor': 4.0})

put_input(5)

delete(5)

get(3)

get_by(Carros.piloto)

get_by()

get_all()

print('                                  Testes finalizados')
print('======================================================================================')
# ----- Fim dos testes -----