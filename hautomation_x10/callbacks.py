import simplejson
from cmds import *
import re
from utils import ADDRESS_REGEXP

def ac_command(self, event):
    data = simplejson.loads(event.kw['data'])
    #print("EJECUTAMOS COMANDO: ECIBO(%s)======> %s" % (self, data))

    cmd = data["cmd"]
    try:
        did = data["did"]
    except Exception:
        pass
    try:
        value = data["value"]
    except Exception:
        pass


    try:
        if cmd == "pl_all_lights_on":
            if "group" in data and data["group"] not in ("", None):
                group = data["group"]
                pl_all_lights_on(self, group)
                return
            #print "ERROR no recibimos el grupo"
        if cmd == "pl_all_lights_off":
            if "group" in data and data["group"] not in ("", None):
                group = data["group"]
                pl_all_lights_off(self, group)
                return
            #print "ERROR no recibimos el grupo"
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
        self.broadcast_event(
            'EV_ERROR',
            data=simplejson.dumps({"errors": [str(err), ]}))

queue = [] #queue where commands from protocol are kept while processing.


def ac_rx_data(self, event):
    data = event.kw['data']
    #TODO analize device update string and convert to json {"did": ... , "new_state": ...}
    #print("RECIBO(%s)======> %s" % (self, data))
    pattern = r"HouseUnit\:\s(%s)" % ADDRESS_REGEXP
    #print pattern
    m = re.search(pattern, data)
    if m is not None:
        queue.append(m.group(1))
        #print "encontrada la direccion"
        return

    pattern = r"Func\:\s(.+)$"
    #print "ahora miramos la funcion"
    m = re.search(pattern, data)
    if m is not None:

        address = queue.pop()
        #print "function encotnrada: %s %s" % (address, m.group(1))
        self.broadcast_event('EV_DEVICE_UPDATE', data={"did": address, "cmd": m.group(1)})
