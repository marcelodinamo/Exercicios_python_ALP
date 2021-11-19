
print(50 * "-")
print(14 * "-", "Programa validar CPF", 14 * "-")
print(50 * "-")
cpf,sep,dig = input("Entre com seu CPF: ").partition('-')
cpf = list(cpf)
cpf.reverse()
peso = 2
soma = 0
for i in cpf:
  resultado = int(i) * peso
  peso += 1
  soma = soma + resultado
resto = soma % 11
digito_1 = 11 - resto
if resto == 0:
  digito_1 = 0
peso = 2 
soma = 0 
cpf.insert(0,digito_1)   
for b in cpf:
  resultado = int(b) * peso
  peso += 1
  soma = soma + resultado
resto = soma % 11 
digito_2 = 11 - resto
if resto == 0:
  digito_2 = 0
dig = list(dig)
dig_1 = int(dig[0])
dig_2 = int(dig[1])
if digito_1 == dig_1 and digito_2 == dig_2:
  print('*** CPF Valido ***')
else:
  print('*** CPF Invalido ***')
