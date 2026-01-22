from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

logging.basicConfig(
    filename='/var/log/app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/error":
            logging.error("Application error occurred")
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Error")
        else:
            logging.info("Request received")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello World")

server = HTTPServer(('', 80), Handler)
server.serve_forever()
