subtotal=0
print("bienvenido al cine")
usuario=input("ingrese su nombre pára continuar:")
clave=int(input("ingrese clave:"))

publico=int(input("indique el tipo de publico 1.)normal 2.)estudiante 3.)adulto mayor"))
sala=int(input("indique el tipo de sala que desea 1.)normal 2.)3d 3.)4dx"))
entradas=int(input("indique el numero de entradas que desea:"))

if publico==1:
    if sala==1:
        subtotal=entradas*5600
    elif sala==2:
        subtotal=entradas*7800
    elif sala==3:
        subtotal=entradas*12000
    else:
        print("ingrese una opcion valida")

elif publico==2:
    if sala==1:
        subtotal=entradas*3400
    elif sala==2:
        subtotal=entradas*4800
    elif sala==3:
        subtotal=entradas*7000
    else:
        print("ingrese una opcion valida")

elif publico==3:
    if sala==1:
        subtotal=entradas*2500
    elif sala==2:
        subtotal=entradas*3500
    elif sala==3:
        subtotal=entradas*4800
    else:
        print("ingrese una opcion valida")
else:
    print("ingrese una opcion valida")

print(f"el subtotal es de ${subtotal}")
iva=subtotal*0.19
print(f"iva:${iva}")
total=subtotal+iva
print("-"*45)
print(f"el total final:${total}")