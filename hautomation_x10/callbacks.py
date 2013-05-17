import simplejson
from cmds import *
import re
from utils import ADDRESS_REGEXP

def ac_command(self, event):
    data = simplejson.loads(event.kw['data'])
    print("RECIBO(%s)======> %s" % (self, data))

    cmd = data["cmd"]
    did = data["did"]
    value = data["value"]

    try:
        if cmd == "pl_switch":
            pl_switch(self, did, value)
            return
        if cmd == "pl_dim":
            pl_dim(self, did, value)
            return
        if cmd == "pl_bri":
            pl_bri(self, did, value)
            return
    except ValueError, err:
        self.broadcasr_event(
            'EV_ERROR',
            data=simplejson.dumps({"errors": [err, ]}))


def ac_rx_data(self, event):
    data = event.kw['data']
    #TODO analize device update string and convert to json {"did": ... , "new_state": ...}
    print("RECIBO(%s)======> %s" % (self, data))
    pattern = "HouseUnit\:\s(%s)" % ADDRESS_REGEXP
    print pattern
    m = re.search(pattern, data)
    if m is not None:
        print m.group(1)
    self.broadcast_event('EV_DEVICE_UPDATE', data=data)
