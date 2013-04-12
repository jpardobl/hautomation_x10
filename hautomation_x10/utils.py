import re


def validate_address(address):
    m = re.match("^[a-pA-P]{1}(\d){1,2}", address)
    if not m:
        raise ValueError("Unsupported address: %s" % address)
    
    num = int(m.group(1))
    if num > 16 or num < 1:
        raise ValueError("Unsupported address: %s" % address)
