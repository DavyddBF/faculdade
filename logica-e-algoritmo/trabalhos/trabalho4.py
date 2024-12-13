print('Bem vindos a lista de contatos de Davyd Ferreira')

listaContatos = []
idGlobal = 5053298

def cadastrarContato(id):
    print(50 * '-')
    print(13 * '-', 'MENU CADASTRAR CONTATO', 13 * '-')
    print(f'Id do Contato: {id}')

    nome = input('Por favor entre com o nome do Contato: ')
    atividade = input('Por favor entre com a Atividade do contato: ')
    telefone = input('Por favor entre com o telefone do contato: ')

    contato = {
        'id': id, 
        'nome': nome, 
        'atividade': atividade, 
        'telefone': telefone
    }
    listaContatos.append(contato.copy())

def consultarContatos():
    while(True):
        print(50 * '-')
        print(13 * '-', 'MENU CONSULTAR CONTATOS', 12 * '-')
        print('1 - Consultar Todos os Contatos')
        print('2 - Consultar Contato por Id')
        print('3 - Consultar Contato(s) por Atividade')
        print('4 - Retornar')

        opcaoConsulta = int(input('>> '))

        if(opcaoConsulta == 1):
            print(50 * '-')
            print('')
            
            for(contato) in listaContatos:
                print(f'id: {contato['id']}')
                print(f'nome: {contato['nome']}')
                print(f'atividade: {contato['atividade']}')
                print(f'telefone: {contato['telefone']}')
                print('')
                
            print(50 * '-')
        elif(opcaoConsulta == 2):
            idConsulta = int(input('Digite o id do contato: '))

            print(50 * '-')
            print('')

            for(contato) in listaContatos:
                if(contato['id'] == idConsulta):
                    print(f'id: {contato['id']}')
                    print(f'nome: {contato['nome']}')
                    print(f'atividade: {contato['atividade']}')
                    print(f'telefone: {contato['telefone']}')
                    print('')
                    break
            else:
                print('Contato não encontrado.')

            print(50 * '-')
        elif(opcaoConsulta == 3):
            atividadeConsulta = input('Digite a Atividade do(s) Contato(s): ')

            print(50 * '-')
            print('')

            for(contato) in listaContatos:
                if(contato['atividade'] == atividadeConsulta):
                    print(f'id: {contato['id']}')
                    print(f'nome: {contato['nome']}')
                    print(f'atividade: {contato['atividade']}')
                    print(f'telefone: {contato['telefone']}')
                    print('')

            print(50 * '-')
        elif(opcaoConsulta == 4):
            return
        else:
            print('Opção inválida. Tente novamente.')

def removerContato():
    while(True):
        print(50 * '-')
        print(14 * '-', 'MENU REMOVER CONTATO', 14 * '-')

        idRemover = int(input('Digite o id do contato a ser removido: '))

        for(contato) in listaContatos:
            if(contato['id'] == idRemover):
                listaContatos.remove(contato)
                print('Contato removido com sucesso!')
                return
        else:
            print('Id inválido. Tente novamente.')

while(True):
    print(50 * '-')
    print(17 * '-', 'MENU PRINCIPAL', 17 * '-')
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Contato')
    print('2 - Consultar Contato(s)')
    print('3 - Remover Contato')
    print('4 - Sair')

    opcaoMenu = int(input('>> '))

    if(opcaoMenu == 1):
        idGlobal += 1
        cadastrarContato(idGlobal)
    elif(opcaoMenu == 2):
        consultarContatos()
    elif(opcaoMenu == 3):
        removerContato()
    elif(opcaoMenu == 4):
        break
    else:
        print('Opção inválida. Tente novamente.')
