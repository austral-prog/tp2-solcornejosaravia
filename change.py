def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(gasto)

    din_recib = 100
    print("Dinero recibido")
    print(din_recib)
    
    vuelto = din_recib - gasto

    print('')
    print("Vuelto")
    print('')
   
    pesos = int(vuelto)
    centavos = round((vuelto - pesos) * 100)

    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)

change() 
