sal_b = float(input("Digite seu salario: "))
com = sal_b * 0.05
imp = sal_b * 0.07
sal_r = com + sal_b - imp
print("Salario à receber: {:.2f}".format(sal_r))