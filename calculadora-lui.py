from PIL import Image
import sympy as sy

print("Bem vindo(a) à calculadora de propriedades dos gases, por favor escolha uma equação:")
print("")
print(" 01 - Equação dos Gases ideais")
print(" 02 - Equação de Van der Walls")
print(" 03 - Equação de Redlich-Kwong")
print(" 04 - Modificação de Soave de Redlich-Kwong")

equacao = int(input("Insira o número da equação desejada:"))
R = 8.314 #jmol/K

if equacao >= 1:
    print("Você gostaria de uma tabela das propriedades termofísicas?")
    print("01 - Sim")
    print("00 - Não")
    resposta = int(input(""))
    if resposta == 1 :
        img = Image.open('tabelaptf.png')
        img.show()
    else:
        print("Ok then")

print("")
if equacao == 1:
    print("Equação dos Gases ideais:")
    print("Insira a variável de interesse:")
    print ("01 - Pressão")
    print ("02 - Volume")
    print ("03 - Temperatura")
    variavel = int(input(""))
    if variavel == 1:
        print ("Insira os dados de volume e temperatura e mol:")
        v = int(input(""))
        t = int(input(""))
        n = int(input(""))
        p = n*R*t/v
        print ("O valor da pressão é", p, "em Pascal")
        
    if variavel == 2:
        print ("Insira os dados de pressão, temperatura e mol:")
        p = int(input(""))
        t = int(input(""))
        n = int(input(""))
        v = n*R*t/p
        print ("O valor do volume é", v, "em metros cúbicos")
        
    if variavel == 3:
        print ("Insira os dados de volume e pressão e mol:")
        v = int(input(""))
        p = int(input(""))
        n = int(input(""))
        t = (p*v)/n*R
        print ("O valor da temperatura é", t, "em Kelvin")
    
    
        
if equacao == 2:
    print("Equação de Van der Walls")
    print("Insira a variável de interesse:")
    print ("01 - Pressão")
    print ("02 - Volume molar")
    print ("03 - Temperatura")
    variavel = int(input(""))
    
    if variavel == 1:
        print("Insira dos dados de volume molar, temperatura e os dados de temperatura e pressão críticas:")
        vm = int(input(""))
        t = int(input(""))
        tc = int(input(""))
        pc = int(input(""))
         
        a = (27*(R*tc)**2)/64*pc 
        b = (R*tc)/(8*pc)
        
        p = sy.Symbol('p')
        eqvdv = sy.Eq((p + a/(vm**2))*(vm-b) - R*t)
        solvdv = sy.solve(eqvdv,p)
        print("O valor da pressão é:",solvdv,"em Pascal")

    if variavel == 2:
        print("Insira os dados de pressão, temperatura e os dados de temperatura e pressão críticas:")
        
        p = int(input(""))
        t = int(input(""))
        tc = int(input(""))
        pc = int(input(""))
         
        a = (27*(R*tc)**2)/64*pc 
        b = (R*tc)/(8*pc)
        
        vm = sy.Symbol('vm')
        eqvdv = sy.Eq((p + a/(vm**2))*(vm-b) - R*t)
        solvdv = sy.solve(eqvdv,vm)
        print("O valor do volume molar é:",solvdv,"em metros cúbicos")
        
        
    if variavel == 3:
        print("Insira os dados de volume molar, pressão e os dados de temperatura e pressão críticas:")
        
        vm = int(input(""))
        p = int(input(""))
        tc = int(input(""))
        pc = int(input(""))
         
        a = (27*(R*tc)**2)/64*pc 
        b = (R*tc)/(8*pc)
        
        t = sy.Symbol('t')
        eqvdv = sy.Eq((p + a/(vm**2))*(vm-b) - R*t)
        solvdv = sy.solve(eqvdv,t)
        print("O valor da temperatura é:",solvdv,"em Kelvin")
        
