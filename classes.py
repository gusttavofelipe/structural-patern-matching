from dataclasses import dataclass

@dataclass
class Command:
    command: str
    directories: list[str]


def execute_command(command: Command):
    match command:
        # passar classe "instanciada" (não é literalmente uma instancia, apenas pro match)
        case Command(command='ls', directories=[_, *_]):
            for directory in command.directories:
                print('$ listing ALL directories from', directory)
        case Command(command='cd', directories=[_, *_]):
            for directory in command.directories:
                print('$ changing to', directory)
        case _:  
            print('$ command not implemented')



execute_command(Command('ls', ['/users']))
execute_command(Command('cd', ['/users']))