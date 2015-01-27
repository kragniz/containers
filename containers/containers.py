try:
    from urllib import urlretrieve
except ImportError:
    from urllib.request import urlretrieve


def simple_discovery(path, secure=True):
    if secure:
        protocol = 'https'
    else:
        protocol = 'http'

    urlretrieve('{protocol}://{path}.aci'.format(path=path,
                                                 protocol=protocol),
                'image.aci'.format(path=path))
