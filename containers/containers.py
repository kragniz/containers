try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

import os

import requests


def save_url(url, filename):
    r = requests.get(url, stream=True)
    if r.status_code == requests.codes.ok:
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
    else:
        raise IOError('HTTP GET on {url} failed with error '
                      '{code}.'.format(url=url, code=r.status_code))


def simple_discovery(name, var=None, secure=True):
    '''Perform simple discovery and save the discovered ACI locally.

    :param name: Name of app.
    :type name: str.
    :param var: Directory to save app to.
    :type var: str.
    :param secure: Choose to use HTTPS or HTTP.
    :type secure: bool.
    :returns:  str -- the name of the ACI.
    '''
    if secure:
        protocol = 'https'
    else:
        protocol = 'http'

    url = '{protocol}://{name}.aci'.format(name=name, protocol=protocol)

    parsed = urlparse(url)
    _, local_file = os.path.split(parsed.path)

    if var is not None:
        local_file = os.path.join(var, local_file)

    save_url(url, local_file)

    return local_file


class AppContainer(object):
    def __init__(self, path=None):
        self.path = path
