# APENAS UMA VARIAVEL (CAMINHO)

def execute_command(command: str):
    match command.split(): # executando funcao no match
        case ['ls', path]: # qualquer outro segundo valor é atribuido a path
            print('$ listing files from', path)
        case ['cd', path]:
            print('$ change directory to', path)
        case _: 
            print('$ command not implemented')


execute_command('ls ubt')
execute_command('cd /users')
#----------------------------------------------------------------------------------------------------------------

# CAMINHO E ARGUMENTO (em 'ls')

# pode-se definir quantas variaveis dinamicas necessarias
def execute_command(command: str):
    match command.split():
        case ['ls', path, arg]: 
            print('$ listing files from', path, arg)
        case ['cd', path]:
            print('$ change directory to', path)
        case _: 
            print('$ command not implemented')


execute_command('ls /ubt --force')
execute_command('cd /users')
#----------------------------------------------------------------------------------------------------------------

# MUITOS DIRETORIOS (em 'ls')

def execute_command(command: str):
    match command.split():
        case ['ls', *paths]: # empacotando valores
            for path in paths:
                print('$ listing files from', path)
        case ['cd', path]:
            print('$ change directory to', path)
        case _: 
            print('$ command not implemented')


execute_command('ls /user /main /hut')
execute_command('cd etc')
#----------------------------------------------------------------------------------------------------------------
