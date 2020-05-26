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
    print(f'Bienvenido {user.get("email")}\n')
    categoria = 0
    while categoria not in ['', '1']:
        categoria = input('Escoge la categoria que te gustaria escuchar\n')
        if categoria not in ['', '1']:
            for category in categories:
                canciones = category.get(categoria)
                if canciones:
                    print(canciones)
                    break
                else:
                    print('No existe esa categoria')
else:
    print('Ups este correo o contraseña no existe')