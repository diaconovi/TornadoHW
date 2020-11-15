import json
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application
from app.views import InfoView, ConfigView

#remove me pls
import os 

define('port', default=8888, help='port to listen on')

def main():
    """Construct and serve the tornado application."""

    define('myvar', default='testvar', help='port to listen on')
    define('testInit', default=111, help='port to listen on')

    config = setConfig()

    app = Application([
        ('/', InfoView), 
        ('/ConfigView', ConfigView)
    ])
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print(f'Listening on http://localhost:{options.port}')
    print(f'Options from here: {options.myvar}')
    print(f'config json: {config["testOP"]}')
    print(f'Option added: {options.testvar}')
    IOLoop.current().start()

def setConfig():
    print ('Setting up configuration from localhost')
    with open('config/config.json') as json_file:
        config = json.load(json_file)

    print(config["testOP"])
    print(config["tetsList"][0])
    print(config["tetsList"][1])

    define('testvar', default='testy', help='port to listen on')
    print (f'Options from upper class {options.myvar}')

    return config

if __name__ == "__main__":
    # execute only if run as a script
    main()
