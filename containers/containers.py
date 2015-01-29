try:
    from urllib import urlretrieve
except ImportError:
    from urllib.request import urlretrieve

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

import os


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

    urlretrieve(url, local_file)

    return local_file


class AppContainer(object):
    def __init__(self, path=None):
        self.path = path
