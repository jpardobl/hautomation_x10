import re

ADDRESS_REGEXP = "[a-pA-P](\d{0,2})"


def validate_address(address):
    m = re.match("^%s$" % ADDRESS_REGEXP, address)
    if not m:
        raise ValueError("Unsupported address: %s" % address)

    num = int(m.group(1))
    if num > 16 or num < 1:
        raise ValueError("Unsupported address: %s" % address)
