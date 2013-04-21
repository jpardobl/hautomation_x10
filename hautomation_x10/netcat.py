import socket
import settings


def command(cmd, mochad_port=None, mochad_host=None):
    if mochad_port is None:
        mochad_port = settings.MOCHAD_PORT

    if mochad_host is None:
        mochad_host = settings.MOCHAD_HOST

    return netcat(mochad_host, mochad_port, cmd)


def netcat(hostname, port, content):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.sendall(b"%s\n" % content)
    s.shutdown(socket.SHUT_WR)
    buff = ""
    while True:
        data = s.recv(1024)
        if data == "":
            break
        buff = "%s%s" % (buff, data)
    s.close()
    return repr(buff)
