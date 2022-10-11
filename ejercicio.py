#TALLER 6 PYTHON
# AUTORA: Isaura Suarez
# FECHA:

from datetime import date
hoy=date.today()
print("Hoy es el día: ",hoy)
print()
print("TALLER 6 CICLOS ITERATIVOS CON LA SENTENCIA WHILE")
print()
num1=int(input("Digite un numero: "))
print(" ****Ciclo  controlado por contador")
i=1
while i<num1:
    print(i)
    i+=1
print("Fin del ciclo")
print()
print(" ***Ciclo controlado por evento")
i=1
numero1=5
numero2=int(input("Digite un numero de 1 a 10: "))
while numero2 !=numero1:
    i+=1
    numero2=int(input("Digite un numero de 1 a 10: "))
print("Acertaste en el intento Nro.",i)
print("Fin del ciclo")
print()
print("***Ciclo abortado con la sentencia Break")
amistad=input("Digite el nombre de una amistad: ")
amistad=amistad.upper()
for character in amistad:
    print(character)
    if character=="A":
       break
print("Fin del ciclo")
print()                       
print("FIN")         