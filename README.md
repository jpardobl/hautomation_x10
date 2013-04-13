hautomation_x10
===============

Python wrapper module which sends home automation commands to mochad


Quick start
-----------

1. Install hautomation_x10: pip install -e git+https://github.com/jpardobl/hautomation_x10.git#egg=hautomation_x10

2. Make the USB cm15a device is plugged in a server

3. Make sure mochad is running on that server

4. open hautomation_x10/settings.py and set MOCHAD_HOST and MOCHAD_PORT to proper values

5. Start issuing commands.

    >>> import hautomation_x10.cmds as cmds
    >>> cmds.pl_switch("A5", "off")
    >>> cmds.pl_switch("A6", "on")
    >>> cmds.pl_dim("A3", 31)
    >>> cmds.pl_bri("A3", 4)
