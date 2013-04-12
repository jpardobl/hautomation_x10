import socket
import settings
import commands


def command(cmd, mochad_port=None, mochad_host=None):
    if mochad_port is None:
        mochad_port = settings.MOCHAD_PORT

    if mochad_host is None:
        mochad_host = settings.MOCHAD_PORT

    cmd = "echo '%s' | nc %s %s" % (cmd, mochad_host, mochad_port)
    print "%s - executing command: %s" % (__file__, cmd)
    ret = commands.getoutput(cmd)
    print "%s - command output: %s" % (__file__, ret)
    #TODO validate return
    return ret
