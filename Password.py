password = input("Ingrese una contraseña: ")
while(1):
    if len(password) < 8:
        password = input("La contraseña debe tener 8 carácteres, ingrese otra: ")
    elif not password.isalnum():
        password = input("La contraseña debe tener carácteres alfanuméricos, ingrese otra: ")
    else:
        print("Contraseña aceptada")
        break
