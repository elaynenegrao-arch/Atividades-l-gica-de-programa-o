A= "10"
B= "11"
C= "12"
D= "13"
E= "14"
F= "15"
letra= input("Insira uma letra (A-F): ")
n1= int(input("Insira um número: "))
if letra == "A":
    calculo= 10*1
    calculo2= n1*16
    resultado= calculo + calculo2
    print(f"O resultado é: {resultado}")
elif letra == "B":
    calculo3= 11*1
    calculo4= n1*16
    resultado1= calculo3 + calculo4
    print(f"O resultado é: {resultado1}")
elif letra == "C":
    calculO5= 12*1
    calculo6= n1*16
    resultado2= calculo5 + calculo6
    print(f"O resultado é: {resultado2}")
elif letra == "D":
    calculo7= 13*1
    calculo8= n1*16
    resultado3= calculo7 + calculo8
    print(f"O resultado é: {resultado3}")    
elif letra == "E":
    calculo9= 14*1
    calculo10= n1*16
    resultado4= calculo9 + calculo10
    print(f"O resultado é: {resultado4}")
elif letra == "F":
    calculo11= 15*1
    calculo12= n1*16
    resultado5= calculo11 + calculo12
    print(f"O resultado é: {resultado5}")
else:
    print("Letra inválida. Por favor, insira uma letra de A a F.")