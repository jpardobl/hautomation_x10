from utils import validate_address
from driver import netcat

try:
    from django.conf import settings
except ImportError:
    import settings

import logging



def pl_switch(address, value):
    if value not in ["on", "off"]:
        raise ValueError("Switch value must be 'on' or 'off'")

    validate_address(address)

    cmd = b"pl %s %s\n" % (address, value)

    netcat(settings.MOCHAD_HOST, settings.MOCHAD_PORT, cmd)


def pl_dim(address, value):
    if int(value) not in range(0, 32):
        raise ValueError("Dim value must be in the range(0, 32)")

    validate_address(address)

    cmd = "pl %s dim %s\n" % (address, value)
    netcat(settings.MOCHAD_HOST, settings.MOCHAD_PORT, cmd)


def pl_bri(address, value):
    if int(value) not in range(0, 32):
        raise ValueError("Dim value must be in the range(0, 32)")

    validate_address(address)

    cmd = "pl %s bright %s\n" % (address, value)
    netcat(settings.MOCHAD_HOST, settings.MOCHAD_PORT, cmd)


def pl_all_lights_on(group):
    cmd = "pl %s1 extended_code_1 0 5\n" % group
    netcat(settings.MOCHAD_HOST, settings.MOCHAD_PORT, cmd)


def pl_all_lights_off(group):
    cmd = "pl %s1 extended_code_1 0 11\n" % group
    netcat(settings.MOCHAD_HOST, settings.MOCHAD_PORT, cmd)
