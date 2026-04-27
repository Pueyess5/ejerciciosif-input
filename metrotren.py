print("bienvenidos a metro tren")
usuario=int(input("sleccione el tipo de ususario: 1.)estudiante 2.)adulto 3.)adulto mayor "))
horario=int(input("seleccione el horerio del vaije: 1.)normal 2.)punta"))

if usuario==1:
    if horario==1:
        print("la tarifa es de $490")
    else:
        print("la tarifa es de $590")


elif usuario==2:
    if horario==1:
        print("la tarifa es de $790")
    else:
        print("la tarifa es de $890")


elif usuario==3:
    if horario==1:
        print("la tarifa es de $390")
    else:
        print("la tarifa es de $490")

else:
    print("seleccione un aopcion valida para continuar")
print("gracias por preferirnos")