def definir_se_e_par(numero): #ENTRADA
#     #PROCESSAMENTO
     resultado = ""
     if numero % 2 == 0:
         resultado = "Par"
     else:
         resultado = "Impar"
    
#     #SAÍDA
     return resultado

print(definir_se_e_par(5))

##Fazer uma função que recebe 2 numeros e retorna a soma deles
def soma(numero1, numero2):
      resultado = numero1 + numero2
      return resultado

n1 = int(input("Digite o numero 1: "))
n2 = int(input("Digite o numero 2: "))

print(soma(n1, n2))

# #Fazer uma função que recebe 2 numeros e retorna a diferença deles
def diferença(numero1, numero2):
  resultado = numero1 - numero2
  return resultado

n1 = int(input("Digite o numero 1: "))
n2 = int(input("Digite o numero 2: "))

print(diferença(n1, n2))


