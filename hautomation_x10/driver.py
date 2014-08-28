

import socket

try:
    from django.conf import settings
except ImportError:
    import settings

import logging
driver_logger = logging.getLogger("driver")
driver_logger.setLevel(settings.LOG_LEVEL)


def netcat(hostname, port, content):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        driver_logger.debug("Trying connection to: %s:%s" % (hostname, port))
        s.connect((hostname, port))

        driver_logger.debug("Connected to: %s:%s" % (hostname, port))
        s.sendall(b"%s\n" % content)
        s.shutdown(socket.SHUT_WR)
        buff = ""

        while True:
            data = s.recv(1024)
            if data == "":
                break
            buff = "%s%s" % (buff, data)
        driver_logger.debug("Received: %s" % repr(buff))
        s.close()
        driver_logger.debug("Connection closed.")
        return repr(buff)
    except Exception as ex:
        driver_logger.error("ERROR: %s" % ex)
        raise ex