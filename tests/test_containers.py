try:
    from http.server import SimpleHTTPRequestHandler
except ImportError:
    from SimpleHTTPServer import SimpleHTTPRequestHandler

try:
    from socketserver import TCPServer
except ImportError:
    from SocketServer import TCPServer

import os
import threading
import unittest

import containers

PORT = 8080

class TestServer(TCPServer):
    allow_reuse_address = True

handler = SimpleHTTPRequestHandler
httpd = TestServer(('', PORT), handler)

httpd_thread = threading.Thread(target=httpd.serve_forever)
httpd_thread.setDaemon(True)
httpd_thread.start()


class TestDiscovery(unittest.TestCase):

    def test_get_etcd(self):
        containers.simple_discovery('localhost:8080/tests/etc/etcd-v2.0.0-linux-amd64', secure=False)


if __name__ == '__main__':
    unittest.main()
