import http.server
import socketserver
import json

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Open and read the pre-departure file
            with open('predeparture.json', 'r') as file:
                data = json.load(file)
                self.wfile.write(json.dumps(data).encode('utf-8'))
        else:
            self.send_error(404, "File Not Found")

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
