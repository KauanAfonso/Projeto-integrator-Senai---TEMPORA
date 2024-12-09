import http.server
import socketserver
import ssl

# Configurações do servidor
PORT = 5000
DIRECTORY = "./ecommerce"  # Diretório onde os arquivos estão

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'  # Página padrão
        return super().do_GET()

# Inicia o servidor com SSL
with socketserver.ThreadingTCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    # Envolvendo o socket do servidor com SSL
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    print(f"Servidor HTTPS iniciado na porta {PORT}. Acesse https://localhost:{PORT}")
    httpd.serve_forever()
