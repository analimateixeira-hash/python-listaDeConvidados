#Lista de convidados para a festa 
convidados_da_festa = ['Ana', 'Diego', 'yuliany']

status_presenca = {}

lista_de_chegadas = ['Ana','Diego'] 
convidados_da_festa = ['Maria', 'João','Ana', 'Carlos', 'Mariana']

status_presenca = {}

print('--- Verificação da lista de convidados ---')

lista_de_chegada = ['João', 'Ana', 'Pedro', 'Maria'] 

for pessoa in lista_de_chegada:
    if pessoa in convidados_da_festa:
        print(f'Olá, {pessoa}! Bem-vindo(a) à festa.')
        status_presenca[pessoa] = 'Confirmado'

    else:
        print(f'Desculpe, {pessoa}. Seu nome não está na lista')
        status_presenca[pessoa] = 'Não Convidado'


