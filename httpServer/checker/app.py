import http.server
import urllib.request

class Handler(http.server.SimpleHTTPRequestHandler):
    def send_internal(self, url):
        try:
            request = urllib.request.Request(url)
            request.selector = self.path
            request.headers = self.headers
            response = urllib.request.urlopen(request)
            return response
        except:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b'Error sending request')
            return None

    def do_GET(self):
        node_response = self.send_internal('http://node:8001')
        if node_response is None:
            return

        python_response = self.send_internal('http://python:8002')
        if python_response is None:
            return

        if node_response.read().strip() != python_response.read().strip():
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b'Responses do not match')
            return
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Responses match')
        return

http.server.HTTPServer(('0.0.0.0', 8000), Handler).serve_forever()
