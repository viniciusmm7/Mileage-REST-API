from main import *
data = [{"piloto": "Amaral", "modelo": "Senna", "marca": "McLaren", "motor": "4.0"},
        {"piloto": "Luciano", "modelo": "488 Spider", "marca": "Ferrari", "motor": "3.9"},
        {"piloto": "Luis", "modelo": "Urus", "marca": "Lamborghini", "motor": "4.0"},
        {"piloto": "Gustavo", "modelo": "918 Spyder", "marca": "Porsche", "motor": "4.6"},
        {"piloto": "Bruno", "modelo": "AMG GT", "marca": "Mercedes-benz", "motor": "4.0"}]

# ----- Testes -----
print('======================================================================================')
print('                                        Testes')

for i in data:
    put(data.index(i), i)
    input('Pressione ENTER para continuar\n')

patch(4, {'piloto': 'Vinícius',
          'marca': 'Koenigsegg',
          'modelo': 'Regera',
          'motor': '5.0'})
input('Pressione ENTER para continuar\n')

put_input(5)
input('Pressione ENTER para continuar\n')

patch_input(4)
input('Pressione ENTER para continuar\n')

delete(5)
input('Pressione ENTER para continuar\n')

get(3)
input('Pressione ENTER para continuar\n')

get_by(Carros.piloto)
input('Pressione ENTER para continuar\n')

get_by()
input('Pressione ENTER para continuar\n')

get_all()
input('Pressione ENTER para continuar\n')

print('                                  Testes finalizados')
print('======================================================================================')
# ----- Fim dos testes -----