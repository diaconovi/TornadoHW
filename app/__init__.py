import json
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application
from views import InfoView

define('port', default=8888, help='port to listen on')


def main():
    """Construct and serve the tornado application."""

    define('myvar', default='testvar', help='port to listen on')
    define('testInit', default=111, help='port to listen on')

    config = setConfig()

    app = Application([
        ('/', InfoView)
    ])
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print('Listening on http://localhost:%i' % options.port)
    print(options.myvar)
    print(options.testInit)
    print(config["testOP"])
    IOLoop.current().start()

def setConfig():
    with open('config/config.json.txt') as json_file:
        config = json.load(json_file)

    print(config["testOP"])
    print(config["tetsList"][1])
    print(config["tetsList"][2])

    define('testvar', default='testy', help='port to listen on')

    return config
