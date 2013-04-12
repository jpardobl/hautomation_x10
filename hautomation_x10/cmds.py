import netcat
import settings
from utils import validate_address


def pl_switch(address, value, mochad_port=None, mochad_host=None):
    if value not in ["on", "off"]:
        raise ValueError("Switch value must be 'on' or 'off'")

    validate_address(address)

    cmd = "pl %s %s" % (address, value)

    netcat.command(cmd, mochad_port, mochad_host)
    return True


def pl_dim(address, value, mochad_port=None, mochad_host=None):
    if value not in range(0, 32):
        raise ValueError("Dim value must be in the range(0, 32)")

    validate_address(address)

    cmd = "pl %s dim %s" % (address, value)
    netcat.command(cmd, mochad_port, mochad_host)
    return True


def pl_bri(address, value, mochad_port=None, mochad_host=None):
    if value not in range(0, 32):
        raise ValueError("Dim value must be in the range(0, 32)")

    validate_address(address)

    cmd = "pl %s bri %s" % (address, value)
    netcat.command(cmd, mochad_port, mochad_host)
    return True
