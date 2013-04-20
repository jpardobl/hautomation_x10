hautomation_x10
===============

Python wrapper module which sends home automation commands to mochad

Introduction
------------

This Python module is a set of functions to make easier to send X10 home automation
commands to mochad.

At the momment the module is capable of sending the following commands

 - Power line switch command which accepts "on" and "off" values
 - Power line dim command which accepts values in the range 1..31
 - Power line bright command which accepts values in the range 1..31

By initializing the settings.MOCHAD_PORT and the settings.MOCHAD_HOST configuration directives
mochad daemon can be in any reachable host.


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


Testing
-------

>>> python hautomation_x10/tests.py


Entry Points
------------

The deploying of the module generates th following  entry points:

 - populate_x10_db: When using this module from the django-hautomation apps, it is
 necesary to populate the database with the protocol X10 information. This is the aim
 of this entry  point
 - pl_switch: entry point to help find power line switch command to developers
 - pl_dim: entry point to help find power line dim command to developers
 - pl_bri: entry point to help find power line bright command to developers
