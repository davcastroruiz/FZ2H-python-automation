def operacion_aritmetica(operator, primer_valor, segundo_valor):
    # operator 1 suma, 2 resta, 3 multiplicacion, 4 division
    operations = [1,2,3,4]
    assert operator in operations
    if operator == 1:
        return primer_valor + segundo_valor
    if operator == 2:
        return primer_valor - segundo_valor
    if operator == 3:
        return primer_valor * segundo_valor
    if operator == 4:
        return primer_valor / segundo_valor

WELCOME_MSG = '''Hola! Soy tu calculadora\nIngresa el NUMERO de operacion a realizar:\n1) suma\n2) resta\n3) multiplicacion\n4) division\n\n'''

while True:
    user_input_operator = int(input(WELCOME_MSG))
    user_input_primer_valor = int(input('ingresar primer valor\n'))
    user_input_segundo_valor = int(input('ingresar segundo valor\n'))
    result = operacion_aritmetica(user_input_operator, user_input_primer_valor, user_input_segundo_valor)
    print(result)
    if input('deseas continuar? n/y\n') == 'n':
        break