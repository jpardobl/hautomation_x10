from utils import validate_address


def pl_switch(self, address, value):
    if value not in ["on", "off"]:
        raise ValueError("Switch value must be 'on' or 'off'")

    validate_address(address)

    cmd = b"pl %s %s\n" % (address, value)

    self.send_event(self.connex, "EV_SEND_DATA", data=cmd)


def pl_dim(self, address, value):
    if int(value) not in range(0, 32):
        raise ValueError("Dim value must be in the range(0, 32)")

    validate_address(address)

    cmd = "pl %s dim %s" % (address, value)
    self.send_event('connex', "EV_SEND_DATA", data=cmd)


def pl_bri(self, address, value):
    if int(value) not in range(0, 32):
        raise ValueError("Dim value must be in the range(0, 32)")

    validate_address(address)

    cmd = "pl %s bright %s" % (address, value)
    self.send_event('connex', "EV_SEND_DATA", data=cmd)

