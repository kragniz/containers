try:
    from http.server import SimpleHTTPRequestHandler
except ImportError:
    from SimpleHTTPServer import SimpleHTTPRequestHandler

try:
    from socketserver import TCPServer
except ImportError:
    from SocketServer import TCPServer

import glob
import os
import sys
import threading
import unittest

import containers


PY3 = sys.version_info[0] == 3

if PY3:
    string_types = str,
else:
    string_types = basestring,

PORT = 8080


class TestServer(TCPServer):
    allow_reuse_address = True

handler = SimpleHTTPRequestHandler
httpd = TestServer(('', PORT), handler)

httpd_thread = threading.Thread(target=httpd.serve_forever)
httpd_thread.setDaemon(True)
httpd_thread.start()


class TestDiscovery(unittest.TestCase):

    def tearDown(self):
        filelist = glob.glob('/tmp/*.aci')
        for f in filelist:
            os.remove(f)

    def test_get_returns_string(self):
        c = containers.simple_discovery(
            'localhost:8080/tests/etc/etcd-v2.0.0-linux-amd64',
            var='/tmp', secure=False)

        self.assertTrue(isinstance(c, string_types))

    def test_get_etcd(self):
        c = containers.simple_discovery(
            'localhost:8080/tests/etc/etcd-v2.0.0-linux-amd64',
            var='/tmp', secure=False)

        self.assertTrue(os.path.isfile(os.path.join('/tmp', c)))


if __name__ == '__main__':
    unittest.main()
