from getpass import getpass
from typing import Optional
from webdav3.client import Client
from collections.abc import Sequence
import sys


def update_menu(login: str, password: str, path: Optional[str] = None) -> None:
    """
    login: str, UiO email address
    password: str, password for the UiO account
    path: optional str, path to file to be uploaded
    """
    options = {
        'webdav_hostname': 'https://foreninger-dav.uio.no/rf/',
        'webdav_login': login,
        'webdav_password': password
    }

    client = Client(options)

    if path is None:
        path = 'index.html'

    client.upload_sync(remote_path='meny/index.html', local_path=path)


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
    cli(sys.argv[1:])
