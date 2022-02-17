from getpass import getpass
from html import make_html
from upload import get_client, update_page
import pandas as pd


def cli(username: str, file_name: str) -> None:
    """
    username: str, full UiO username, including @uio.no
    file_name: str, name of file to parse as menu

    Prompts the user for their password, generates html page from file
    """
    password = getpass(f'Password for {username}: ')
    client = get_client('https://foreninger-dav.uio.no/rf/', username, password)
    data = make_html(pd.read_excel(file_name, header=0))

    update_page(client, 'servering/bar', data)


if __name__ == '__main__':
    import sys
    cli(*sys.argv[1:])
