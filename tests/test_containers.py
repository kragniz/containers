import unittest

from containers import containers

class TestDiscovery(unittest.TestCase):

    def test_get_etcd(self):
        containers.simple_discovery('localhost:8080/tests/etc/etcd-v2.0.0-linux-amd64', secure=False)


if __name__ == '__main__':
    unittest.main()
