#código de olga
#Olga clonó lo que tenia Isaura y de ese código realiza su parte. en el gibhub del lider deben crear su rama

#código de isaura
#menu de opciones

print("Estilos y Belleza")
print("1. ver informacion de la empresa")
print("2. Comprar")
print("3. Agendar cita")
opcion=int(input("digite opcion: "))
#el código de olga empieza desde aquí
if (opcion==2):
    print("Esta registrado? ")
    print("1. si")
    print("2. no")
    op=int(input("digit opcion: "))
    if op==1:
        id=int(input("ingrese su identificacion: "))
        if id==1234:
            print("gracias por su compra")
        else:
            print("usuario invalido, llame para validar información")
    else:
        print("Registrese")

    


