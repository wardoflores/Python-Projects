import socket
import typing
import mimetypes
import os

from request import Request
import headers

HOST = "127.0.0.2"
PORT = 9000

SERVER_ROOT = os.path.abspath("www")

RESPONSE = b"""\
HTTP/1.1 200 OK
Content-type: text/html
Content-length: 24

<h1>The code worked!</h1>""".replace(b"\n", b"\r\n")

BAD_REQUEST_RESPONSE = b"""\
HTTP/1.1 400 Bad Request
Content-type: text/plain
Content-length: 11

Bad Request""".replace(b"\n", b"\r\n")

NOT_FOUND_RESPONSE = b"""\
HTTP/1.1 404 Not Found
Content-type: text/plain
Content-length: 9

Not Found""".replace(b"\n", b"\r\n")


METHOD_NOT_ALLOWED_RESPONSE = b"""\
HTTP/1.1 405 Method Not Allowed
Content-type: text/plain
Content-length: 17

Method Not Allowed""".replace(b"\n", b"\r\n")

FILE_RESPONSE_TEMPLATE = """\
HTTP/1.1 200 OK
Content-type: {content_type}
Content-length: {content_length}

""".replace("\n", "\r\n")

def serve_file(sock: socket.socket, path: str) -> None:
    """Given a socket and the relative path to a file (relative to
    SERVER_SOCK), send that file to the socket if it exists.  If the
    file doesn't exist, send a "404 Not Found" response.
    """
    if path == "/":
        path = "/index.html"

    abspath = os.path.normpath(os.path.join(SERVER_ROOT, path.lstrip("/")))
    if not abspath.startswith(SERVER_ROOT):
        sock.sendall(NOT_FOUND_RESPONSE)
        return

    try:
        with open(abspath, "rb") as f:
            stat = os.fstat(f.fileno())
            content_type, encoding = mimetypes.guess_type(abspath)
            if content_type is None:
                content_type = "application/octet-stream"

            if encoding is not None:
                content_type += f"; charset={encoding}"

            response_headers = FILE_RESPONSE_TEMPLATE.format(
                content_type=content_type,
                content_length=stat.st_size,
            ).encode("ascii")

            sock.sendall(response_headers)
            sock.sendfile(f)
    except FileNotFoundError:
        sock.sendall(NOT_FOUND_RESPONSE)
        return

with socket.socket() as server_sock:
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((HOST, PORT))
    server_sock.listen(0)
    print(f"Listening on {HOST}:{PORT}...")
    
    while True:
            client_sock, client_addr = server_sock.accept()
            print(f"Received connection from {client_addr}...")
            with client_sock:
                try:
                    request = Request.from_socket(client_sock)
                    try:
                        content_length = int(request.headers.get("content-length", "0"))
                    except ValueError:
                        content_length = 0

                    if content_length:
                        body = request.body.read(content_length)
                        print("Request body", body)

                    if request.method != "GET":
                        client_sock.sendall(METHOD_NOT_ALLOWED_RESPONSE)
                        continue

                    serve_file(client_sock, request.path)
                except Exception as e:
                    print(f"Failed to parse request: {e}")
                    client_sock.sendall(BAD_REQUEST_RESPONSE)