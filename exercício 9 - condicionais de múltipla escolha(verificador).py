nome = input('Qual seu nome?')
idade = int(input('Qual sua idade?'))
if nome == 'Max':
    print('Olá, Max! Atualmente você está com {} anos de idade!'.format(idade))
elif idade < 18:
    print('Você não é o Max! E é menor de idade!')
elif idade > 100:
    print('Diferente de você, o Max não é imortal!')