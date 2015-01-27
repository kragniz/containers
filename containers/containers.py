try:
    from urllib import urlretrieve
except ImportError:
    from urllib.request import urlretrieve

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

import os


def simple_discovery(path, var=None, secure=True):
    if secure:
        protocol = 'https'
    else:
        protocol = 'http'

    url = '{protocol}://{path}.aci'.format(path=path, protocol=protocol)

    parsed = urlparse(url)
    _, local_file = os.path.split(parsed.path)

    if var is not None:
        local_file = os.path.join(var, local_file)

    urlretrieve(url, local_file)


class AppContainer(object):
    def __init__(self, path=None):
        self.path = path
