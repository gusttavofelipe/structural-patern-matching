# case com dicionarios

def execute_command(command: dict):
    match command:
        case {'command': 'ls', 'directories': [_, *_]}:
            print('MATCH')
            for directory in command['directories']:
                print('$ listing ALL directories from', directory)
        case _: 
            print('$ command not implemented')

# deve-se passaro dicionario inteiro como argumento
execute_command({'command': 'ls', 'directories': ['/git', '/pie']})