# estrutura if, elif, else normal 

# def execute_command(command: str):
#     if command == 'ls':
#         print('$ listing files')
#     elif command == 'cd':
#         print('$ change directory')
#     else:
#         print('$ command not implemented')

# execute_command('cd')


# structural pattern matching

def execute_command(command: str):
    match command:
        case 'ls':
            print('$ listing files')
        case 'cd':
            print('$ change directory')
        case _: # valor padrão (se nenhuma das opcoes)
            print('$ command not implemented')
