from collections.abc import Sequence
from getpass import getpass
from upload import update_menu


def cli(args: Sequence[str]) -> None:
    """
    Prompts the user for email address if not supplied,
    takes path argument if present,
    prompts the user for password.
    Passes login, password and optional path to update_menu.
    """
    if len(args) > 0:
        login = args[0]
    else:
        login = input('UiO email address: ')
    
    if len(args) > 1:
        path = args[1]
    else:
        path = None

    password = getpass()

    update_menu(login, password, path)

if __name__ == '__main__':
    import sys
    cli(sys.argv[1:])