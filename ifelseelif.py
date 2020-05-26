user = dict(
    email='hola@epydemia.dev',
    password='123456789'
)
categories = [
    {'rock': ['parecemos tontos - Bunbury', 'bohemian rapsody - Queen']},
    {'pop': ['Azul - Cristian castro', 'playa - Luis Miguel']},
    {'salsa': ['muy muy - chichiperalta', 'christian - Los salseros']},
    {'metal': ['blood brothers - Iron Maiden', 'Jump - Van Halen']},
]
print('Hola que tal ingresa tu correo electronico:\n')
email = input()
password = input('Ingresa tambien tu contraseña:\n')

if user.get('email') == email and user.get('password') == password:
    print(f'Bienvenido {user.get("email")}')
    categoria = input('Escoge la categoria que te gustaria escuchar\n')
    canciones = None
    if categoria == 'rock':
        diccionario = categories[0]
        canciones = diccionario.get('rock')
    elif categoria == 'pop':
        canciones = categories[1].get('pop')
    elif categoria == 'salsa':
        canciones = categories[2].get('salsa')
    elif categoria == 'metal':
        canciones = categories[3].get('metal')
    else:
        print('Esa categoria no existe')
    if canciones:
        print(canciones)
else:
    print('Ups este correo o contraseña no existe')
