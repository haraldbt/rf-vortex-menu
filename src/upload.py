from typing import Optional
from webdav3.client import Client


def get_client(hostname: str, login: str, password: str):
    """
    hostname: str
    login: str, UiO email address
    password: str, password for the UiO account
    """
    options = {
        'webdav_hostname': hostname,
        'webdav_login': login,
        'webdav_password': password
    }

    return Client(options)


def update_page(client: Client, path: str, data: str) -> None:
    # Special characters break if string data isn't encoded
    client.upload_to(data.encode(), remote_path=f'{path}/index.html')