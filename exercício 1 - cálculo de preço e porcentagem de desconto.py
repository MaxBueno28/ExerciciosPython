preco = float(input('Digite o preço do produto:'))
p = float(input('Digite o percentual de desconto (0-100)%:'))

desconto = preco * (p / 100)
final = preco - desconto

print('O preço do produto é: {}. Desconto de {}%.'.format(preco,p))
print('O valor calculado do desconto foi de: {}. reais. O valor final foi de: {}. reais'.format(desconto, final))