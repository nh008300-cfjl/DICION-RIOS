from time import sleep


def maior(lista_pessoas):
    cont = maior_valor = 0
    nome_maior = ''

    print('-=' * 30)
    print('Analisando os valores passados...')

    for pessoa in lista_pessoas:
        print(f"{pessoa['nome']} ({pessoa['idade']} anos) ", end='', flush=True)
        sleep(0.3)

        if cont == 0:
            maior_valor = pessoa['idade']
            nome_maior = pessoa['nome']
        else:
            if pessoa['idade'] > maior_valor:
                maior_valor = pessoa['idade']
                nome_maior = pessoa['nome']
        cont += 1

    print(f'\nForam informadas {cont} pessoas ao todo.')
    print(f'A pessoa com maior idade é {nome_maior} com {maior_valor} anos.')


# Programa principal
grupo = []

while True:
    pessoa = {}
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

# Chamada da função passando a lista de dicionários
maior(grupo)
