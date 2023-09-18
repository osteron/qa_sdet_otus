import socket
from http import HTTPStatus
import re
from urllib.parse import urlparse, parse_qs

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 4042  # Port to listen on (non-privileged ports are > 1023)
end_of_stream = b'\r\n\r\n'


def read_http_request(connection):
    fragments = []
    while True:
        chunk = connection.recv(1024)
        if not chunk:
            break
        fragments.append(chunk)
        if end_of_stream in chunk:
            break
    return b"".join(fragments)


def read_remaining_http_body(connection, size_to_read):
    fragments = []
    while size_to_read > 0:
        chunk = connection.recv(min(size_to_read, 1024))
        if not chunk:
            break
        size_to_read -= len(chunk)
        fragments.append(chunk)
    return b"".join(fragments)


def create_http_response(method, source, status_code, client_headers_and_body_bytes):
    reason_phrase = HTTPStatus(status_code).phrase
    source = repr(source).encode()
    status_code = repr(status_code).encode()
    body = (
            b"Request Method: " + method + b"\r\n"
            b"Request Source: " + source + b"\r\n"
            b"Response Status: " + status_code + b" " + reason_phrase.encode() + b"\r\n" +
            client_headers_and_body_bytes
    )
    body_length = repr(len(body)).encode()
    http_response = (
            b"HTTP/1.0 200 OK\r\n"
            b"Content-Length: " + body_length + end_of_stream + body
    )
    print(http_response)
    return http_response


def get_status_code(query):
    parsed_url = urlparse(query)
    parsed_query = parse_qs(parsed_url.query)
    status = 200
    if b'status' in parsed_query:
        try:
            status = int(parsed_query[b'status'][0])
        except ValueError:
            pass
    try:
        HTTPStatus(status)
    except ValueError:
        status = 200
    return status


def handle_client(connection, client_address):
    with connection:
        client_data = read_http_request(connection)
        start_str_with_headers, body_first_part = client_data.split(end_of_stream, maxsplit=1)
        start_str_bytes, client_header_bytes = start_str_with_headers.split(b'\r\n', maxsplit=1)

        match = re.search(rb"Content-Length: (?P<length>\d+)", client_header_bytes)

        if match:
            content_length = int(match.group("length"))
            size_to_read = content_length - len(body_first_part)
            body_second_part = read_remaining_http_body(connection, size_to_read)
            body = body_first_part + body_second_part
        else:
            body = b""
        client_headers_and_body_bytes = client_header_bytes + end_of_stream + body
        method, query, _ = start_str_bytes.split()
        status_code = get_status_code(query)
        connection.send(create_http_response(method=method, source=client_address, status_code=status_code,
                                             client_headers_and_body_bytes=client_headers_and_body_bytes))


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        print(f"Running server on {HOST}:{PORT}...")
        server_socket.listen()

        while True:
            (client_connection, client_address) = server_socket.accept()
            handle_client(client_connection, client_address)
            print(f"Sent data to {client_address}")


if __name__ == "__main__":
    run_server()
