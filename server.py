import http.server
import socketserver

PORT = 8080

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Set the directory where index.html is located
handler = MyRequestHandler
handler.extensions_map.update({
    '.html': 'text/html',
})

# Start the server
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
