# nomeando com as

def execute_command(command: str):
    match command.split():
        case ['ls' | 'exa' as the_command, *paths] as the_list if len(paths) > 1:
            for path in paths:
                print('$ listing ALL directories from', path)
            print(f'{the_command=}=, {the_list=}')

        case ['ls' | 'exa', *paths] if len(paths) <= 1:
            print('$ listing ONE directory from', paths[0])
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')


execute_command('ls /user /main /hut')
execute_command('exa /user')
