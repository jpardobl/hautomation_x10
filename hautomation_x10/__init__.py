import logging
#logging.basicConfig(level=logging.DEBUG)

from ginsfsm.gobj import GObj
from ginsfsm.c_connex import GConnex
from ginsfsm.gaplic import GAplic, setup_gaplic_thread
from settings import MOCHAD_HOST, MOCHAD_PORT, GAPLIC_NAME, GOBJ_NAME
from callbacks import ac_rx_data, ac_command
#from ginsfsm.c_timer import GTimer
#from ginsfsm.c_srv_sock import GServerSock

DRIVER1_GCONFIG = {  # type, default_value, flag, validate_function, desc
    'host': [str, MOCHAD_HOST, 0, None, ""],
    'port': [int, MOCHAD_PORT, 0, None, ""],
}


DRIVER1_FSM = {
    'event_list': (
        'EV_DEVICE_UPDATE:top output',
        'EV_RX_DATA:bottom input',
        'EV_COMMAND: top input',
        'EV_ERROR: top output',
    ),
    'state_list': ('ST_IDLE',),
    'machine': {
        'ST_IDLE':
        (
            ('EV_RX_DATA',      ac_rx_data,     'ST_IDLE'),
            ('EV_COMMAND',      ac_command,     'ST_IDLE'),
        ),
    }
}


class DriverX10(GObj):
    """  Driver1 GObj.

    .. ginsfsm::
       :fsm: DRIVER1_FSM
       :gconfig: DRIVER1_GCONFIG

    *Input-Events:*

        * :attr:`'EV_RX_DATA'`: Receiving data.
            Receiving data from urls.

    *Output-Events:*

    """
    def __init__(self):
        GObj.__init__(self, DRIVER1_FSM, DRIVER1_GCONFIG)

    def start_up(self):
        """ Initialization zone."""
   #     self.timer = self.create_gobj(
   #         None,
   #         GTimer,
   #         self,
   #     )
        self.connex = self.create_gobj(
            'connex',
            GConnex,
            self,
            destinations=[
                (self.config.host, self.config.port),
            ],
            #host=self.config.host,
            #port=self.config.port,
            # only want receive EV_RX_DATA event
            connected_event_name=None,
            disconnected_event_name=None,
            transmit_ready_event_name=None,
        )


def start_up():
    print "loading Driver for X10 protocol"
    local_conf = {
        'router_enabled':  False,
        'GRouter.server':  False,
        'GRouter.localhost_route_ports':  8002,
        'GRouter.trace_router':  False,
        'GObj.trace_mach':  False,
        'GObj.trace_creation':  False,
        'GObj.trace_traverse':  False,
        'GObj.trace_subscription':  False,
        'GSock.trace_dump':  False,
        'GObj.logger': logging,
    }
    ga_driver = GAplic(name=GAPLIC_NAME, roles='driver', **local_conf)
    ga_driver.create_gobj(
        GOBJ_NAME,
        DriverX10,
        ga_driver,
        __unique_name__=True,
    )
    thread_driver = setup_gaplic_thread(ga_driver)
    thread_driver.start()

    return thread_driver
