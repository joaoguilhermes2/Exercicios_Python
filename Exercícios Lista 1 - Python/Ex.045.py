''' 45. Uma fábrica de camisetas produz  os  tamanhos  pequeno,  médio  e  grande,  cada  uma  sendo  
vendida respectivamente por 35, 45 e 55 reais. Construa um algoritmo em que o usuário forneça 
a quantidade de camisetas  pequenas,  médias  e  grandes  referentes  a  uma  venda,  e  a  máquina  
informe quanto será o valor arrecadado. ''' 

quant_cam_peq = int(input("Digite a quantidade de camisas pequenas que você deseja: "))
quant_cam_med = int(input("Digite a quantidade de camisas médias que você deseja: "))
quant_cam_grande = int(input("Digite a quantidade de camisas grandes que você deseja: "))

valor_cam_peq = 35
valor_cam_med = 45
valor_cam_grande = 55

camisa_peq =  quant_cam_peq * valor_cam_peq
camisa_med = quant_cam_med * valor_cam_med
camisa_grande = quant_cam_grande * valor_cam_grande

valor_total = camisa_peq + camisa_med + camisa_grande

print(f"O valor total das camisetas pequenas é de R$ {camisa_peq}")
print(f"O valor total das camisetas médias é de R$ {camisa_med}")
print(f"O valor total das camisetas grandes é de R$ {camisa_grande}")
print(f"O valor total das camisetas é de R$ {valor_total}")