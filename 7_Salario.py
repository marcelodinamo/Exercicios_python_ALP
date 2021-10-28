sal_b = float(input("Digite seu salario: "))
conta_a = float(input("Digite o valor da conta 01: "))
conta_b = float(input("Digite o valor da conta 02: "))
juro_a = conta_a * 0.02
juro_b = conta_b * 0.02 
sal_r = sal_b - conta_a - conta_b -juro_a -juro_b
print("Salario à receber: {:.2f}".format(sal_r))