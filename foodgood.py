subtotal=0
cantidad=0
canbebida=0
print("bienvenidos a food good ")
nombre=input("ingrese su nombre:")

print("combos:")
print("1.)big gloton         normal:$6500 xl:$8900")
print("2.)tocomples full     normal$3000 xl:$4500")
print("3.)fajitas taliban    normal:$2400 xl:$3200")
print("4.)papas us love      normal:$1450  XL:$2400")
combo=int(input("selccione el combo a comprar (1-4):"))
tamaño=int(input("seleccione el tamaño del combo que desea 1.)normal 2.)xl:"))
cantidad=int(input(f"escriba la cantidad que desea:"))

if combo==1:
    if tamaño==1:
        subtotal=cantidad*6500
    elif tamaño==2:
        subtotal=cantidad*8900
    else:
        print("seleccione una opcion valida")

elif combo==2:
    if tamaño==1:
        subtotal=cantidad*3000
    elif tamaño==2:
        subtotal=cantidad*4500
    else:
        print("seleccione una opcion valida")

elif combo==3:
    if tamaño==1:
        subtotal=cantidad*2400
    elif tamaño==2:
        subtotal=cantidad*3200
    else:
        print("seleccione una opcion valida")

elif combo==4:
    if tamaño==1:
        subtotal=cantidad*1450
    elif tamaño==2:
        subtotal=cantidad*2400
    else:
        print("seleccione una opcion valida")
else:
    print("seleccione una opcion valida (1-4)")

bebida=input("desea agregar bebida (s/n)")
if bebida=="s":
    tamañobebida=int(input("seleccion el tamaño de la bebida 1.)normal:1200 2.)grande:$2300 3.)xl:$3200 :"))
    canbebida=int(input("ingrese la cantidad de bebidas que desea:"))
    if tamañobebida==1:
        subtotal+=canbebida*1200
    elif tamañobebida==2:
        subtotal+=canbebida*2300
    elif tamañobebida==3:
        subtotal+=canbebida*3200
    else:
        print("seleccione un opcion de tamaño de bebida valida")
    
    cantidadf=cantidad+canbebida
    print(f"la cantidad de productos:{cantidadf}")
    print(f"el subtotal de la compra es de:${subtotal}")
    iva=subtotal*0.19
    print(f"iva:${iva: .0f}")
    total=subtotal+iva
    print("-"*45)
    print(f"el total final de la compra es de:{total}")
else:
    print(f"la cantidad de productos:{cantidad}")
    print(f"el subtotal de la compra es de:${subtotal}")
    iva=subtotal*0.19
    print(f"iva:${iva: .0f}")
    total=subtotal+iva
    print("-"*45)
    print(f"el total final de la compra es de:{total}")
