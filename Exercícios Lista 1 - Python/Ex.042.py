''' 42. Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a 
escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo. ''' 

degrau = float(input("Digite a altura do degrau da escada:"))
altura_desejada = float(input("Digite a altura que você deseja subir na escada: "))

subida = altura_desejada / degrau

print(f"Você deve subir {subida} degraus para chegar no seu destino.")