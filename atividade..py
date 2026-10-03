n1= float(input("Digite o primeiro número: "))
n2= float(input("Digite o segundo número: "))

quersomar= input("Deseja somar os números? (s/n): ")
if quersomar.lower() == "s":
    soma = n1 + n2
    print("A soma dos números é:", soma)    
quersubtrair= input("Deseja subtrair os números? (s/n): ")
if quersubtrair.lower() == "s":
    subtracao = n1 - n2
    print("A subtração dos números é:", subtracao)
quermultiplicar= input("Deseja multiplicar os números? (s/n): ")
if quermultiplicar.lower() == "s":
    multiplicacao = n1 * n2
    print("A multiplicação dos números é:", multiplicacao)  
querdividir= input("Deseja dividir os números? (s/n): ")
if querdividir.lower() == "s":  
    if n2 != 0:
        divisao = n1 / n2
        print("A divisão dos números é:", divisao)
    else:
        print("Não é possível dividir por zero.")
quermedia= input("Deseja calcular a média dos números? (s/n): ")
if quermedia.lower() == "s":
    media = (n1 + n2) / 2
    print("A média dos números é:", media)
quermaior= input("Deseja saber qual número é maior? (s/n): ")
if quermaior.lower() == "s":    
    if n1 > n2:
        print("O primeiro número é maior.")
    elif n2 > n1:
        print("O segundo número é maior.")
    else:
        print("Os números são iguais.")
querrecomecar= input("Deseja reiniciar o programa? (s/n): ")
if querrecomecar.lower() == "s":
    print("Reiniciando o programa...")
    # Aqui você pode chamar a função principal novamente ou reiniciar o script