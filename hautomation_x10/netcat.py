import socket
import settings
import commands


def command(cmd, mochad_port=None, mochad_host=None):
    if mochad_port is None:
        mochad_port = settings.MOCHAD_PORT

    if mochad_host is None:
        mochad_host = settings.MOCHAD_HOST

    cmd = "echo '%s' | nc %s %s" % (cmd, mochad_host, mochad_port)
    print "%s - executing command: %s" % (__file__, cmd)
    ret = commands.getoutput(cmd)
    print "%s - command output: %s" % (__file__, ret)
    #TODO validate return
    return ret


def command_socket(cmd, mochad_port=None, mochad_host=None):
    if mochad_port is None:
        mochad_port = settings.MOCHAD_PORT

    if mochad_host is None:
        mochad_host = settings.MOCHAD_HOST

    return netcat(mochad_host, mochad_port, cmd)

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.sendall(b"%s" % content)
    #s.shutdown(socket.SHUT_WR)
    buff = ""
    while 1:
        data = s.recv(1024)
        if data == "":
            break
        buff = "%s%s" % (buff, data)
    print "Received:", repr(buff)
    s.close()
    print "Connection closed."
    return repr(buff)