if equacao == 3:
    print("Equação de Redlich-Kwong")
    print("Insira a variável de interesse:")
    print ("01 - Pressão")
    print ("02 - Volume")
    print ("03 - Temperatura")
    variavel = int(input(""))
    
    if variavel == 1 :
        print("Insira dos dados de volume molar, temperatura e os dados de temperatura e pressão críticas:")
        vm = int(input(""))
        t = int(input(""))
        tc = int(input(""))
        pc = int(input(""))       
    
        a = (0.42784*(R**2)*(tc**2.5))/pc
        b = (0.08662*R*tc)/pc
        
        p = sy.Symbol('p')
        eqrk = sy.Eq((R*t)/(vm-b) - a/(t**(1/2)*vm*(vm+b))-p)
        solvrk = sy.solve(eqrk,p)
        print("O valor da pressão é:", solvrk, "em Pascal")
        
        
    if variavel == 2:
        print("Insira os dados de pressão, temperatura e os dados de temperatura e pressão críticas:")
        
        p = int(input(""))
        t = int(input(""))
        tc = int(input(""))
        pc = int(input(""))
         
        a = (0.42784*(R**2)*(tc**2.5))/pc
        b = (0.08662*R*tc)/pc
        
        vm = sy.Symbol('vm')
        eqrk = sy.Eq((R*t)/(vm-b) - a/(t**(1/2)*vm*(vm+b))-p)
        solvrk = sy.solve(eqrk,vm)
        print("O valor do volume molar é:",solvrk,"em metros cúbicos")
        
    if variavel == 3:
        print("Insira os dados de volume molar, pressão e os dados de temperatura e pressão críticas:")
        
        vm = int(input(""))
        p = int(input(""))
        tc = int(input(""))
        pc = int(input(""))
         
        a = (0.42784*(R**2)*(tc**2.5))/pc
        b = (0.08662*R*tc)/pc
        
        t = sy.Symbol('t')
        eqrk = sy.Eq((R*t)/(vm-b) - a/(t**(1/2)*vm*(vm+b))-p)
        solvrk = sy.solve(eqrk,t)
        print("O valor da temperatura é:",solvrk,"em Kelvin")
        
if equacao == 4:
    print("Equação de Redlich-Kwong Modificada:")
    print("Insira a variável de interesse:")
    print ("01 - Pressão")
    print ("02 - Volume")
    print ("03 - Temperatura")
    variavel = int(input(""))
        
    if variavel == 1 :
        print("Insira dos dados de volume molar, temperatura, os dados de temperatura e pressão críticas e o fator acêntrico:")
        vm = int(input(""))
        t = int(input(""))
        tc = int(input(""))
        pc = int(input(""))
        w =  int(input(""))
    
        a = (0.42747*(R**2)*(tc**2))/pc
        b = (0.08664*R*tc)/pc
        tr = t/tc
        L = (1+(0.48508+1.55171*w-0.17613*(w**2))*(1-(tr**0.5))**2)
        
        p = sy.Symbol('p')
        eqs = sy.Eq((R*t)/(vm-b) - a*L/(vm*(vm+b))-p)
        solvs = sy.solve(eqs,p)
        print("O valor da pressão é:", solvs, "em Pascal")
        
        
    if variavel == 2:
        print("Insira os dados de pressão, temperatura, os dados de temperatura e pressão críticas e o fator acêntrico:")
        
        p = int(input(""))
        t = int(input(""))
        tc = int(input(""))
        pc = int(input(""))
        w =  int(input(""))
         
        a = (0.42747*(R**2)*(tc**2))/pc
        b = (0.08664*R*tc)/pc
        tr = t/tc
        L = (1+(0.48508+1.55171*w-0.17613*(w**2))*(1-(tr**0.5))**2)
        
        vm = sy.Symbol('vm')
        eqs = sy.Eq((R*t)/(vm-b) - a*L/(vm*(vm+b))-p)
        solvs = sy.solve(eqs,vm)
        print("O valor do volume molar é:",solvs,"em metros cúbicos")
        
    if variavel == 3:
        print("Insira os dados de volume molar, pressão, os dados de temperatura e pressão críticas e o fator acêntrico:")
        
        vm = int(input(""))
        p = int(input(""))
        tc = int(input(""))
        pc = int(input(""))
        w =  int(input(""))
         
        a = (0.42747*(R**2)*(tc**2))/pc
        b = (0.08664*R*tc)/pc
        tr = t/tc
        L = (1+(0.48508+1.55171*w-0.17613*(w**2))*(1-(tr**0.5))**2)
        
        
        t = sy.Symbol('t')
        eqs = sy.Eq((R*t)/(vm-b) - a*L/(vm*(vm+b))-p)
        solvs = sy.solve(eqrk,t)
        print("O valor da temperatura é:",solvs,"em Kelvin") 
        
print("")
print("")
print("")
print("")

print ("Obrigado por usar a calculadora Dickson, espero que tenha sido útil")
        
        
        
        
        
        
