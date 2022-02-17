from typing import Optional
from webdav3.client import Client


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