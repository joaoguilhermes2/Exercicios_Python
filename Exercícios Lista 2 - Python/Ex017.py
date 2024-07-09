''' 17. Seu João precisa fazer um empréstimo automático no aplicativo, o banco aprova a transação de 
acordo com as seguintes condições: Leia o salário de um trabalhador e o valor da prestação de 
um empréstimo. Se a prestação for maior que 20% do salário imprima: Empréstimo não 
concedido, caso contrário imprima: Empréstimo concedido. '''

salario = float(input("Digite o seu salário: R$ "))
valor_prestacao_emprestimo = float(input("Digite o valor da prestação de um empréstimo: "))

limite_prestacao = salario * 0.2

if valor_prestacao_emprestimo > limite_prestacao:
    print("Empréstimo não concedido!")
else:
    print("Empréstimo concedido!")