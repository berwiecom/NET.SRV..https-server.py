
#### Script needed to enable SSL

### https://blog.anvileight.com/posts/simple-python-http-server/


# Pisse = Summer Logo new
# openssl req -days 365                     \
#  -newkey rsa:2048                         \
#  -keyout net.srv..python-server..key.pem  \
#  -out    net.srv..python-server..cert.pem \
#  -x509


import BaseHTTPServer, SimpleHTTPServer
import ssl

httpd = BaseHTTPServer.HTTPServer(('localhost', 80), # 4443
        SimpleHTTPServer.SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket,
         keyfile='./net.srv..python-server..key.pem',
        certfile='./net.srv..python-server..cert.pem', server_side=True)

httpd.serve_forever()


## Execute:
# python ./net.srv..python-server.py
