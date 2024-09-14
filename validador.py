    #Valida una contraseña según los criterios establecidos.
def validar_contrasena(contrasena):

    # Conjuntos de caracteres para las verificaciones
    mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '0123456789'
    especiales = '!@#$%^&*'

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_especial = False
    
    #True si la contraseña es válida, False en caso contrario.

    if len(contrasena) < 8:
        return False

    for caracter in contrasena:
        if caracter in mayusculas:
            tiene_mayuscula = True
        elif caracter in minusculas:
            tiene_minuscula = True
        elif caracter in numeros:
            tiene_numero = True
        elif caracter in especiales:
            tiene_especial = True

    return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial

# Solicitar contraseña al usuario
contrasena = input("Ingrese su contraseña: ")

# Validar la contraseña
if validar_contrasena(contrasena):
    print("La contraseña es válida.")
else:
    print("La contraseña no es válida. Debe contener al menos 8 caracteres, una mayúscula, una minúscula, un número y un carácter especial.")