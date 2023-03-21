
def execute_command(command: str):
    match command.split():
        case ['ls' | 'exa', *paths]: # | == or
            for path in paths:
                print('$ listing files from', path)
        case ['cd'| 'change', path]: # | == or
            print('$ change directory to', path)
        case _: 
            print('$ command not implemented')


execute_command('ls /user /main /hut')
execute_command('exa /user')
execute_command('cd /etc')
execute_command('change /etc')
